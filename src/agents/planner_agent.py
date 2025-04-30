from .base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    """行程规划 Agent"""
    
    def __init__(self):
        super().__init__("Planner")
    
    def _get_instructions(self) -> str:
        return """你是一个专业的旅游行程规划师。你的职责是：
1. 根据用户需求制定合适的行程计划
2. 考虑以下因素：
   - 旅行时间安排
   - 景点推荐
   - 游览顺序
   - 停留时间
   - 特别注意事项
3. 提供详细的行程规划
4. 考虑用户的预算和偏好
5. 确保行程的合理性和可行性

请记住：
- 保持行程的灵活性
- 考虑交通时间
- 注意景点开放时间
- 提供备选方案
- 关注用户安全"""
    
    async def process(self, message: str) -> str:
        """处理行程规划请求"""
        return await super().process(message) 