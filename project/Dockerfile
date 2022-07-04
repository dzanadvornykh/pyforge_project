FROM python:3.9

RUN apt-get update

RUN mkdir ./project
COPY requirements.txt ./project/requirements.txt
RUN pip install -r ./project/requirements.txt
# RUN chmod 777 ./project/main.py
CMD ["bash"]