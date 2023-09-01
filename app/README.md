# Python webapp

Простое приложение на фреймворке [`FastAPI`](https://fastapi.tiangolo.com/)

| Endpoint    |                                                                                                            Что делает |                     Example Response |
|-------------|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------|
| `/id`       | Возвращает значение переменной окружения $UUID, содержащее любую произвольную строку-идентификатор в формате uuid     |`bc3b0e31-edbf-464b-bc64-b71083083fb8`|
| `/hostname` | Отдает имя хоста, на котором запущено приложение                                                                      |`devopscloudrucamp-68b99dd866-4qzmr`  |
| `/author"`  | Возвращает значение переменной окружения $AUTHOR, в которой задано имя или никнейм человека, выполняющего это задание |`Danila Gudynin`                      |
| `/readiness`| Проба на готовность приложения к роботе                                                                               |`{"status": "success"}`               |
| `/liveness` | Проба на подтверждение работоспособности приложения                                                                   |`{"status": "success"}`               |

## Запуск
Два варианта

1. Docker-compose
```bash
cd ./app
docker compose up
```

2. Docker
```bash
docker build -t simple-app ./app
docker run -it -p 8000:8000 -e AUTHOR=Danila_Gudynin -e UUID=bc3b0e31-edbf-464b-bc64-b71083083fb8 simple-app 
```