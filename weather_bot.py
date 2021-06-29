import telebot
import config
# from selenium import webdriver
from bs4 import BeautifulSoup
import requests

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# driver = webdriver.Chrome(executable_path="drivers/chromedriver", chrome_options = options)
request = requests.get("https://ua.sinoptik.ua/погода-рівне")
html = BeautifulSoup(request.content, 'html.parser')
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def main(message):
    # URL = "https://ua.sinoptik.ua/погода-рівне"
    # driver.get(URL)
    # weather = driver.find_element_by_css_selector("div#blockDays")
    # min_temp = driver.find_element_by_css_selector(".temperature .min").text.strip().replace('\n',' ')
    # max_temp = driver.find_element_by_css_selector(".temperature .max").text.strip().replace('\n',' ')
    # desc = driver.find_element_by_css_selector(".wDescription .description").text.strip()
    min_temp = html.select_one('.temperature .min').text.strip()
    max_temp = html.select_one('.temperature .max').text.strip()
    desc = html.select_one('.wDescription .description').text.strip()

    print(f'{min_temp}\n{max_temp}\n{desc}')
    bot.send_message(message.chat.id, f'{min_temp}\n{max_temp}\n{desc}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Help message!')

bot.polling()
# driver.close()

