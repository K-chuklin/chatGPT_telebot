# Телеграмм бот с нейросетью
Этот телеграмм бот позволяет начать беседу с моделью GPT-3.5 от OpenAI прямо из вашего Telegram аккаунта, 
без необходимости использования VPN или других сложных настроек. 
Бот создан с использованием языка Python и библиотек telebot для работы с Telegram API и openai для взаимодействия с моделью GPT-3.5.

## Установка
Клонируйте репозиторий:
```
git clone github.com/K-chuklin/chatGPT_telebot
```
## Установите зависимости:
```
pip install -r requirements.txt
```
## Получите API ключи от Telegram Bot API и OpenAI. Запишите их в файле config.py:
```
bot_token = 'YOUR_TELEGRAM_BOT_TOKEN'
url = 'YOUR_OPENAI_URL'
api_key = 'YOUR_OPENAI_API_KEY'
```
## Запуск
Запустите бота с помощью команды:
```
python bot.py
```

## Cоздание Docker образа
(Для запуска на сервере)
Создайте Docker образ с помощью команды:
```
docker-compose build
```
Запустите созданный образ с помощью команды:
```
docker-compose up
```


Теперь ваш телеграмм бот готов к использованию!

## Использование
Просто начните беседу с вашим ботом в Telegram, отправив ему сообщение. 
Бот будет использовать модель GPT-3.5, чтобы предложить ответ на ваш запрос.



### Важно!
Этот бот создан исключительно в образовательных целях. Пожалуйста, не злоупотребляйте его функционалом и убедитесь, что он соответствует правилам использования Telegram API и OpenAI API.

### Автор
Автор: Chuklin Konstantin
GitHub: [Ваш профиль GitHub](https://github.com/K-chuklin)

