from enum import Enum

from pydantic import BaseModel, Field


class Message(BaseModel):
    message: str = Field(..., description="返回的文本消息", examples=["Hello World"])


class Status(str, Enum):
    ok = "ok"
    degraded = "degraded"
    error = "error"


class ServiceInfo(BaseModel):
    name: str = Field(..., description="服务名称", examples=["naive-rag-agent"])
    version: str = Field(..., description="服务版本", examples=["0.1.0"])
    uptime_seconds: float = Field(
        ..., description="进程自启动至今的运行秒数", examples=[12.345]
    )


class HealthResponse(BaseModel):
    status: Status = Field(..., description="服务整体健康状态")
    service: ServiceInfo = Field(..., description="服务自身信息")
