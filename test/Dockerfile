FROM python:3.9
ENV dir test
RUN mkdir $dir
RUN ls .
RUN cd $dir
ADD . /$dir
WORKDIR /$dir
RUN pip install -r requirements.txt
#EXPOSE 8000
CMD ["python", "test.py"]