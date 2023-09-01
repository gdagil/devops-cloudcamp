import uvicorn

from core.config import settings

from fastapi import FastAPI, HTTPException, status




app = FastAPI(
    title="Web приложение на Python",
    root_path_in_servers=False
)


@app.get(
    "/hostname", 
    status_code=200,
    response_model=str,
    description="Отдает имя хоста, на котором запущено приложение"
)
def get_hostname() -> str:
    return settings._hostname


@app.get(
    "/author", 
    status_code=200,
    response_model=str,
    description="""Возвращает значение переменной окружения $AUTHOR, 
    в которой задано имя или никнейм человека, выполняющего это задание"""
)
def get_author() -> str:
    return settings.author


@app.get(
    "/id", 
    status_code=200,
    response_model=str,
    description="""Возвращает значение переменной окружения $UUID, 
    содержащее любую произвольную строку-идентификатор в формате uuid"""
)
def get_id() -> str:
    return str(settings.uuid)


@app.get(
    "/readiness", 
    status_code=200,
    response_model=dict[str,str],
)
def readiness_probe() -> dict[str,str]:
    return {"status": "success"}


@app.get(
    "/liveness", 
    status_code=200,
    response_model=dict[str,str],
)
def liveness_probe() -> dict[str,str]:
    if not settings._hostname and settings.author and settings.uuid:
        return {"status": "success"}
    else:
        raise HTTPException(status.HTTP_503_SERVICE_UNAVAILABLE)




if __name__ == "__main__":
    uvicorn.run(
            app, 
            port=8000, 
            host="0.0.0.0", 
            reload=False, 
            use_colors=False,
            server_header=False,
        )