import hazelcast
from threading import Thread

N = 100

def writer():
	client = hazelcast.HazelcastClient(cluster_name="task2")
	queue = client.get_queue("queue")
	for i in range(N):
		while True:
			if queue.size().result() < 10:
				print("put", i)
				queue.put(i)
				break
			print("writer waiting")
	client.shutdown()

def reader(name):
	client = hazelcast.HazelcastClient(cluster_name="task2")
	queue = client.get_queue("queue").blocking()
	for i in range(N):
		print(name, "take", queue.take())
	client.shutdown()

wt = Thread(target=writer)
r1 = Thread(target=reader, args=("reader1",))
r2 = Thread(target=reader, args=("reader2",))
wt.start()
r1.start()
r2.start()
wt.join(timeout=1.0)
r1.join(timeout=1.0)
r2.join(timeout=1.0)

