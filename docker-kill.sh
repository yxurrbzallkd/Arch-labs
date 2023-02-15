docker kill facade
docker rm facade
docker kill messages
docker rm messages
for i in 1 2 3
do
	docker kill member-$i
	#docker rm member-$i
	docker kill logger-$i
	docker rm logger-$i
done
