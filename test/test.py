import consul
import os

c = None
if os.environ.get('RUNNING_IN_DOCKER', False):
	c = consul.Consul("host.docker.internal")
else:
	c = consul.Consul()
print(c.catalog.nodes())
print(c.catalog.node('hazels'))
print(c.catalog.node('hazels')[1])
services = [c.catalog.node('hazels')[1]['Services']]
urls = [f"{i['Address']}:{i['Port']}" for i in services]
random.shuffle(urls)
print("connected to consul, urls are", urls)
