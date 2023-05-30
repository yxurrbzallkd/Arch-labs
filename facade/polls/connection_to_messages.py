from django.http import HttpRequest
import requests
import os
import random
import consul

def messages_get_all():
	c = None
	if os.environ.get('RUNNING_IN_DOCKER', False):
		c = consul.Consul("host.docker.internal")
	else:
		c = consul.Consul()
	services = list(c.catalog.node('messages')[1]['Services'].values())
	urls = [f"http://{i['Address']}:{i['Port']}" for i in services]
	print("connected to consul, urls are", urls)
	result = dict()
	for url in urls:
		print("trying", url)
		try:
			r = requests.get(url)
			print("result", result)
			r = r.text
			result[url] = r
		except Exception as e:
			print("url", url, "error", e)
	return result

def messages_get():
	c = None
	if os.environ.get('RUNNING_IN_DOCKER', False):
		c = consul.Consul("host.docker.internal")
	else:
		c = consul.Consul()
	services = list(c.catalog.node('messages')[1]['Services'].values())
	urls = [f"http://{i['Address']}:{i['Port']}" for i in services]
	random.shuffle(urls)
	result = ""
	for url in urls:
		print("trying", url)
		try:
			result = requests.get(url)
			print("result", result)
			result = result.text
			break
		except Exception as e:
			print("url", url, "error", e)
	return result

