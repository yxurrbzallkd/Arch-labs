import hazelcast
import os
print("importing")
hazelcast_url = os.environ.get('HAZELCAST_URL', False)
print("hazelcast_url", hazelcast_url)
client = hazelcast.HazelcastClient(cluster_name="message-database", cluster_members=[hazelcast_url])
print("created client")