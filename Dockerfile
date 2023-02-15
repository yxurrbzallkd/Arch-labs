FROM python:3.9
ENV RUNNING_IN_DOCKER Yes
ENV dir lab
RUN mkdir $dir
RUN ls .
RUN cd $dir
ADD bq_limited_test.py /$dir
ADD requirements.txt /$dir
WORKDIR /$dir
RUN pip install -r requirements.txt
CMD ["python", "bq_limited_test.py"]