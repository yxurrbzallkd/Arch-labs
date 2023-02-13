PYTHON=python3
bash installations.sh
echo "Starting facade..."
cd facade
$PYTHON manage.py runserver 8000&
F_ID=$!
cd ..
echo "Starting logger..."
cd logger
LIDS=""
#docker build -t logger .
IDS="1 2 3 "
for i in ${IDS}
do
	echo $i "port" 700$i
	#docker run --name logger -e HAZELCAST_URL="http://172.18.0.3:570"$i -d -p 700$i:7000 -it logger
	L_ID=$!
	LIDS="$LIDS $L_ID"
	docker run \
    --name member-$i\
    --network hazelcast-network \
    --rm \
	-d \
    -e HZ_CLUSTERNAME=message-database \
    -p 570$i:5701 \
     hazelcast/hazelcast:5.2.1
done
cd ..
echo "Starting messages..."
cd messages
$PYTHON manage.py runserver 5000&
M_ID=$!
cd ..
clenup() {
	echo "ctrl+c happened"
	kill $F_ID
	for i in ${IDS}
	do
		docker kill member-$i
	done
	kill $M_ID
	cd logger
	$PYTHON manage.py flush # clear database
	cd ..
	exit 0
}
echo "waiting for ctrl+c"
while true
do
	trap clenup INT
done
