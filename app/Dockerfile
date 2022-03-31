FROM ubuntu:18.04

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev && \
    apt-get install -y python3-pip python3-venv

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN python3 -m venv venv

#RUN source venv/bin/activate

#RUN pip3 install pika && \
RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "flask" ]

CMD [ "run", "--host=0.0.0.0" ]