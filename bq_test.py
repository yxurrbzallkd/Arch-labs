import hazelcast
from threading import Thread

QUEUE="queue"
CLUSTER="task2"

def reader_cycle(name):
	print(name)
	client = hazelcast.HazelcastClient(cluster_name=CLUSTER)
	print("created client", name)
	queue = client.get_queue(QUEUE)
	for i in range(1000):
		value = queue.take()
		if value:
			print(name, value)

def writer_cycle(name):
	print(name)
	client = hazelcast.HazelcastClient(cluster_name=CLUSTER)
	print("created client", name)
	queue = client.get_queue(QUEUE)
	for i in range(1000):
		queue.put(i)
		print(name, i)

w = Thread(target=writer_cycle, args=("writer",))
r1 = Thread(target=reader_cycle, args=("reader1",))
r2 = Thread(target=reader_cycle, args=("reader2",))
w.start()
r1.start()
r2.start()
w.join()
r1.join()
r2.join()

