# Каркас телеграм бота

## Компоненты:

- Бот на aiogram
- БД sqlite, либо postgresql
- модели БД на sqlalchemy

## перед запуском

Отредактировать конфиг tgbot/bot/config.py
Создать файл .env с параметрами:

```
TG_TOKEN=XXXX
```

Если требуется бд postgres, то дополнительно:

```
POSTGRES_DB=db_bot
POSTGRES_USER=postgres
POSTGRES_PASSWORD=qwer!123
```

Ккомпоз файл для postgres: docker-compose.postgre.yml