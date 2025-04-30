from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import os

from ..agents.controller_agent import ControllerAgent
from ..agents.planner_agent import PlannerAgent
from ..agents.transport_agent import TransportAgent
from ..agents.hotel_agent import HotelAgent
from ..agents.food_agent import FoodAgent
from ..agents.weather_agent import WeatherAgent
from ..agents.budget_agent import BudgetAgent

app = FastAPI(title="旅游助手")

# 获取项目根目录的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 设置模板和静态文件
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "src", "templates"))
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "src", "static")), name="static")

# 初始化控制器代理
controller = ControllerAgent()

# 注册所有代理
planner = PlannerAgent()
transport = TransportAgent()
hotel = HotelAgent()
food = FoodAgent()
weather = WeatherAgent()
budget = BudgetAgent()

controller.register_agent(planner)
controller.register_agent(transport)
controller.register_agent(hotel)
controller.register_agent(food)
controller.register_agent(weather)
controller.register_agent(budget)

class ChatMessage(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/chat", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.post("/api/chat")
async def chat(chat_message: ChatMessage):
    response = await controller.process(chat_message.message)
    return {"response": response}

@app.get("/health")
async def health_check() -> dict:
    """健康检查"""
    return {"status": "healthy"} 