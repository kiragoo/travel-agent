from setuptools import setup, find_packages

setup(
    name="travel-agent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai>=1.12.0",
        "openai-agents",
        "langchain>=0.1.9",
        "python-dotenv>=1.0.0",
        "requests>=2.31.0",
        "pydantic>=2.5.0",
        "pydantic-settings>=2.1.0",
        "fastapi>=0.104.0",
        "uvicorn>=0.24.0",
        "python-jose>=3.3.0",
        "passlib>=1.7.4",
        "python-multipart>=0.0.6",
    ],
) 