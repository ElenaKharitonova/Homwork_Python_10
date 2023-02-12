import telebot

def send_answer(id,question,answer):
    bot.send_message(id,f"{question}\nОтвет:{answer}")

bot = telebot.TeleBot("TOKEN")

data = open('question.txt','r',encoding='utf8')
questions_list = data.readlines()
data.close()

answered_question = []
for row in questions_list:
    split_row = row.split(' || ')
    id = split_row[0]
    question = split_row[1]
    print(question[:-1])
    answer = input("Если хотите пропустить вопрос, напишите 'пропустить', если нет введите ответ: ")
    if answer != 'пропустить':
        send_answer(id,question,answer)
        answered_question.append(row)
        print('___________________________')
        
for answer in answered_question:
    questions_list.remove(answer)  
    data = open('question.txt','w',encoding='utf8')
    data.writelines(questions_list)
    data.close()
