FROM python:3.9
ENV RUNNING_IN_DOCKER Yes
ENV dir lab1
RUN mkdir $dir
RUN ls .
RUN cd $dir
ADD . /$dir
WORKDIR /$dir
RUN pip install -r requirements.txt
CMD ["python", "-u", "manage.py", "runserver", "0.0.0.0:6000"]