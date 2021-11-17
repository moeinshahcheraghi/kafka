import kafka 
from json import loads
consumer = kafka.KafkaConsumer(
    'sample',
    bootstrap_servers=['kafka:9092' , 'kafka:9093' , 'kafka:9094'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='sample1',
     value_deserializer=lambda x: loads(x.decode('utf-8')))
for message in consumer:
    message = message.value
    collection.insert_one(message)
    print('{} added to {}'.format(message, collection))
