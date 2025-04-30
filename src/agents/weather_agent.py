from .base_agent import BaseAgent

class WeatherAgent(BaseAgent):
    """天气查询 Agent"""
    
    def __init__(self):
        super().__init__("Weather")
    
    def _get_instructions(self) -> str:
        return """你是一个专业的天气信息顾问。你的职责是：
1. 提供准确的天气预报
2. 分析天气对旅行的影响
3. 提供穿衣建议
4. 提供户外活动建议
5. 预警恶劣天气

请记住：
- 关注天气变化
- 提供详细预报
- 考虑季节特点
- 注意天气风险
- 给出应对建议""" 