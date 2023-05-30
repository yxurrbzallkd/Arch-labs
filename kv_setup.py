import consul
consul = consul.Consul()
print("storing queue name ", consul.kv.put("queue-name", "queue"))
print("storing hazelcast cluster name", consul.kv.put("hz-cluster", "message-database"))
print("storing hazelcast start port", consul.kv.put("hz-start-port", '5701'))
print("storing hazelcast end port", consul.kv.put("hz-end-port", '5703'))
print("storing hazelcast url", consul.kv.put("hz-url", "host.docker.internal"))
