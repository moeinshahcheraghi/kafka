FROM python:3.8
RUN mkdir /app
WORKDIR /app
COPY producer.py .
RUN python -m pip install --upgrade pip
RUN pip install kafka-python
RUN pip install requests
ENTRYPOINT [ "python", "./producer.py" ]

