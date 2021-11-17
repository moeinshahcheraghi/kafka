FROM python:3.8
RUN mkdir /app
WORKDIR /app
COPY consumer.py .
RUN python -m pip install --upgrade pip
RUN pip install kafka-python
CMD [ "python" , "./consumer.py" ]
