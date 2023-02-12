import telebot
from telebot import types

bot = telebot.TeleBot("TOKEN")

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('/start') 
itembtn2 = types.KeyboardButton('/question')
markup.add(itembtn1, itembtn2)

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.reply_to(message,f"Здравствуйте, {message.from_user.first_name}! Я бот техподдержки. Нажмите '/question', чтобы задать свой вопрос",reply_markup=markup)

@bot.message_handler(commands=['question'])
def correction(message):
    bot.reply_to(message,"Задайте свой вопрос одним сообщением, я передам его оператору",reply_markup=markup)
    bot.register_next_step_handler(message,write_question)
        
def write_question(message):
    data = open('question.txt','a',encoding='utf8')
    data.write(f'{message.from_user.id} || {message.from_user.first_name} {message.from_user.last_name}: {message.text}\n')
    data.close()
    bot.reply_to(message,"Среднее время ожидания ответа 1 час.")


@bot.message_handler(content_types=['text'])
def echo_all(message):
    text = message.text.lower()
    if 'спасибо' in text:
        bot.reply_to(message,f"Ждем Вас снова, {message.from_user.first_name}")
        
bot.polling(none_stop=True)
