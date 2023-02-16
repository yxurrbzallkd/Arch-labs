from django.http import HttpRequest
import requests
import os
import random

messager_port_ids=list(range(1,3))

def messages_get():
	print(messager_port_ids)
	random.shuffle(messager_port_ids)
	result = ""
	for i in messager_port_ids:
		port = i+5000
		url = f"http://127.0.0.1:{port}/messages/"
		RUNNING_IN_DOCKER = os.environ.get('RUNNING_IN_DOCKER', False)
		if RUNNING_IN_DOCKER:
			print("I am running in Docker container")
			url = f"http://host.docker.internal:{port}/messages/"
		print("trying", url)
		try:
			result = requests.get(url)
			print("result", result)
			result = result.text
			break
		except Exception as e:
			print("error", e)
	return result

