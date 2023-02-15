print("Hello World!")
import hazelcast
print("testing boundedness - trying to insert 11 elements when the bound is 10")
client = hazelcast.HazelcastClient(cluster_name="task2",
									cluster_members=["host.docker.internal:5701"])
print("created client")
queue = client.get_queue("queue").blocking()
print(queue.size())
for i in range(100):
	queue.put(i)
	#print(queue.size())
print("trying to pop 10 elements")
results = [queue.take() for i in range(100)]
print([i for i in results])
