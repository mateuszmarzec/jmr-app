FROM alpine:latest
RUN apk add --no-cache --update gcc python3-dev musl-dev postgresql-dev
ADD ./requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade pip --no-cache-dir -q -r /tmp/requirements.txt
ADD . /opt/jmr-app/
WORKDIR /opt/jmr-app
RUN python3 manage.py collectstatic --noinput
RUN python3 manage.py migrate
CMD gunicorn --bind 0.0.0.0:$PORT jmr.wsgi