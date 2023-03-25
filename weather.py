import json
import telebot
import requests
from telebot import types

bot = telebot.TeleBot('')#токен Telegram
API = ''#openweathermap API

@bot.message_handler(commands=['start'])#обработчик команды start
def start(message):
    bot.send_message(message.chat.id, 'Введите название города')

@bot.message_handler(content_types=['text'])#обработчик введенного текста
def get_weather(message):
    city = message.text.strip().lower()#получает значение введенное пользователем и записывает его в переменную
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')#получать температуру в цельсиях
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')
    else:
        bot.reply_to(message, f'Город указан не верно')

bot.polling(none_stop=True)