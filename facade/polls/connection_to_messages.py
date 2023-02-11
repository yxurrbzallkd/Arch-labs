from django.http import HttpRequest
import requests
import os
import random
def messages_get():
	result = ""
	url="http://127.0.0.1:5000/messages"
	try:
		result = requests.get(url)
		print("result", result)
		result = result.text
	except Exception as e:
		print("error", e)
		SECRET_KEY = os.environ.get('RUNNING_IN_DOCKER', False)
		if SECRET_KEY:
			print("I am running in Docker container")
		print('maybe messages is running in Docker, trying again')
		url="http://host.docker.internal:5000/messages"
		try:
			result = requests.get(url)
			print("result", result)
			result = result.text
		except Exception as e:
			print("error", e)
			result = "Failed to connect to messages...."
	return result

