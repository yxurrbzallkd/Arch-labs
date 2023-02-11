cd facade
docker build -t facade .
docker run --name facade -d -p 8000:8000 -it facade
cd ..
cd logger
docker build -t logger .
docker run --name logger -d -p 7000:7000 -it logger
cd ..
cd messages
docker build -t messages .
docker run --name messages -d -p 6000:6000 -it messages
cd ..
echo "Enter any character to terminate"
read -n 1
docker kill facade
docker kill logger
docker kill messages
