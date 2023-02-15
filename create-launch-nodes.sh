docker pull hazelcast/hazelcast:5.2.1
docker network create hazelcast-network
#docker run --network hazelcast-network -p 8080:8080 -d hazelcast/management-center:latest-snapshot
for i in 1 2 3
do
echo $i
docker run \
    --name member-$i\
    --network hazelcast-network \
    -e "JAVA_OPTS=-Dhazelcast.client.config=/mnt/c/users/diana/documents/onedrive/architecture/hazelcast/config.xml"\
    --rm \
    -e HZ_CLUSTERNAME=task2 \
    -p 570$i:5701 \
    -d \
     hazelcast/hazelcast:5.2.1
    
done
#-e "JAVA_OPTS=java -Dhazelcast.client.config=/mnt/c/users/diana/documents/onedrive/architecture/hazelcast/config.xml"\
#-e "JAVA_OPTS=-Dhazelcast.config=/opt/hazelcast/config/hazelcast-docker.xml"\
#-v /mnt/c/users/diana/documents/onedrive/architecture/hazelcast/config.xml:/opt/hazelcast/config/hazelcast-docker.xml