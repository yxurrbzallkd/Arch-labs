FROM python:3.9
ENV RUNNING_IN_DOCKER Yes
ENV HZ_CLUSTERNAME message-database
ENV dir lab1
RUN mkdir $dir
RUN ls .
RUN cd $dir
ADD . /$dir
WORKDIR /$dir
RUN pip install -r requirements.txt
CMD "./run.sh"