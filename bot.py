import time
import requests
import random
import os
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv("TOKEN")

url = f"https://api.telegram.org/bot{bot_token}/"


def last_update(request):
    response = requests.get(request + 'getUpdates')
    response = response.json()
    results = response['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def get_message_text(update):
    message_text = update['message']['text']
    return message_text


def send_message(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def main():
    update_id = last_update(url)['update_id']
    while True:
        time.sleep(3)
        update = last_update(url)
        if update_id == update['update_id']:
            text = get_message_text(update).lower()
            chat_id = get_chat_id(update)

            if text in ['hi', 'hello', 'hey', 'привет']:
                send_message(chat_id, 'Салем! Черкани /help, чтобы увидеть, что я умею')
            elif text == 'csc31':
                send_message(chat_id, 'Python')
            elif text == 'python':
                send_message(chat_id, 'Версия 3.14 🐍')
            elif text == 'dice':
                _1 = random.randint(1, 6)
                _2 = random.randint(1, 6)
                send_message(chat_id, f'Ты выбросил {_1} и {_2}!\nИтого: {_1 + _2} 🎲')

            # Новая команда /help
            elif text == '/help':
                help_text = (
                    "🛠 *Доступные команды:*\n\n"
                    "/help — показать все команды\n"
                    "/mood — узнать моё настроение \n"
                    "/rest —  узнать как себя чувсвую \n"
                    "/advice — получить совет от бота ️\n"
                    "dice — бросить кости 🎲\n"
                )
                send_message(chat_id, help_text)

            elif text == '/mood':
                moods = [
                    "Дайте чашечку кофе.",
                    "Нормально. Перезагрузился, теперь снова живой.",
                    "Хочу спать.",
                    "В ударе! Как студент за 3 часа до дедлайна!",
                    " Сплю, не мешай... "
                ]
                send_message(chat_id, random.choice(moods))

            elif text == '/rest':
                rests = [
                    "Сегодня я не работаю, лень.",
                    "‍Не хочу работать. Подожди до завтра.",
                    " Ну сказал же, жди завтра :)"
                ]
                send_message(chat_id, random.choice(rests))

            elif text == '/advice':
                advices = [
                    "Не делай сегодня то, что можно отложить на после дедлайна",
                    "Если я работаю - не спрашивай как я работаю. Я сам не знаю",
                    "Сохраняй код,не забывай",
                    "Не пиши комментарии в коде. Пусть тот кто читает,страдает",
                    "Пей энергетики. Или кофе. Или оба сразу"
                ]
                send_message(chat_id, random.choice(advices))

            else:
                send_message(chat_id, 'Сорян, не пониманте. черкани /help для списка команд.')

            update_id += 1


if __name__ == '__main__':
    main()
