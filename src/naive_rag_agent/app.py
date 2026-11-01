from fastapi import FastAPI

from naive_rag_agent.config import settings

tags_metadata = [
    {
        "name": "system",
        "description": "服务健康检查等系统级接口。",
    },
    {
        "name": "greeting",
        "description": "问候相关的示例接口。",
    },
]

app = FastAPI(
    title="Naive RAG Agent API",
    description=(
        "一个基于 FastAPI 的朴素 RAG Agent 服务。\n\n"
        "接口文档由 FastAPI 自动生成,基于 OpenAPI 3.1 规范。"
    ),
    version=settings.version,
    debug=settings.debug,
    openapi_tags=tags_metadata,
    contact={
        "name": "naiveRAGagent",
        "url": "https://example.com",
        "email": "dev@example.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)
