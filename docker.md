

```docker
CMD ["python", "-u", "manage.py", "runserver", "8000"]
```
```bash
docker run --name=facade -p 8000:8000 -it facade
```
server runs on 127.0.0.1:8000, inaccessible

```docker
CMD ["python", "-u", "manage.py", "runserver", "0.0.0.0:8000"]
```
```bash
docker run --name=facade -p 8000:8000 -it facade
```
runs, accessible on localhost

CMD ["python", "-u", "manage.py", "runserver", "127.0.0.1:7000"]
docker run --name logger -p 7000:7000 -it logger
not accessible
docker run --name logger -p 127.0.0.1:7000:7000 -it logger
not accessible

CMD ["python", "-u", "manage.py", "runserver", "0.0.0.0:7000"]
docker run --name logger -p 7000:7000 -it logger

runs, accessible on localhost
