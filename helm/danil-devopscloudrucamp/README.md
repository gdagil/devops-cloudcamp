# Python webapp packaged by gdagil

Простое приложение на фреймворке [`FastAPI`](https://fastapi.tiangolo.com/) - [тут](../app/README.md)

## Prerequisites
* Kubernetes 1.19+
* Helm 3.2.0+

## Установка
Добавьте репозиторий helm
```bash
helm repo add gdagil https://gdagil.github.io/devops-cloudcamp/
helm repo update
```

Ставим последний релиз
```bash
helm install danil-app --namespace danil-devopscloudrucamp --create-namespace gdagil/danil-devopscloudrucamp
```