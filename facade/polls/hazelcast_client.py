import hazelcast
import os
import consul
print("importing hazelcast")
c = None
if os.environ.get('RUNNING_IN_DOCKER', False):
	c = consul.Consul("host.docker.internal")
else:
	c = consul.Consul()
#print(c.catalog.node('hazels')[1])
#print(c.catalog.node('hazels')[1]['Services'])
#print(list(c.catalog.node('hazels')[1]['Services'].values()))
#services = list(c.catalog.node('hazels')[1]['Services'].values())
#print(services)
#urls = [f"{i['Address']}:{i['Port']}" for i in services]
hazelcast_cluster = c.kv.get("hz-cluster")
sp = int(c.kv.get("hz-start-port"))
ep = int(c.kv.get("hz-end-port"))
address = int(c.kv.get("hz-url"))
urls = [f"{address}:{port}" for port in range(sp, ep+1)]
print("hazelcast cluster members:", urls)
client = hazelcast.HazelcastClient(cluster_name=hazelcast_cluster,
									   cluster_members=urls)
print("created client")
queue_name = c.kv.get("queue-name")
print("queue name is", queue_name)
queue = client.get_queue(queue_name)
