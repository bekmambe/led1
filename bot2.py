
import telebot

bot = telebot.TeleBot("1484323762:AAEA88DTpig2MDpmZMf09Yszq45kEd9xPVk")

@bot.message_handler(commands=['start'])
def start(message):
    # the message is already modified when it reaches message handler
    message = "Салам Алейкум"

@bot.message_handler(content_types=['text'])

def send_echo(message):
    name = message.text
    result = "У техника " + message.text + "\n"
    
    pult = "Если оператор пульта 10000 р.\n"
    brig = " Если бригадир: Монтаж 5000 р. Дежурство 4500 р. Демонтаж 4000 р. Переработка 450 р/час Командировка 6500 р. \n Если помощник бригадира: Монтаж 3850 р. Дежурство 3300 р. Демонтаж 2750 р. Переработка 330 р/час Командировка 4950 р. \n"
    zambrig = "Монтаж 3850 р. Дежурство 3300 р. Демонтаж 2750 р. Переработка 330 р/час Командировка 4950 р. \n"
    tech1 = " Монтаж 3300 р. Дежурство 2750 р. Демонтаж 2200 р. Переработка 275 р/час Командировка 4125 \n "
    tech2 = " Монтаж 2750 р. Дежурство 2200 р. Демонтаж 1650 р. Переработка 220 р/час Командировка 3300 \n "
    
    if name == "Агапов":
        result = brig + pult
    elif name == "агапов":
        result = brig + pult
    elif name == "Аскеров":
        result = tech1
    elif name == "аскеров":
        result = tech1
    elif name == "Богиня":
        result = brig
    elif name == "богиня":
        result = brig
    elif name == "Волков":
        result = brig
    elif name == "волков":
        result = brig
    elif name == "Гремин":
        result = tech2
    elif name == "гремин":
        result = tech2
    elif name == "Гусев":
        result = zambrig + pult
    elif name == "гусев":
        result = zambrig + pult
    elif name == "Дьяченко":
        result = brig
    elif name == "дьяченко":
        result = brig
    elif name == "Дьяченко К":
        result = brig
    elif name == "дьяченко к":
        result = brig
    elif name == "Дьяченко К.":
        result = brig
    elif name == "дьяченко к.":
        result = brig
    elif name == "Дьяченко Константин":
        result = brig
    elif name == "дьяченко константин":
        result = brig
    elif name == "Дьяченко Л":
        result = tech2
    elif name == "дьяченко Л":
        result = tech2
    elif name == "Дьяченко Л.":
        result = tech2
    elif name == "дьяченко л.":
        result = tech2
    elif name == "дьяченко л":
        result = tech2
    elif name == "Дьяченко Леонид":
        result = tech2
    elif name == "дьяченко Леонид":
        result = tech2
    elif name == "Дьяченко леонид":
        result = tech2
    elif name == "дьяченко леонид":
        result = tech2
    elif name == "Задоркин":
        result = tech2
    elif name == "задоркин":
        result = tech2
    elif name == "Космачев":
        result = zambrig
    elif name == "космачев":
        result = zambrig
    elif name == "Куверин":
        result = tech2
    elif name == "куверин":
        result = tech2
    elif name == "Каменский":
        result = tech1
    elif name == "каменский":
        result = tech1
    elif name == "Кривошеин":
        result = "Монтаж 5000 р. Дежурство 4500 р. Демонтаж 4000 р. Переработка 450 р/час Командировка 6500 р. \n"
    elif name == "кривошеин":
        result = "Монтаж 5000 р. Дежурство 4500 р. Демонтаж 4000 р. Переработка 450 р/час Командировка 6500 р. \n"
    elif name == "Кузнецов":
        result = zambrig
    elif name == "кузнецов":
        result = zambrig
    elif name == "Маслов":
        result = brig
    elif name == "маслов":
        result = brig
    elif name == "Можайский":
        result = brig
    elif name == "Мж":
        result = brig
    elif name == "МЖ":
        result = brig
    elif name == "мж":
        result = brig
    elif name == "можайский":
        result = brig
    elif name == "Нестеров":
        result = zambrig
    elif name == "нестеров":
        result = zambrig
    elif name == "Парфеев":
        result = brig + pult
    elif name == "парфеев":
        result = brig + pult
    elif name == "Петров":
        result = tech1
    elif name == "петров":
        result = tech1
    elif name == "Семенов":
        result = tech1
    elif name == "семенов":
        result = tech1
    elif name == "Трошин":
        result = tech2
    elif name == "трошин":
        result = tech2
    elif name == "Кузьмин":
        result = tech2
    elif name == "кузьмин":
        result = tech2
    elif name == "Шкодкин":
        result = tech1
    elif name == "шкодкин":
        result = tech1
    elif name == "Куценков":
        result = "Это наш Светочь - главный босс. Получает точно побольше тебя \n"
    elif name == "куценков":
        result = "Это наш Светочь - главный босс. Получает точно побольше тебя \n"
    elif name == "Ларикова":
        result = "Это наша Королева! ты - пыль под копытами ее собак \n"
    elif name == "ларикова":
        result = "ты как посмел это Имя с маленькой буквы написать, щенок? \n"
    elif name == "Томашек":
        result = "зачем тебе это знать? \n"
    elif name == "томашек":
        result = "зачем тебе это знать? \n"
    
        
    else:
        result = "про такого еще не знаю. или уже? \n"
        
    bot.send_message(message.chat.id, result)

bot.polling( none_stop = True )