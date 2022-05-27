import telebot
import pymongo
import pickle
import joblib
from pprint import pprint

# Connect to mongoDB
MONGODB_URI = "mongodb+srv://holly:if5172@tiroidcluster.qzzri.mongodb.net/tiroidDB?retryWrites=true&w=majority"
client = pymongo.MongoClient(MONGODB_URI) 
db = client['tiroidDB']
print("Database loaded")
answers = db['answers']

# load the model from disk
filename_mod = 'joblib-latest-multinom-nb.pkl'
loaded_model = joblib.load(open(filename_mod, 'rb'))
print("Model Loaded")

api = '5181979829:AAEueTTI3--iCXqnS401FJ1vVaCizkR74M0'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def action_start(message):
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    bot.send_message(message.chat.id, '''
Hi apa kabar {} {}? Tiroid Help Bot siap menjawab pertanyaanmu mengenai Graves Disease. 
Silahkan tanya mengenai informasi penyakit Graves dengan menggunakan format \"/ask <pertanyaan>\"
'''.format(first_name, last_name))

    print(message)

@bot.message_handler(commands=['id'])
def action_id(message):
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    id_telegram = message.chat.id
    bot.send_message(message.chat.id, '''
ID Telegram = {}
        '''.format(id_telegram))

@bot.message_handler(commands=['help'])
def action_help(message):
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    bot.send_message(message.chat.id, '''
Halo {} {} 👋
Berikut adalah list command yang dapat dilakukan
/start → Mulai menggunakan Bot
/help → Melihat kembali list command Bot
/ask → Ketik langsung pertanyaan dengan memisahkan /ask dan pertanyaan dengan spasi

Contoh: 
/ask Apa itu Graves Disease
'''.format(first_name,last_name))

@bot.message_handler(commands=['ask'])
def action_ask(message):
    
    texts = message.text.split(' ')

    # Convert question
    question = texts[1:len(texts)]
    question_str = ' '
    question_str = question_str.join(question)

    # Predict answer based on question
    pred = loaded_model.predict([question_str])
    pred_category = int(pred[0]*100)
    
    # Access DB to get answer string based on category
    answers_str = answers.find_one({'category': pred_category})['answer']
    answers_images = answers.find_one({'category': pred_category})['images']
    
    # Send answer strings
    for ans in answers_str:
        bot.send_message(message.chat.id, ans)
    # Send answer images
    for image_url in answers_images:
        bot.send_photo(message.chat.id, image_url)

print('tiroidbot start running')

bot.polling()

    