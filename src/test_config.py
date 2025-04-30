from utils.config import settings

def test_settings():
    """测试配置"""
    print("OpenAI API Key:", settings.OPENAI_API_KEY)
    print("SiliconFlow API Key:", settings.SILICONFLOW_API_KEY)
    print("OpenAI Model:", settings.OPENAI_MODEL)
    print("OpenAI Temperature:", settings.OPENAI_TEMPERATURE)
    print("Debug Mode:", settings.DEBUG)

if __name__ == "__main__":
    test_settings() 