# 旅游助手项目

基于 openai-agent-sdk 开发的智能旅游助手系统。

## 环境要求

- Python 3.8+
- pip
- virtualenv

## 安装步骤

1. 创建虚拟环境：
```bash
python -m venv venv
```

2. 激活虚拟环境：
- Windows:
```bash
.\venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 配置环境变量：
- 复制 `.env.example` 为 `.env`
- 在 `.env` 文件中填入您的 API 密钥：
  - OPENAI_API_KEY
  - SILICONFLOW_API_KEY

## 项目结构

```
travel-agent/
├── venv/                  # 虚拟环境
├── requirements.txt       # 项目依赖
├── .env.example          # 环境变量模板
├── README.md             # 项目说明
└── src/                  # 源代码目录
    ├── agents/           # Agent 实现
    ├── api/              # API 接口
    ├── models/           # 数据模型
    └── utils/            # 工具函数
```

## 开发说明

1. 确保在开发前激活虚拟环境
2. 遵循 PEP 8 编码规范
3. 使用类型注解
4. 编写单元测试
5. 保持代码文档更新 