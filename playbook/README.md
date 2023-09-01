# Ansible playbook

Необходимо написать Ansible playbook, который выполняет на хосте следующие действия:

- [x] создает нового пользователя cloudru с паролем cloudpass
- [x] разрешает на хосте авторизацию через ssh по ключу
- [x] запрещает логин по ssh от пользователя root
- [x] копирует предоставленный публичный ключ для пользователя `cloudru`


## Запуск плейбука

1. В файле [`ansible.cfg`](./ansible.cfg) написать имя пользователя в 
параметре `remote_user`

2. Указать правильный адрес до машины в файле [`hosts.yaml`](./hosts.yaml)

3. 
    - Или добавить путь к ключу ssh  в файл [`hosts.yaml`](./hosts.yaml)
    - Или файле [`ansible.cfg`](./ansible.cfg) включить запрос пароля при старте плейбука

```bash
cd ./playbook
ansible-playbook ./configure_host.yaml
```

## Тестирование

```bash
ansible all -u cloudru -k -i ./hosts.yaml -m ping
```