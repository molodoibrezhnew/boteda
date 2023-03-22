import telegram
from telegram.ext import Updater, MessageHandler, Filters

# Список разрешенных продуктов
ALLOWED_PRODUCTS = {
    'овощи': [
        'брокколи', 'цветная капуста', 'шпинат', 'морковь', 'бобы',
        'горох', 'брюссельская капуста', 'редис', 'лук', 'чеснок',
        'томаты', 'баклажаны', 'перец сладкий', 'кабачки', 'огурцы',
        'шампиньоны', 'артишоки', 'шпинат', 'спаржа', 'сельдерей',
        'капуста', 'огурцы', 'гороховые стручки', 'грибы', 'зеленый горошек',
        'салат', 'кунжут', 'спаржевая фасоль', 'петрушка', 'укроп'
    ],
    'фрукты': [
        'яблоки', 'груши', 'апельсины', 'мандарины', 'бананы',
        'киви', 'авокадо', 'малина', 'черника', 'клубника', 'вишня',
        'ананас', 'манго', 'гранат', 'водяные дыни', 'папайя', 'черешня',
        'грейпфрут', 'лимоны', 'абрикосы', 'виноград', 'кокосы', 'инжир',
        'лимоны', 'лайм', 'персики', 'сливы', 'персиммон'
    ],
    'крупы и зерновые': [
        'гречка', 'овсянка', 'киноа', 'бурый рис',
        'цельнозерновые макароны', 'пшеничная крупа',
        'булгур', 'перловка', 'кукурузная крупа', 'амарант',
        'манная крупа', 'гречневая крупа', 'ячневая крупа', 'какао',
        'квиноа', 'крупа из топинамбура', 'рожь', 'ячмень'
    ],
    'белковые продукты': [
        'индейка', 'курица', 'рыба', 'морепродукты', 'тофу',
        'творог нежирный', 'греческий йогурт', 'яйца', 'креветки',
        'форель', 'горбуша', 'минтай', 'сельдь', 'скумбрия',
        'тунец
    ],
    'белковые продукты': [
        'индейка', 'курица', 'рыба', 'морепродукты', 'тофу',
        'творог нежирный', 'греческий йогурт', 'яйца',
        'говядина', 'баранина', 'кролик', 'индюшатина',
        'утка', 'гусятина', 'телятина', 'свинина', 'креветки', 'лангусты', 'крабы'
    ],
    'бобовые и орехи': [
        'чечевица', 'нут', 'фасоль', 'миндаль', 'грецкий орех', 'кедровые орехи', 'чиа-семена', 'льняные семена',
        'кунжут', 'арахис', 'фисташки', 'кешью', 'орехи макадамии', 'бразильские орехи', 'орехи пекан', 'фундук'
    ],
    'заменители сахара': [
        'стевия', 'эритрит', 'ксилит', 'маннит',
        'агава', 'мед', 'изомальт', 'ягодный сироп', 'сироп лука'
    ],
    'масла и жиры': [
        'оливковое масло', 'рапсовое масло',
        'авокадо масло', 'кокосовое масло',
        'семена льна', 'грецкий орех', 'миндаль', 'арахис', 'фисташки'
    ],
    'напитки': [
        'вода', 'зеленый чай', 'травяные чаи', 'черный кофе',
        'фреш из свежих овощей', 'смузи', 'теплое молоко с медом', 'теплый имбирный чай'
    ]
}


Функция для проверки, можно ли употреблять продукт

def is_allowed_food(food):
for key in ALLOWED_PRODUCTS:
if food.lower() in ALLOWED_PRODUCTS[key]:
return f'{food} можно употреблять при {key}'
return f'{food} нельзя употреблять'
Функция для обработки сообщений

def handle_message(update, context):
# Получаем текст сообщения
message_text = update.message.text
# Проверяем, можно ли употреблять продукт
result = is_allowed_food(message_text)
# Отправляем ответ пользователю
context.bot.send_message(chat_id=update.effective_chat.id, text=result)
Токен для доступа к Telegram API

TOKEN = 'YOUR_TOKEN_HERE'
Создаем объект Updater и передаем ему токен

updater = Updater(TOKEN, use_context=True)
Получаем диспетчер сообщений

dispatcher = updater.dispatcher
Создаем обработчик сообщений

message_handler = MessageHandler(Filters.text, handle_message)
Регистрируем обработчик в диспетчере

dispatcher.add_handler(message_handler)
Запускаем бота

updater.start_polling()
Ждем завершения работы бота

updater.idle()
