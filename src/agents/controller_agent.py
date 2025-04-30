from typing import Dict, Optional
from .base_agent import BaseAgent
from ..utils.config import settings

class ControllerAgent(BaseAgent):
    """主控 Agent"""
    
    def __init__(self):
        super().__init__("Controller")
        self.sub_agents: Dict[str, BaseAgent] = {}
        
    def _get_instructions(self) -> str:
        return """你是一个旅游助手系统的主控 Agent。你的职责是：
1. 分析用户的需求
2. 将需求分配给合适的子 Agent
3. 协调子 Agent 的工作
4. 整合子 Agent 的回复
5. 确保回复的连贯性和完整性

请记住：
- 保持对话的连贯性
- 确保信息的准确性
- 提供个性化的服务
- 注意用户的安全和隐私"""
        
    def register_agent(self, agent: BaseAgent) -> None:
        """注册子 Agent"""
        if not isinstance(agent, BaseAgent):
            raise TypeError("Agent must be an instance of BaseAgent")
        self.sub_agents[agent.name] = agent
        
    def get_agent(self, name: str) -> Optional[BaseAgent]:
        """获取子 Agent"""
        return self.sub_agents.get(name)
    
    async def process(self, message: str) -> str:
        """处理用户输入"""
        # 分析意图
        intent = await self._analyze_intent(message)
        
        # 根据意图选择合适的 Agent
        if agent := self.get_agent(intent):
            response = await agent.process(message)
        else:
            response = "抱歉，我暂时无法处理这个请求。"
            
        return response
    
    async def _analyze_intent(self, message: str) -> str:
        """分析用户意图"""
        prompt = f"""作为一个旅游助手系统的意图分析器，请分析以下用户输入属于哪个子系统：
用户输入: {message}

可选子系统:
- Planner: 行程规划
- Transport: 交通查询
- Hotel: 住宿预订
- Food: 美食推荐
- Weather: 天气查询
- Budget: 预算管理

请只返回一个子系统的名称。"""
        
        # 添加系统消息
        messages = [
            {"role": "system", "content": "你是一个专业的意图分析器，请准确分析用户意图。"},
            {"role": "user", "content": prompt}
        ]
        
        # 使用基类的 process 方法来调用 API
        response = await super().process(prompt)
        return response.strip()
        
    async def cleanup(self) -> None:
        """清理资源"""
        # 清理子 Agent
        for agent in self.sub_agents.values():
            await agent.cleanup()
            
        # 清理自身
        self.messages.clear()
        self.context.clear() 