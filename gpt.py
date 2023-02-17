import telebot
import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY', '')
bot = telebot.TeleBot(os.getenv('BOT_TOKEN', ''))

def openai_api(message):
	response = openai.Completion.create(
            model='text-davinci-003',
            prompt=message.text,
            max_tokens=1000,
    )

	return response.choices[0]["text"]

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, 'Привіт, я ChatGPT')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.send_message(message.chat.id, 'Трохи зачекайте...')
	gpt = openai_api(message)
	bot.reply_to(message, gpt)

bot.infinity_polling()
