import os
import hazelcast
from .hazelcast_client import client

def log_msg(msg):
	print("received a message", msg['msg'])
	hazelcast_url = os.environ.get('HAZELCAST_URL', False)
	if not hazelcast_url:
		print("can't find hazelcast - no url provided")
		return False
	storage = client.get_map("messages")
	storage.put(msg['UUID'], msg['msg'])
	return True

def get_msgs():
	print("hello getting messages")
	hazelcast_url = os.environ.get('HAZELCAST_URL', False)
	if not hazelcast_url:
		print("can't find hazelcast url")
		return False
	print("hazelcast on", hazelcast_url)
	print("creating hazelcast client")
	#client = hazelcast.HazelcastClient(cluster_name="message-database", cluster_members=[hazelcast_url])
	print("created client")
	storage = client.get_map("messages")
	print("got map")
	data = storage.values().result()
	print("received values")
	return "\n".join([str(i) for i in data])
