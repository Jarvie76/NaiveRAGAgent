import time

from fastapi import APIRouter

from naive_rag_agent.config import settings
from naive_rag_agent.schemas import (
    HealthResponse,
    Message,
    ServiceInfo,
    Status,
)

router = APIRouter()

# 进程启动时刻,用于计算 uptime(单调时钟,不受系统时间调整影响)
_START_TIME = time.monotonic()


@router.get(
    "/health",
    tags=["system"],
    summary="健康检查",
    description="返回服务自身信息与状态,可用于探针/监控。",
    response_model=HealthResponse,
    response_description="服务健康检查结果",
)
async def health():
    return HealthResponse(
        status=Status.ok,
        service=ServiceInfo(
            name=settings.service_name,
            version=settings.version,
            uptime_seconds=round(time.monotonic() - _START_TIME, 3),
        ),
    )


@router.get(
    "/hello/{name}",
    tags=["greeting"],
    summary="向指定对象问好",
    description="根据路径参数 `name` 返回一条问候消息。",
    response_model=Message,
)
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
