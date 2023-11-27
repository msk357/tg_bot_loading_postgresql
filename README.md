# TG-bot downloader

![Иллюстрация к механике проекта](https://github.com/msk357/tgbot_loading_data_postgresql/raw/main/for_readme.jpg)

## Описание проекта.
Обработка CSV файлов для дальнейшего сохранения файла на сервере и загрузки данных в PostgreSQL. Данные используются для визуализациии и построения дашбородов. Функционал визуализации данных релизован в "Datalens" и является второй частью проекта.

#### Ссылка на дашборд - <https://datalens.yandex/s9nefwfbptoah?tab=2Y>

### Проект основан на технологиях:
- Python 3.9.6
- PostgreSQL
- Telegram API
- Python-telegram-bot v.13.7
- Pandas
- GitActions
- Psycopg2-binary
- Docker

### Запуск проекта
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/msk357/tgbot_loading_data_postgresql
```
Провести установку Docker:
```
sudo apt install docker.io
```
Перейти в папку infra и подготовить среду для запуска контейнера:
```
cd infra
sudo nano .env
```
Внести имзенения в файл .env:
```
TOKEN=<Your_token>
DB_NAME=<Your_name_DB>
POSTGRES_USER=<Your_name_user>
POSTGRES_PASSWORD=<Your_password>
DB_HOST=<Your_name_host>
DB_PORT=<Your_name_port>
```
Запустить контейнер Docker:
```
docker-compose up -d --build
```