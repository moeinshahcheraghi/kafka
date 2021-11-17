from time import sleep
from json import dumps
import kafka 
producer = kafka.KafkaProducer(bootstrap_servers=['kafka:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
for e in range(1000):
    data = {'number' : e}
    producer.send('sample', value=data)
    sleep(5)
