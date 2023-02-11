from django.http import HttpRequest
import requests
import os
import random
def log_msg(msg):
	UUID = random.randint(0, 2**31)
	print("sending message", msg, 'UUID', UUID)
	url="http://127.0.0.1:7000/database/"
	try:
		result = requests.post(url, json={'UUID': UUID,'msg': msg})
		print("result", result)
	except Exception as e:
		print("error", e)
		SECRET_KEY = os.environ.get('RUNNING_IN_DOCKER', False)
		if SECRET_KEY:
			print("I am running in Docker container")
		print('maybe logger is running in Docker, trying again')
		url="http://host.docker.internal:7000/database/"
		try:
			result = requests.post(url, json={'UUID': UUID,'msg': msg})
			print("result", result)
		except Exception as e:
			print("error", e)
			return False
	print("successfully logged the message")
	return True

def get_msgs():
	print("getting messages")
	result = ""
	url="http://127.0.0.1:7000/database/"
	try:
		result = requests.get(url)
		print("result", result)
		result = result.text
	except Exception as e:
		print("error", e)
		SECRET_KEY = os.environ.get('RUNNING_IN_DOCKER', False)
		if SECRET_KEY:
			print("I am running in Docker container")
		print('maybe logger is running in Docker, trying again')
		url="http://host.docker.internal:7000/database/"
		try:
			result = requests.get(url)
			print("result", result)
			result = result.text
		except Exception as e:
			print("error", e)
			return "Error: couldn't get messages"
	return str(result)