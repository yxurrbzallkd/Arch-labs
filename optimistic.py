import hazelcast

def main():
	client = hazelcast.HazelcastClient(cluster_name="task2")
	#print("created client")
	distributed_map = client.get_map("map")
	#print("got map")
	key = "1"
	distributed_map.put(key, 0)
	#print("Starting")
	for i in range(1000):
	    while True:
	        oldvalue = distributed_map.get(key).result()
	        newvalue = oldvalue+1
	        if distributed_map.replace_if_same(key, oldvalue, newvalue):
	            break
	result = distributed_map.get(key).result()
	print("Finished! Result =", result)
	return result