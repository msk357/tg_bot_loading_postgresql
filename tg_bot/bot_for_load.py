"""
Модуль с основной логикой работы бота.
Бот считывает сообщение пользователя и сверяет текст с доступными таблицами БД.
Названия таблиц БД и колонок таблицы CSV хранятся в переменной TABLES_LIST_DB.
Если сообщение проходит проверку, файл CSV обрабатывается функциями из модуля convert_csv.py.
После успешной обработки файл загружается с помощью функции из модуля connect_db.py.
"""
import os
import telegram
import traceback
import app_logger

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from settings import PATH_DIRECTORY, TOKEN
from convert_csv import convert_csv_data
from connect_db import load_csv_db, TABLES_LIST_DB

PATH_DIRECTORY = PATH_DIRECTORY
TOKEN: str = TOKEN

# Настройка логирования, основная логика добавлена в модуле app_logger
logger = app_logger.logger_get(__name__)

"""
Функция-команда с инструкцией по работе телеграмм-ботом.
Возвращает краткую инструкцию для пользователя.
"""


def instructions(update, context):
    text_start: str = ('Для обновления данных необходимо отправить файл в формате CSV и '
                       'прописать название обновляемой таблицы. Список доступных для обновления таблиц '
                       'достен при вызове комнады "tables". Файл и текстовое '
                       'название таблицы отправьте одним сообщением.'
                       )

    # Отправляем сообщение с кнопкой
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text_start
                             )


"""
Функция-команда выдает название доступных для обновления таблиц DB.
"""


def tables(update, context):
    # сохраняем в переменную current_tables_db названия доступных для обновления таблиц
    current_tables_db: str = ''.join([str(x) + '\n' for x in TABLES_LIST_DB.keys()])
    text_instruction: str = f'Доступные таблицы для обновления данных: \n{current_tables_db}'

    # Отправляем сообщение с кнопкой
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=text_instruction
                             )


"""
Функция отвечает за обработку входящего файла CSV и ожидает два агумента:
update - запрос к ТГ-боту, проверка входящих сообщений;
context - входящая информация от пользователя с названием обновляемой таблицы DB и CSV-файлом.
Функция сохраняет CSV-файл в переменную file и входящее сообщение в message.
В name_table_load из message сохраняется название таблицы DB для подготовки CSV-файла.
"""


def handle_file(update, context):
    # сохраняем файл в переменную file и в переменной message хранится сообщение пользователя
    try:
        file = context.bot.get_file(update.message.document.file_id)
        # разделяем входящее сообщение от пользователя на название таблицы и дату
        message = update.message.caption.lower()
        context.user_data['message'] = message
        name_table_load: str = message
        # file_name хранится имя обновляемой таблицы
        file_name = os.path.join(f'{name_table_load}.csv')

        if name_table_load in TABLES_LIST_DB.keys() and file_name.endswith('.csv'):
            # переназначем путь для file_name и сохраняем CSV по заданному пути
            file_name = os.path.join(PATH_DIRECTORY, f'{name_table_load}.csv')
            file.download(file_name)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Файл успешно сохранен на сервере.'
                                     )

            # после сохранения файла применяются функции обработки CSV и загрузки данных в БД
            table_context: dict[str] = TABLES_LIST_DB[name_table_load]

            try:
                convert_csv_data(name_table_load, table_context)
                update.message.reply_text(
                    text='Файл подготовлен к загрузке'
                )
            except Exception as error:
                update.message.reply_text(
                    text=f'Ошибка при подготовке файла CSV:\n{str(error)}'
                )
                app_logger.logger.error(f'Ошибка при обработке файла:\n{str(error)}\n{traceback.format_exc()}')

            try:
                load_csv_db(PATH_DIRECTORY, name_table_load)
                update.message.reply_text(
                    text='Данные успешно загружены в базу данных'
                )

            except Exception as error:
                update.message.reply_text(
                    text=f'Ошибка при загрузке в базу данных:\n{str(error)}\n{traceback.format_exc()}'
                )
                app_logger.logger.error(f'Ошибка при загрузке в базу данных:'
                                        f'\n{str(error)}\n{traceback.format_exc()}')
        else:
            update.message.reply_text(
                text=f'Ошибка - названия таблицы нет в БД или формат файла не соотвествует CSV.'
            )
            app_logger.logger.error(f'Ошибка - названия таблицы нет в БД или формат файла не соотвествует CSV.')

    except Exception as error:
        update.message.reply_text(
            text=f'Ошибка - проверьте тип файла или название отчета.\n{str(error)}\n{traceback.format_exc()}'
        )
        app_logger.logger.error(f'Ошибка - проверьте тип файла или название отчета.\n{str(error)}')


"""
Основная логика модуля, функция инициирует запуск бота.
В качестве основного аремента функция принимает токен для запуска бота.
В add_handlers регистрируются команды-обработчики.
"""


def main():
    bot = telegram.Bot(token=TOKEN)
    updater = Updater(bot=bot, use_context=True)
    dispatcher = updater.dispatcher

    # присваиваем переменным значения обработчиков и регистрируем обработчики через dispatcher
    dispatcher.add_handler(CommandHandler('instructions', instructions))
    dispatcher.add_handler(CommandHandler('tables', tables))
    dispatcher.add_handler(MessageHandler(Filters.document.file_extension('csv') | Filters.text, handle_file))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
