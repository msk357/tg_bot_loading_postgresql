"""
Модуль для общих настроек проекта.
В модуле хранятся секретные переменные из .env и
основные глобальные переменные.
"""
import os
from dotenv import load_dotenv


load_dotenv()
# указываем путь к файлу .env
env_path = '/tg_bot_loading_postgresql_docker/infra_project/.env'
load_dotenv(dotenv_path=env_path)

# токен для ТГ-бота
TOKEN = os.getenv("TOKEN")

# переменные для подключения к DB
DATABASE = os.getenv("DATABASE")
PASSWORD = os.getenv("PASSWORD")
USER_DB = os.getenv("USER_DB")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")

# путь к файлу CSV
PATH_DIRECTORY = os.getenv("PATH_DIRECTORY")


"""
Основная переменная.
Ключи словаря - это названия обновляемых таблиц в DB.
В словаре с названием таблицы хранятся ключи, используемые для обработки CSV.
column_date - хранит название столбцов CSV-файла с типом поля date.
column_int - хранит название столбцов CSV-файла с типом поля int.
columns_name_csv - названия столбцов CSV-файла,
которые необходимо загрузить в таблицу DB.
columns_name_db - названия столбцов таблицы DB, которые необходимо обновить.
table_id - название PK в обновляемой таблице DB типа int.
address_id - название PK в обновляемой таблице DB типа str.
"""
TABLES_LIST_DB: dict[str] = {
                    'teko': {
                        'column_date': [
                            'Время'
                        ],
                        'column_int': [
                            'Сумма в валюте получения',
                            'POSID'
                        ],
                        'columns_name_csv': [
                            'Время',
                            'Global Id',
                            'Товар',
                            'Наименование номенклатуры',
                            'POSID',
                            'Сумма в валюте получения'
                        ],
                        'columns_name_db': [
                            'datesale',
                            'teko_id',
                            'product',
                            'product_name',
                            'posid',
                            'sumsale'
                        ],
                        'table_id': [
                            'teko_id'
                        ]
                    },  # ok
                    'stores': {
                        'column_int': [
                            'PosID',
                            'Аренда'
                        ],
                        'columns_name_csv': [
                            'PosID',
                            'Адрес ТТ',
                            'Регион',
                            'Аренда',
                            'Кластер',
                            'Супервайзер',
                            'Кофе',
                            'Статус'
                        ],
                        'columns_name_db': [
                            'posid',
                            'address',
                            'region',
                            'rent',
                            'format',
                            'supervisor',
                            'coffee',
                            'status'
                        ],
                        'table_id': [
                            'posid'
                        ]
                    },  # ok
                    'teko_category': {
                        'columns_name_csv': [
                            'Товар',
                            'наименование номенклатуры',
                            'категория'
                        ],
                        'columns_name_db': [
                            'teko_id',
                            'category_id'
                        ],
                        'table_id': [
                            'teko_id'
                        ]
                    },  # ok
                    'targets': {
                        'column_date': [
                            'reporting_period'
                        ],
                        'column_int': [
                            'PosID',
                            'gi',
                            'upsale',
                            'insurance',
                            'eset',
                            'wink',
                            'promo',
                            'rtk',
                            'rtk_day',
                            'smartphones',
                            'fo_rtk',
                            'credit_lid'
                        ],
                        'percent_to_int': [
                            'mnp',
                            'credit',
                            'rtk_cr',
                            'vmr'
                        ],
                        'columns_name_csv': [
                            'target_id',
                            'PosID',
                            'gi',
                            'focus_tariffs',
                            'mnp',
                            'upsale',
                            'insurance',
                            'eset',
                            'wink',
                            'promo',
                            'rtk',
                            'rtk_lid',
                            'rtk_cr',
                            'rtk_day',
                            'smartphones',
                            'fo_rtk',
                            'credit',
                            'credit_lid',
                            'vmr',
                            'reporting_period'
                        ],
                        'columns_name_db': [
                            'target_id',
                            'posid',
                            'gi',
                            'focus_tariffs',
                            'mnp',
                            'upsale',
                            'insurance',
                            'eset',
                            'wink',
                            'promo',
                            'rtk',
                            'rtk_lid',
                            'rtk_cr',
                            'rtk_day',
                            'smartphones',
                            'fo_rtk',
                            'credit',
                            'credit_lid',
                            'vmr',
                            'reporting_period'
                        ],
                        'table_id': [
                            'target_id'
                        ]
                    },  # ok
                    'activations': {
                        'column_date': [
                            'ACTIVATION_DATE'
                        ],
                        'column_int': [
                            'FIRST_PAY',
                            'POS_ID'
                        ],
                        'columns_name_csv': [
                            'MSISDN',
                            'ACTIVATION_DATE',
                            'ICC',
                            'TRPL_NAME_ETIME',
                            'POS_ID',
                            'SEGMENT_NAME',
                            'FIRST_PAY',
                            'METHOD_REG_SIM'
                        ],
                        'columns_name_db': [
                            'number',
                            'datesale',
                            'activations_id',
                            'tariff',
                            'posid',
                            'segment',
                            'first_pay',
                            'channel'
                        ],
                        'table_id': [
                            'activations_id'
                        ]
                    },  # ok
                    'rtk_ao': {
                        'column_date': [
                            'datesale'
                        ],
                        'column_int': [
                            'pos_id',
                            'fact'
                        ],
                        'columns_name_csv': [
                            'pos_id',
                            'nomenclature',
                            'number',
                            'quality',
                            'fact',
                            'datesale'

                        ],
                        'columns_name_db': [
                            'posid',
                            'nomenclature',
                            'ao_id',
                            'quality',
                            'fact',
                            'datesale'
                        ],
                        'table_id': [
                            'ao_id'
                        ]
                    },  # ok
                    'di_applications': {
                        'column_date': [
                            'date_order',
                            'date_status'
                        ],
                        'column_int': [
                            'pos_id'
                        ],
                        'percent_to_int': [],
                        'columns_name_csv': [
                            'date_order',
                            'orderid',
                            'pos_id',
                            'msisdn',
                            'status',
                            'reason',
                            'comment',
                            'date_status'
                        ],
                        'columns_name_db': [
                            'datesale',
                            'orderid',
                            'posid',
                            'number',
                            'status',
                            'reason',
                            'comment',
                            'date_status'
                        ],
                        'table_id': [
                            'orderid'
                        ]
                    },  # ok
                    'di_successful': {
                        'column_date': [
                            'date_order',
                            'date_activation'
                        ],
                        'column_int': [
                            'pos_id'
                        ],
                        'percent_to_int': [],
                        'columns_name_csv': [
                            'date_order',
                            'orderid',
                            'pos_id',
                            'msisdn',
                            'sales_sim',
                            'date_activation'
                        ],
                        'columns_name_db': [
                            'datesale',
                            'orderid',
                            'posid',
                            'number',
                            'upsale',
                            'date_activation'
                        ],
                        'table_id': [
                            'orderid'
                        ]
                    },  # ok
                    'crediting': {
                        'column_date': [
                            'Время отправки заявки на рассмотрение'
                        ],
                        'column_int': [
                            'PosId ТТ'
                        ],
                        'percent_to_int': [
                            'Процентная ставка',
                            'Сумма товара',
                            'Сумма кредита'
                        ],
                        'columns_name_csv': [
                            'Номер заявки',
                            'PosId ТТ',
                            'ФИО продавца',
                            'ФИО клиента',
                            'Сумма товара',
                            'Сумма кредита',
                            'Время отправки заявки на рассмотрение',
                            'Банк',
                            'Окончательный статус заявки',
                            'Одобрения по любому банку',
                            'Акции по всем банкам',
                            'Процентная ставка',
                            'Тип оформления заявки'
                        ],
                        'columns_name_db': [
                            'crediting_id',
                            'posid',
                            'login',
                            'name_client',
                            'sum_sale',
                            'sum_credit',
                            'date_credit',
                            'bank',
                            'status',
                            'approved',
                            'bank_details',
                            'percent',
                            'application_type'
                        ],
                        'table_id': [
                            'crediting_id'
                        ],
                        'separations': [
                            'Акции по всем банкам'
                        ]
                    },  # ok
                    'vmr': {
                        'column_date': [
                            'date_report',
                            'Комментарий: Дата консультации'
                        ],
                        'column_int': [
                            'Номер Локации',
                            'ID анкеты'
                        ],
                        'percent_to_int': [
                            'Решение вопроса Всего',
                            'ПРОДВИЖЕНИЕ ДОПОЛНИТЕЛЬНОЙ ПРОДАЖИ Всего',
                            'ПРОДВИЖЕНИЕ УСЛУГ ФИКСИРОВАННОЙ СВЯЗИ И АО РОСТЕЛЕКОМ Всего',
                            'Всего'
                        ],
                        'columns_name_csv': [
                            'Номер Локации',
                            'date_report',
                            'Логин продавца',
                            'Сценарий',
                            'Комментарий: Дата консультации',
                            'Решение вопроса Всего',
                            'ПРОДВИЖЕНИЕ ДОПОЛНИТЕЛЬНОЙ ПРОДАЖИ Всего',
                            'ПРОДВИЖЕНИЕ УСЛУГ ФИКСИРОВАННОЙ СВЯЗИ И АО РОСТЕЛЕКОМ Всего',
                            '18. Как решался запрос клиента',
                            'Всего',
                            'ID анкеты'
                        ],
                        'columns_name_db': [
                            'posid',
                            'date_report',
                            'login',
                            'request',
                            'date_visit',
                            'core_request',
                            'upsale',
                            'rtk',
                            'pay',
                            'total',
                            'vmr_id'
                        ],
                        'table_id': [
                            'vmr_id'
                        ]
                    },  # ok
                    'traffic': {
                        'column_date': [
                        ],
                        'column_int': [
                            'Код ТТ',
                            'VALUE'
                        ],
                        'columns_name_csv': [
                            'Код ТТ',
                            'DATE',
                            'VALUE'
                        ],
                        'columns_name_db': [
                            'posid',
                            'traffic_date',
                            'traffic'
                        ],
                        'table_id': [
                            'posid'
                        ]
                    },  # ok
                    'mnp_successful': {
                        'column_date': [
                            'DATE'
                        ],
                        'column_int': [
                            'Код ТТ',
                            'VALUE'
                        ],
                        'columns_name_csv': [
                            'Код ТТ',
                            'DATE',
                            'VALUE'
                        ],
                        'columns_name_db': [
                            'posid',
                            'mnp_date',
                            'portations'
                        ],
                        'table_id': [
                            'mnp_date'
                        ]
                    },  # ok
                    'mnp_applications': {
                        'column_date': [
                            'DATE'
                        ],
                        'column_int': [
                            'Код ТТ',
                            'VALUE'
                        ],
                        'columns_name_csv': [
                            'Код ТТ',
                            'DATE',
                            'VALUE'
                        ],
                        'columns_name_db': [
                            'posid',
                            'applications_date',
                            'applications'
                        ],
                        'table_id': [
                            'applications_date'
                        ]
                    },  # ok
                    'photo_report': {
                        'column_date': [
                            'date_report'
                        ],
                        'percent_to_int': [
                            'result'
                        ],
                        'columns_name_csv': [
                            'report_id',
                            'posid',
                            'result',
                            'date_report'
                        ],
                        'columns_name_db': [
                            'report_id',
                            'posid',
                            'result',
                            'date_report'
                        ],
                        'table_id': [
                            'report_id'
                        ]
                    },  # ok
                    'service_errors': {
                        'column_date': [
                            'date_report'
                        ],
                        'column_int': [
                        ],
                        'columns_name_csv': [
                            'posid',
                            'result',
                            'date_report',
                            'errors_id'
                        ],
                        'columns_name_db': [
                            'posid',
                            'result',
                            'date_report',
                            'errors_id'
                        ],
                        'table_id': [
                            'errors_id'
                        ]
                    },  # ok
                    'smartphones': {
                        'column_date': [
                            'Номер чека'
                        ],
                        'column_int': [
                            'Сумма'
                        ],
                        'columns_name_csv': [
                            'Ссылка.Склад',
                            'Номер чека',
                            'Номенклатура',
                            'IMEI',
                            'Сумма'

                        ],
                        'columns_name_db': [
                            'address',
                            'datesale',
                            'model',
                            'imei',
                            'sumsale'
                        ],
                        'table_id': [
                            'imei'
                        ],
                        'address_id': [
                            'Ссылка.Склад'
                        ]
                    },  # ok
                    'product_sales': {
                        'column_date': [
                            'Номер чека'
                        ],
                        'column_int': [
                            'Сумма'
                        ],
                        'columns_name_csv': [
                            'Ссылка.Склад',
                            'Номер чека',
                            'Номенклатура',
                            'Сумма'

                        ],
                        'columns_name_db': [
                            'address',
                            'datesale',
                            'model',
                            'sumsale'
                        ],
                        'table_id': [
                            'imei'
                        ],
                        'address_id': [
                            'Ссылка.Склад'
                        ]
                    }  # ok
                    }

CURRENT_PK_INT: list[int] = [
    1004153,
    880470,
    782234,
    895117,
    874213,
    1001792,
    883662,
    876016,
    993806,
    790421,
    782321,
    782273,
    782371,
    1001160,
    1000877,
    775853,
    879336,
    997967,
    782302,
    788184,
    837324,
    1017607,
    927793,
    1055072,
    1056466,
    821532,
    869963,
    870452,
    971332,
    957312,
    958052,
    993810,
    842342,
    888967,
    964042,
    1014973,
    790426,
    1007369,
    848688,
    1086736,
    782260,
    1111667,
    1004332,
    1069135,
    935006,
    889614,
    782305,
    782304,
    892478,
    782267,
    833870,
    1067189,
    1067191,
    957673,
    759116,
    759073,
    759121,
    771430,
    821537,
    929703,
    932025,
    914884,
    993209,
    998514,
    759052,
    759099,
    1067192,
    891921,
    759051,
    929113,
    759100,
    793923,
    959163,
    71811,
    443,
    730687,
    988482,
    50835,
    1044869,
    101113,
    830396,
    1082621,
    446,
    777309,
    77749,
    1004105,
    75772,
    970707,
    965431,
    96165,
    881997,
    101219,
    50302,
    874040,
    68454,
    79089,
    890462
]  # список актульных PK формата int для проверки
CURRENT_PK_STR: list[str] = [
    'г.Москва, Щелковское шоссе, 75 (ТРЦ Щелковский) *Теле2*',
    'г.Москва, Измайловский вал,2 *Теле2*',
    'МО, Серпухов, Борисовское ш.,17 (ТЦ Слава) *Теле2*',
    'г.Москва, Щербинка, Пушкинская,2 *Теле2*',
    'МО, Воскресенск, Советская,15/11 *Теле2*',
    'МО, Домодедово, Корнеева,1 *Теле2*',
    'г.Москва, Хабаровская,15 (ТЦ Манго) *Теле2*',
    'г.Москва, Рязановское пос., Симферопольское шоссе,20а, стр.1 (ТЦ Карусель) *Теле2*',
    'г.Москва, Щербинка, Железнодорожная,44 *Теле2*',
    'г.Москва, Волжский б-р,113а, стр.1 (ТЦ Волжский) *Теле2*',
    'г.Москва, Щелковское шоссе,100 (ТЦ Щелково) *Теле2*',
    'г.Москва, Новоясеневский пр-т,2 *Теле2*',
    'МО, Протвино, Ленина,22 (ТЦ Слава) *Теле2*',
    'г.Москва, Московский, Никитина,2 (ТЦ Столица) *Теле2*',
    'г.Москва, Боровское шоссе,27 *Теле2*',
    'г.Москва, Борисовские пруды,26 к.2 *Теле2*',
    'МО, Раменское, Молодежная,20 (ТЦ Атак) *Теле2*',
    'МО, Рошаль, Советская,25 *Теле2*',
    'МО, Шатура, Ильича пр-т,40 *Теле2*',
    'г.Москва, Сормовская,6 (ТЦ ДА) *Теле2*',
    'МО, Люберцы, Томилино, Егорьевское ш.,2 *Теле2*',
    'МО, Королёв, Космонавтов пр-т,20а *Теле2*',
    'МО, Электросталь, Мира,29 *Теле2*',
    'г.Москва, Владимирская 2-я,36 *Теле2*',
    'г.Москва, Бутырская,2/18 *Теле2*',
    'МО, Люберцы, Октябрьский пр-т,366 (ТЦ Орбита) *Теле2*',
    'МО, Люберцы, Октябрьский пр-т,112 (ТЦ Выходной) *Теле2*',
    'г.Москва, Большая Серпуховская,17 *Теле2*',
    'г.Москва, Уральская,1 *Теле2*',
    'г.Москва, Менжинского,32 (ТЦ Кондор) *Теле2*',
    'г.Москва, Шереметьевская,6 к.1 *Теле2*',
    'г.Москва, Чертановская,20 стр.3 *Теле2*',
    'г.Москва, Алтуфьевское,88 *Теле2*',
    'МО, Королёв, Калинина,2 *Теле2*',
    'МО, Куровское, Вокзальная,14 *Теле2*',
    'МО, Балашиха, Энтузиастов ш.,11 с.4 *Теле2* (ТЦ Новоизмайловский)',
    'МО, Балашиха, Фадеева,3 *Теле2*',
    'г.Москва, Шоссе Энтузиастов,12 к.2 (ТЦ Город-2) *Теле2*',
    'г.Москва, Шоссе Энтузиастов,12 к.2 (ТЦ Город-1) *Теле2*',
    'г.Москва, Новослободская,10 с.1 *Теле2*',
    'г.Москва, Открытое шоссе, вл.9 (ТЦ Подсолнухи) *Теле2*',
    'г.Москва, Мира,114б стр.2 *Теле2*',
    'г.Москва, Останкинская 1-я,55 *Теле2*',
    'МО, Реутов, Октября,10 (ТЦ Экватор) *Теле2*',
    'МО, Балашиха, Свердлова,2а *Теле2*',
    'г.Москва, Первомайская,42 *Теле2*',
    'г.Москва, Новокосинская,31/4 *Теле2*',
    'МО, Реутов, Ленина,1а (ТЦ Карат) *Теле2*',
    'г.Москва, Рязанский пр-т,2/2 (ТК Город) *Теле2*',
    'г.Москва, Крутицкий 3-й пер,18 *Теле2*',
    'Ишим, Ленина,47 *Теле2* (ПФ)',
    'Тюмень, Ленина,61 *Теле2* (ПФ)',
    'Тюмень, Широтная,112б *Теле2* (ПФ)',
    'Абатское, Ленина,55б *Теле2* (ПФ)',
    'Вагай, Ленина,16а *Теле2* (ПФ)',
    'Голышманово, Ленина,11 *Теле2* (ПФ)',
    'Заводоуковск, Первомайская,9 *Теле2* (ПФ)',
    'Ишим, Маркса,35 *Теле2* (ПФ)',
    'Ишим, Маркса,80 *Теле2* (ПФ)',
    'Казанское, Луначарского,24а *Теле2* (ПФ)',
    'Омутинское, Шоссейная,50 *Теле2* (ПФ)',
    'Тобольск, 7 мкр,30 (ТРЦ Жемчужина Сибири) *Теле2* (ПФ)',
    'Тобольск, 8 мкр,6г *Теле2* (ПФ)',
    'Тюмень, Алебашевская,19 (ТЦ Зеленый Берег) *Теле2* (ПФ)',
    'Тюмень, Герцена,97 (ТЦ Галацентр) *Теле2* (ПФ)',
    'Тюмень, Менделеева,1 (ТРЦ Кристалл) *Теле2* (ПФ)',
    'Тюмень, Пермякова,50б (ТРЦ Солнечный) *Теле2* (ПФ)',
    'Тюмень, Республики,171/5 *Теле2* (ПФ)',
    'Тюмень, Республики,200а (ТРЦ Малахит) *Теле2* (ПФ)',
    'Тюмень, Ямская,118 *Теле2* (ПФ)',
    'Ярково, Пионерская,83 *Теле2* (ПФ)',
    'Интернац.,43 (ТЦ Омский) *Теле2* (ВИ)',
    'Авиагородок,38 *Теле2* (ВИ)',
    'Челюскинцев 4-я,119 *Теле2* (ВИ)',
    'Лобкова,3 *Теле2* (ВИ)',
    'Архитекторов_б.,35(Мега) *Теле2* (ВИ)',
    'Маркса,10 *Теле2* (ВИ)',
    'Заозерная,24а *Теле2* (ВИ)',
    'Октября 10 Лет,175 *Теле2* (ВИ)',
    'Гашека,9/1 *Теле2* (ВИ)',
    'Культуры,7 *Теле2* (ВИ)',
    'Кр.путь,127/1 *Теле2* (ВИ)',
    'Бархатовой,4 *Теле2* (ВИ)',
    'Серова,19а *Теле2* (ВИ)',
    'Космический,52 *Теле2* (ВИ)',
    'Лицкевича,1 *Теле2* (ВИ)',
    'Тюкалинск1 *Теле2* (ВИ)',
    'Исилькуль1 *Теле2* (ВИ)',
    'Азово2 *Теле2* (ВИ)',
    'Нижняя Омка4 *Теле2* (ВИ)',
    'Одесское1 *Теле2* (ВИ)',
    'Горьковское2 *Теле2* (ВИ)',
    'Нововаршавка1 *Теле2* (ВИ)',
    'Полтавка1 *Теле2* (ВИ)',
    'Саргатское2 *Теле2* (ВИ)',
    'Калачинск1 *Теле2* (ВИ)',
    'Черлак4 *Теле2* (ВИ)'
]  # список актульных PK формата str для проверки
COLUMNS_NAME_POSID_IN_CSV: list[str] = [
    'posid',
    'pos_id',
    'PosID',
    'PosId ТТ',
    'Код ТТ',
    'Номер Локации',
    'POS_ID',
    'POSID'
]  # название колонки с posid в csv
CSV_CONVERSION_FROM_UNPIVOT: list[str] = [
    'mnp_successful',
    'traffic',
    'mnp_applications'
]  # название таблиц CSV формата pivot, для обработки в unpivot формат
