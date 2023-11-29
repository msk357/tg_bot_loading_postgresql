# Создаем образ на основе базового слоя python
FROM python:3.9.6-slim
# Создаем рабочую директорию
RUN mkdir /tg_bot_loading_postgresql_docker
RUN mkdir /tg_bot_loading_postgresql_docker/tg_bot
RUN mkdir /tg_bot_loading_postgresql_docker/infra_project
RUN mkdir /tg_bot_loading_postgresql_docker/csv
WORKDIR tg_bot_loading_postgresql_docker
# Копируем файл requirements
COPY requirements.txt .
# Устанавливаем пакеты, необходимые для работы
RUN pip install -r ./requirements.txt --no-cache-dir
# Копируем модули бота в рабочую директорию
COPY tg_bot ./tg_bot
COPY infra_project/.env ./infra
# Запускаем ТГ-бот
CMD ["python3", "tg_bot/bot_for_load.py"]
