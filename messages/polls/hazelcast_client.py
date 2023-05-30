import hazelcast
import os
print("importing")
hazelcast_cluster = os.environ.get('HZ_CLUSTERNAME', False)
print("hazelcast_cluster", hazelcast_cluster)
RUNNING_IN_DOCKER = os.environ.get('RUNNING_IN_DOCKER', False)
if RUNNING_IN_DOCKER:
	client = hazelcast.HazelcastClient(cluster_name=hazelcast_cluster,
									   cluster_members=["host.docker.internal:5701",
									   					"host.docker.internal:5702",
														"host.docker.internal:5703"])
else:
	client = hazelcast.HazelcastClient(cluster_name=hazelcast_cluster)
print("created client")
queue = client.get_queue("queue")
print("got queue")