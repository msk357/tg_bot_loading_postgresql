# Создаем образ на основе базового слоя python
FROM python:3.9.6-slim
# Создаем рабочии директории
# tg-bot - хранятся основные python-файлы для работы бота
# infra_project - директория с env и Dockerfile
# csv - в директории хранятся файлы csv, которые отправляют в бот
RUN mkdir /tg_bot_loading_postgresql_docker
RUN mkdir /tg_bot_loading_postgresql_docker/tg_bot
RUN mkdir /tg_bot_loading_postgresql_docker/infra_project
RUN mkdir /tg_bot_loading_postgresql_docker/csv
WORKDIR tg_bot_loading_postgresql_docker
# Копируем файл requirements
COPY ../requirements.txt .
# Устанавливаем пакеты, необходимые для работы
RUN pip install -r ./requirements.txt --no-cache-dir
# Копируем модули бота в рабочую директорию
COPY ../tg_bot ./tg_bot
# Запускаем ТГ-бот
CMD ["python3", "tg_bot/bot_for_load.py"]
