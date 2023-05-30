from django.http import HttpRequest
import requests
import os
import random
import consul


def log_msg(msg):
	c = None
	if os.environ.get('RUNNING_IN_DOCKER', False):
		c = consul.Consul("host.docker.internal")
	else:
		c = consul.Consul()
	services = list(c.catalog.node('loggers')[1]['Services'].values())
	urls = [f"http://{i['Address']}:{i['Port']}" for i in services]
	random.shuffle(urls)
	print("connected to consul, logger urls are", urls)
	UUID = random.randint(0, 2**31)
	success = False
	print("sending message", msg, 'UUID', UUID)
	for url in urls:
		print("trying", url)
		try:
			result = requests.post(url, json={'UUID': UUID,'msg': msg})
			print("result", result)
			success = True
			print("successfully logged the message")
			break
		except Exception as e:
			print("url", url, "error", e)
	return success

def get_msgs():
	c = None
	if os.environ.get('RUNNING_IN_DOCKER', False):
		c = consul.Consul("host.docker.internal")
	else:
		c = consul.Consul()
	services = list(c.catalog.node('loggers')[1]['Services'].values())
	urls = [f"http://{i['Address']}:{i['Port']}" for i in services]
	random.shuffle(urls)
	for url in urls:
		print("trying", url)
		try:
			result = requests.get(url, timeout=10)
			print("result", result)
			result = result.text
			success = True
			break
		except Exception as e:
			print("url", url, "error", e)
	return str(result)