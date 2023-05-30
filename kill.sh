for i in 1 2 3
do
	docker kill facade-$i
	docker rm facade-$i
done
for i in 1 2
do
	docker kill messages-$i
	docker rm messages-$i
done
for i in 1 2 3
do
	docker kill member-$i
	#docker rm member-$i
	docker kill logger-$i
	docker rm logger-$i
done
docker kill badger
docker rm badger
docker kill facades
docker rm facades
docker kill loggers
docker rm loggers
docker kill messages
docker rm messages
docker kill hazels
docker rm hazels
