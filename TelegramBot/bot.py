from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

OPEN_WEATHER_API_KEY = '8bfd07dd010c0f6be8eaa572698a531e'

def get_weather_json(city):
    contents = requests.get('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=' + OPEN_WEATHER_API_KEY).json()
    return contents
    
def get_weather(weather_json):
    weather=weather_json['weather'][0]['main']
    return weather
    
def get_temperature(weather_json):
    temperature=weather_json['main']['temp']
    return temperature


def help(bot, update):
    bot.message.reply_text('You can control me by sending these commands:\n\n/weather {City} - find out the weather and temperature in the selected city\n/help - command list')

def weather(bot, update):
    city = bot.message.text[9:]
    weather_json = get_weather_json(city)

    weather=get_weather(weather_json)
    temperature=get_temperature(weather_json)

    bot.message.reply_text('Weather: ' + weather)
    bot.message.reply_text('Temperature: ' + str(temperature) + "°C")
    

def main():
    updater = Updater('2051859870:AAEkvvl1TVSYAfpkcUaBxHk--9rUfr0RSmI', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('weather',weather))
    dp.add_handler(CommandHandler('help',help))
    dp.add_handler(CommandHandler('start',help))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
