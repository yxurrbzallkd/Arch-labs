PYTHON=python3
pip3 install python-consul
echo "Starting consul"
docker run \
    -d \
    -p 8500:8500 \
    -p 8600:8600/udp \
    --name=badger \
    consul agent -server -ui -node=server-1 -bootstrap-expect=1 -client=0.0.0.0
echo "Storing key-value info into consul"
$PYTHON kv_setup.py
for i in 1 2 3
do
	echo "launching hazelcast member-"$i
	docker run \
    --name member-$i\
    --network hazelcast-network \
    --rm \
	-d \
    -p 570$i:5701 \
	-it hazelcast/hazelcast:5.2.1
	docker exec hazels /bin/sh -c  \
	"echo '{\"service\": {\"name\": \"hazel-$i\", \"tags\": [\"go\", \"hazel\"], \"port\": 570$i, \"address\": \"host.docker.internal\"}}' > /consul/config/conf-h-$i.json"
	docker exec hazels consul reload
done
sleep 3
exit 0
docker run --name=facades -d \
consul agent -node=facades -retry-join="172.17.0.2"
echo "launching facade"
for i in 1 2 3
do
	docker run --name facade-$i -d -p 800$i:8000 -it facade
	docker exec facades /bin/sh -c  \
	"echo '{\"service\": {\"name\": \"facade-$i\", \"tags\": [\"go\", \"facade\"], \"port\": 800$i, \"address\": \"host.docker.internal\"}}' > /consul/config/conf-f-$i.json"
	docker exec facades consul reload
done
sleep 3
docker run --name=messages -d \
consul agent -node=messages -retry-join="172.17.0.2"
echo "launching messages"
for i in 1 2
do
	docker run --name messages-$i -d -p 500$i:8000 -it facade
	docker exec messages /bin/sh -c  \
	"echo '{\"service\": {\"name\": \"messages-$i\", \"tags\": [\"go\", \"message\"], \"port\": 500$i, \"address\": \"host.docker.internal\"}}' > /consul/config/conf-m-$i.json"
	docker exec messages consul reload
done
sleep 3
echo "launching logger"
docker run --name=loggers -d \
consul agent -node=loggers -retry-join="172.17.0.2"
for i in 1 2 3
do
	echo "launching logger-"$i
	docker run --name logger-$i \
	-e HAZELCAST_URL="host.docker.internal:570$i" \
	-d -p 700$i:7000 -it logger
	docker exec loggers /bin/sh -c  \
	"echo '{\"service\": {\"name\": \"logger-$i\", \"tags\": [\"go\", \"logger\"], \"port\": 700$i, \"address\": \"host.docker.internal\"}}' > /consul/config/conf-l-$i.json"
	docker exec loggers consul reload
done

