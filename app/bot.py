from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import json


# Training file path
TRAINER_FILEPATH = "./app/trainer.json"


class ENGSM:
    ISO_639_1 = 'en_core_web_sm'


try:
    chatbot = ChatBot("KrzBot", tagger_language=ENGSM)
except:
    from spacy.cli import download

    download("en_core_web_sm")
    chatbot = ChatBot("KrzBot", tagger_language=ENGSM)


# Load conversation list from training file
with open(TRAINER_FILEPATH, 'r', encoding='utf-8') as json_file:
    conversa = json.load(json_file)


trainer = ListTrainer(chatbot)
trainer.train(conversa)