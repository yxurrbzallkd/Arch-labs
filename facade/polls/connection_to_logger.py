from django.http import HttpRequest
import requests
import os
import random

logger_port_ids=list(range(1,4))

def log_msg(msg):
	UUID = random.randint(0, 2**31)
	success = False
	print("sending message", msg, 'UUID', UUID)
	random.shuffle(logger_port_ids)
	for i in logger_port_ids:
		port = i+7000
		url = f"http://127.0.0.1:{port}/database/"
		RUNNING_IN_DOCKER = os.environ.get('RUNNING_IN_DOCKER', False)
		if RUNNING_IN_DOCKER:
			print("I am running in Docker container")
			url = f"http://host.docker.internal:{port}/database/"
		print("trying", url)
		try:
			result = requests.post(url, json={'UUID': UUID,'msg': msg})
			print("result", result)
			success = True
			print("successfully logged the message")
			break
		except Exception as e:
			print("port", port, "error", e)
	return success

def get_msgs():
	print("getting messages")
	result = ""
	random.shuffle(logger_port_ids)
	for i in logger_port_ids:
		port = i+7000
		url = f"http://127.0.0.1:{port}/database/"
		RUNNING_IN_DOCKER = os.environ.get('RUNNING_IN_DOCKER', False)
		if RUNNING_IN_DOCKER:
			print("I am running in Docker container")
			url = f"http://host.docker.internal:{port}/database/"
		print("trying", url)
		try:
			result = requests.get(url, timeout=10)
			print("result", result)
			result = result.text
			success = True
			break
		except Exception as e:
			print("port", port, "error", e)
	return str(result)