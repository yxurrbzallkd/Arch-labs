from polls.hazelcast_client import queue
from django_daemon_command.management.base import DaemonCommand
from time import sleep
from polls.models import Entry

class Command(DaemonCommand):
	def process(self, *args, **options):
		while True:
			#print("running the daemon")
			sleep(1)
			if queue.size().result() > 0:
				#print("queue size is", queue.size().result())
				value = queue.take().result()
				entry = Entry()
				entry.msg = value
				print("recording", value)
				entry.save()

