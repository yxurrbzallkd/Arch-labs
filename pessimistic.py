import hazelcast

def main():
    client = hazelcast.HazelcastClient(cluster_name="task2")
    #print("created client")
    distributed_map = client.get_map("map")#.blocking() 
    #print("got map")
    key = "1"
    distributed_map.put(key, 0)
    #print("Starting")
    for i in range(1000):
        distributed_map.lock(key)
        try:
            value = distributed_map.get(key).result()
            value += 1
            distributed_map.put(key, value)
        finally:
            distributed_map.unlock(key)
    result = distributed_map.get(key).result()
    print("Finished! Result =", result)
    return result
