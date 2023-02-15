import racy
import optimistic
import pessimistic
from threading import Thread

N = 3

def start(threads):
	for t in threads:
		t.start()

def join(threads):
	for t in threads:
		t.join()

print("Racy test. Expect different results:")
threads = [Thread(target=racy.main) for i in range(N)]
start(threads)
join(threads)

print("Pessimistic test. Expect same results:")
threads = [Thread(target=pessimistic.main) for i in range(N)]
start(threads)
join(threads)

print("Optimistic test. Expect same results:")
threads = [Thread(target=optimistic.main) for i in range(N)]
start(threads)
join(threads)

