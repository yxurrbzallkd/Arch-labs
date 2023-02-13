bash installations.sh
cd facade
docker build -t facade .
docker run --name facade -d -p 8000:8000 -it facade
cd ..
cd messages
docker build -t messages .
docker run --name messages -d -p 6000:6000 -it messages
cd ..
cd logger
docker build -t logger .
IDS="1 2 3 "
for i in ${IDS}
do
	echo $i "port" 700$i
	docker run --name logger-$i -e HAZELCAST_URL="127.0.0.1:570"$i -d -p 700$i:7000 -it logger
	docker run \
    --name member-$i\
    --network hazelcast-network \
    --rm \
	-d\
    -e HZ_CLUSTERNAME=message-database \
    -p 570$i:5701 \
     hazelcast/hazelcast:5.2.1
done
cd ..
clenup() {
	echo "ctrl+c happened"
	docker rm facade
	docker rm messages
	for i in ${IDS}
	do
		docker rm member-$i
		docker rm  logger-$i
	done
	exit 0
}
echo "waiting for ctrl+c"
while true
do
	trap clenup INT
done


