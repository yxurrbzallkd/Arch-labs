PYTHON=python3
echo "Starting logger..."
cd logger
i=$1
export HAZELCAST_URL="127.0.0.1:570"$i
$PYTHON manage.py runserver 700$i