import telebot
# import mysql.connector
# import deep learning module

# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     passwd='',
#     database='data_satu')


# #cek akses database
# print(mydb)

#input ke SQL
api = '5181979829:AAEueTTI3--iCXqnS401FJ1vVaCizkR74M0'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def action_start(message):
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    bot.send_message(message.chat.id, 'Hi, apa kabar {} {}?'.format(first_name, last_name))
    print(message)

@bot.message_handler(commands=['id'])
def action_id(message):
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    id_telegram = message.chat.id
    bot.send_message(message.chat.id, '''
Hai, ini ID Telegram kamu
Nama = {} {} 
ID = {}
        '''.format(first_name,last_name, id_telegram))

@bot.message_handler(commands=['help'])
def action_help(message):
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    bot.send_message(message.chat.id, '''
Hi {} {}, ini list command yaa
/start -> Sapa Bot dulu Gan
/id -> Cek id Kamu
/help -> List Command Bot
/ask -> Bertanya
'''.format(first_name,last_name))

@bot.message_handler(commands=['ask'])
def action_ask(message):
    
    answer = {
    "1": "Jawaban 1 ayayayaya",
    "2": "Jawaban 2 iyiyiyiy",
    "3": "Jawaban 3 uwuwuwuwu",
    "4": "Jawaban 4 hohohohoh",
    "5": "Jawaban 5 lolololol",
    "6": "Jawaban 6 lalalalala"
    }

    texts = message.text.split(' ')
    question = texts[1:len(texts)]
    question_str = ' '
    question_str = question_str.join(question)
    id_ask = len(question)
    # ngerun modelnya berdasarkan question str
    # id_ask = model(question_str)
    bot.send_message(message.chat.id, answer[str(id_ask)])


print('bot start running')

# question = command.split(' ')

bot.polling()

    