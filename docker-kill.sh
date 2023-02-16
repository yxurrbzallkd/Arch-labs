docker kill facade
docker rm facade
docker kill messages-1
docker rm messages-1
docker kill messages-2
docker rm messages-2
for i in 1 2 3
do
	docker kill member-$i
	#docker rm member-$i
	docker kill logger-$i
	docker rm logger-$i
done
