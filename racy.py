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
		value = distributed_map.get(key).result()
		value += 1
		distributed_map.put(key, value)
	print("Finished! Result =", distributed_map.get(key).result())
	return distributed_map.get(key).result()
