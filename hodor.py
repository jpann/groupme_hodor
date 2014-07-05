import os
from flask import Flask
from flask import request
import requests
import random
import codecs

app = Flask(__name__)

def replace_spc_handler(error):
	return (u' ' * (error.end-error.start), error.end)

def stripped(text):
	text = text.lower()
	return text.encode('ascii','replace_spc')

def get_random(min, max):
	return random.randint(min, max)

def send_message(text):
	bot_id = os.environ['BOT_ID']

	message = {
		'text' : text,
		'bot_id' : bot_id
	}

	r = requests.post("https://api.groupme.com/v3/bots/post", params = message)

def get_random_hodor():
	r = get_random(1, 10)

	if r == 1:
		return "Hodor"
	elif r == 2:
		return "HODOR"
	elif r == 3:
		return "Hoooodor"
	elif r == 4:
		return "Ho-dor"
	elif r == 5:
		return "Hodor Hodor Hodor"
	elif r == 6:
		return  "*Shakes* Hodor Hodor Hodor"
	elif r == 7:
		return "HODOR!!!!"
	elif r == 8:
		return "Hodor..."
	elif r == 9:
		return "Hooooooodoooooooooooooooor"
	elif r = 10:
		return "Hodor?"

@app.route('/', methods=['POST'])
def message():
	if not request.json or not 'text' in request.json:
		return
	
	user_id = request.json['user_id']
	nick = request.json['name'].lower()
	message = request.json['text'].lower()
	message = stripped(message).strip()
	
	if nick in os.environ['IGNORE_NAMES'].split('|'):
		return

	if os.environ['BOT_NAME'].lower() in message:
		send_message(get_random_hodor())
	
	if message.endswith("?"):
		if get_random(1, 1000) <= 10:
			send_message(get_random_hodor())
