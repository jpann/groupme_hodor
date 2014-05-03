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

@app.route('/', methods=['POST'])
def message():
	if not request.json or not 'text' in request.json:
		return
	
	user_id = request.json['user_id']
	nick = request.json['name']
	message = request.json['text']
	message = stripped(message)

	return 'Hello world!'
