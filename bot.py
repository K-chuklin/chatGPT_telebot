from openai import OpenAI
import telebot
import config


# Укажите токен вашего бота и ключ API OpenAI
TOKEN = config.bot_token

# Создаем экземпляры бота и клиента OpenAI
bot = telebot.TeleBot(TOKEN)
client = OpenAI(api_key=config.api_key, base_url=config.url)


# Обработчик для команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id,
                     "Привет! Я бот, который общается с помощью нейросети. Попробуй отправить мне что-нибудь.")


# Обработчик для всех входящих сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Отправляем сообщение пользователя нейросети и получаем ответ
    ai_response = send_to_ai(message.text)
    # Отправляем ответ нейросети пользователю
    bot.send_message(message.chat.id, ai_response)


# Функция для отправки сообщения нейросети и получения ответа
def send_to_ai(user_input):
    messages = [{"role": "user", "content": user_input}]
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages
    )
    ai_response = chat_completion.choices[0].message.content
    return ai_response


# Запускаем бота
bot.polling()
