FROM python:3.7

#python

RUN mkdir /app

COPY ./start.py /app
COPY ./settings.py /app
COPY ./requirements.txt /app

WORKDIR /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

CMD ["python", "start.py"]