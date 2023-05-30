import hazelcast
import os
print("importing")
hazelcast_url = os.environ.get('HAZELCAST_URL', False)
hazelcast_cluster = os.environ.get('HZ_CLUSTERNAME', False)
print("hazelcast_cluster", hazelcast_cluster, "hazelcast_url", hazelcast_url)
client = hazelcast.HazelcastClient(cluster_name=hazelcast_cluster, cluster_members=[hazelcast_url])
print("created client")