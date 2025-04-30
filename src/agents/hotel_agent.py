from .base_agent import BaseAgent

class HotelAgent(BaseAgent):
    """住宿预订 Agent"""
    
    def __init__(self):
        super().__init__("Hotel")
    
    def _get_instructions(self) -> str:
        return """你是一个专业的住宿预订顾问。你的职责是：
1. 推荐合适的住宿
2. 分析位置优势
3. 提供设施信息
4. 比较价格和评价
5. 提供预订建议

请记住：
- 考虑预算范围
- 关注地理位置
- 检查设施配套
- 注意安全因素
- 查看用户评价""" 