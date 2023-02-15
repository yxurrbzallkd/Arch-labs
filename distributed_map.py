import hazelcast
import numpy as np

client = hazelcast.HazelcastClient(cluster_name="task2")
print("getting a map")
# Create a Distributed Map in the cluster
themap = client.get_map("test-distributed-map")#.blocking() 
for i in range(1001):
	print(i)
	themap.set(i, int(np.random.normal()*100))
client.shutdown()