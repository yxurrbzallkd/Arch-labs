PYTHON=python3
PIP=pip3
$PIP install django
$PIP install hazelcast-python-client
$PIP install requests
docker pull hazelcast/hazelcast:5.2.1
docker network create hazelcast-network