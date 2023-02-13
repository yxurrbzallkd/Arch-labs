docker run --name facade -d -p 8000:8000 -it facade
docker run --name messages -d -p 6000:6000 -it messages
IDS="1 2 3 "
for i in ${IDS}
do
	docker run --name logger-$i -e HAZELCAST_URL="127.0.0.1:570"$i -p 700$i:7000 -it logger
	docker run \
    --name member-$i\
    --network hazelcast-network \
    --rm \
	-d \
	-e "JAVA_OPTS=-Dhazelcast.local.public.Address=127.0.0.1:570"$i \
    -e HZ_CLUSTERNAME=message-database \
    -p 570$i:5701 \
	-it hazelcast/hazelcast:5.2.1
done
cd ..
clenup() {
	echo "ctrl+c happened"
	docker kill facade
	docker rm facade
	docker kill messages
	docker rm messages
	for i in ${IDS}
	do
		docker kill member-$i
		docker rm member-$i
		docker kill logger-$i
		docker rm logger-$i
	done
	exit 0
}
echo "waiting for ctrl+c"
while true
do
	trap clenup INT
done


