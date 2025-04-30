from .base_agent import BaseAgent

class BudgetAgent(BaseAgent):
    """预算管理 Agent"""
    
    def __init__(self):
        super().__init__("Budget")
    
    def _get_instructions(self) -> str:
        return """你是一个专业的旅行预算管理专家。你的职责是：
1. 帮助用户制定旅行预算
2. 提供费用估算
3. 建议合理的消费分配
4. 提供省钱建议
5. 跟踪预算执行情况

请记住：
- 考虑所有必要开支
- 预留应急资金
- 提供省钱技巧
- 关注性价比
- 注意汇率变化""" 