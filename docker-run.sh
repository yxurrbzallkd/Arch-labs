echo "launching facade"
docker run --name facade -d -p 8000:8000 -it facade
echo "launching messages"
docker run --name messages -d -p 6000:6000 -it messages
IDS="1 2 3 "
for i in ${IDS}
do
	echo "launching hazelcast member-"$i
	docker run \
    --name member-$i\
    --network hazelcast-network \
    --rm \
	-d \
    -e HZ_CLUSTERNAME=message-database \
    -p 570$i:5701 \
	-it hazelcast/hazelcast:5.2.1
done

for i in ${IDS}
do
	echo "launching logger-"$i
	docker run --name logger-$i \
	-e HZ_CLUSTERNAME=message-database \
	-e HAZELCAST_URL="host.docker.internal:570"$i \
	-d -p 700$i:7000 -it logger
done