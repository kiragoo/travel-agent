from typing import Any, Dict, List, Optional
import httpx
import json
import asyncio
from ..utils.config import settings

class BaseAgent:
    """基础 Agent 类"""
    
    def __init__(self, name: str):
        self._name = name
        self.messages: List[Dict[str, str]] = []
        self.context: Dict[str, Any] = {}
        
    def _get_instructions(self) -> str:
        """获取 Agent 指令"""
        return f"""你是一个专业的{self._name}助手。请根据用户的需求提供帮助。"""
    
    async def _make_api_request(self, client: httpx.AsyncClient, retries: int = 3) -> Dict[str, Any]:
        """发送 API 请求，带重试机制"""
        last_error = None
        for attempt in range(retries):
            try:
                print(f"正在发送请求到 {settings.MODEL_BASE_URL}/chat/completions (第 {attempt + 1} 次尝试)")
                print(f"请求头: Authorization: Bearer {settings.SILICONFLOW_API_KEY[:5]}...")
                print(f"请求体: {json.dumps({
                    'model': settings.MODEL_NAME,
                    'messages': self.messages,
                    'temperature': settings.MODEL_TEMPERATURE,
                    'max_tokens': settings.MODEL_MAX_TOKENS
                }, ensure_ascii=False, indent=2)}")
                
                response = await client.post(
                    "/chat/completions",
                    headers={"Authorization": f"Bearer {settings.SILICONFLOW_API_KEY}"},
                    json={
                        "model": settings.MODEL_NAME,
                        "messages": self.messages,
                        "temperature": settings.MODEL_TEMPERATURE,
                        "max_tokens": settings.MODEL_MAX_TOKENS
                    },
                    timeout=60.0  # 设置 60 秒超时
                )
                
                print(f"响应状态码: {response.status_code}")
                print(f"响应头: {dict(response.headers)}")
                
                if response.status_code != 200:
                    print(f"错误响应内容: {response.text}")
                    response.raise_for_status()
                    
                result = response.json()
                print(f"响应内容: {json.dumps(result, ensure_ascii=False, indent=2)}")
                return result
                
            except (httpx.TimeoutException, httpx.ReadTimeout) as e:
                last_error = e
                if attempt < retries - 1:
                    wait_time = (attempt + 1) * 5  # 递增等待时间
                    print(f"请求超时，等待 {wait_time} 秒后重试...")
                    await asyncio.sleep(wait_time)
                continue
            except Exception as e:
                raise e
        
        raise Exception(f"在 {retries} 次尝试后仍然失败: {str(last_error)}")
    
    async def process(self, message: str) -> str:
        """处理输入消息"""
        try:
            # 添加系统指令
            if not self.messages:
                self.messages.append({
                    "role": "system",
                    "content": self._get_instructions()
                })
            
            # 添加用户消息
            self.messages.append({
                "role": "user",
                "content": message
            })
            
            # 调用 SiliconFlow API
            async with httpx.AsyncClient(
                base_url=settings.MODEL_BASE_URL,
                timeout=httpx.Timeout(60.0, connect=10.0)  # 连接超时10秒，总超时60秒
            ) as client:
                try:
                    result = await self._make_api_request(client)
                except httpx.RequestError as e:
                    print(f"请求错误: {str(e)}")
                    raise Exception(f"API 请求失败: {str(e)}")
                except httpx.HTTPStatusError as e:
                    print(f"HTTP 错误: {str(e)}")
                    raise Exception(f"API 返回错误状态码: {e.response.status_code}")
                except json.JSONDecodeError as e:
                    print(f"JSON 解析错误: {str(e)}")
                    raise Exception("API 返回了无效的 JSON 数据")
            
            # 获取助手回复
            try:
                assistant_message = result["choices"][0]["message"]["content"]
            except (KeyError, IndexError) as e:
                print(f"响应格式错误: {str(e)}")
                print(f"完整响应: {json.dumps(result, ensure_ascii=False, indent=2)}")
                raise Exception("API 响应格式不正确")
            
            # 保存助手回复到消息历史
            self.messages.append({
                "role": "assistant",
                "content": assistant_message
            })
            
            # 如果消息历史太长，保留最后10条消息
            if len(self.messages) > 10:
                self.messages = [self.messages[0]] + self.messages[-9:]
            
            return assistant_message
            
        except Exception as e:
            error_msg = f"处理消息时出错: {str(e)}"
            print(error_msg)
            raise Exception(error_msg)
    
    def update_context(self, key: str, value: Any) -> None:
        """更新上下文"""
        self.context[key] = value
    
    def get_context(self, key: str) -> Optional[Any]:
        """获取上下文"""
        return self.context.get(key)
    
    def clear_context(self) -> None:
        """清除上下文"""
        self.context.clear()
        self.messages = []
        
    @property
    def name(self) -> str:
        """获取 Agent 名称"""
        return self._name 