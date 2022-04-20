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
filename = 'model_nb.sav'
filename_vec = 'vectorizer.sav'
loaded_model = pickle.load(open(filename, 'rb'))
print("Model Loaded")
loaded_vec = pickle.load(open(filename_vec, 'rb'))
print("Vectorizer Loaded")

api = '5181979829:AAEueTTI3--iCXqnS401FJ1vVaCizkR74M0'
bot = telebot.TeleBot(api)

@bot.message_handler(commands=['start'])
def action_start(message):
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    bot.send_message(message.chat.id, '''
Hi apa kabar {} {}? <Nama bot yg bagus> siap menjawab pertanyaanmu mengenai Grave's Disease. 
Silahkan tanya mengenai informasi penyakit Grave's dengan menggunakan format \"/ask <pertanyaan>\"
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
/ask Apa itu Grave's Disease
'''.format(first_name,last_name))

@bot.message_handler(commands=['ask'])
def action_ask(message):
    
    # ganti akses db
    answer_sample = {
    "0": "Jawaban 0 ayayayaya",
    "1": "Jawaban 1 ayayayaya",
    "2": "Jawaban 2 iyiyiyiy",
    "3": "Jawaban 3 uwuwuwuwu",
    "4": "Jawaban 4 hohohohoh",
    "5": "Jawaban 5 lolololol",
    "6": "Jawaban 6 lalalalala"
}
    texts = message.text.split(' ')

    # Convert question
    question = texts[1:len(texts)]
    question_str = ' '
    question_str = question_str.join(question)

    # Predict answer based on question
    question_vec = loaded_vec.transform([question_str])
    pred = loaded_model.predict(question_vec)
    pred_category = float(pred[0])

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

    