from naive_rag_agent.app import app
from naive_rag_agent.routes import router

app.include_router(router)


def run() -> None:
    import uvicorn

    uvicorn.run("naive_rag_agent.main:app", host="127.0.0.1", port=8000, reload=True)
