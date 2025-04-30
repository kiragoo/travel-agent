from .base_agent import BaseAgent

class TransportAgent(BaseAgent):
    """交通查询 Agent"""
    
    def __init__(self):
        super().__init__("Transport")
    
    def _get_instructions(self) -> str:
        return """你是一个专业的交通出行顾问。你的职责是：
1. 推荐最佳出行方式
2. 提供路线规划
3. 估算交通时间
4. 计算交通费用
5. 提供实时建议

请记住：
- 考虑多种选择
- 注意时间安排
- 关注交通状况
- 提供备选方案
- 确保安全可靠""" 