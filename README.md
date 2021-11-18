# What is Kafka?

Kafka is an open source software which provides a framework for storing, reading and analysing streaming data.
Kafka is designed to be run in a “distributed” environment, which means that rather than sitting on one user’s computer, it runs across several (or many) servers, leveraging the additional processing power and storage capacity that this brings.

Kafka was originally created at LinkedIn, where it played a part in analysing the connections between their millions of professional users in order to build networks between people. It was given open source status and passed to the Apache Foundation – which coordinates and oversees development of open source software – in 2011


# For run Kafka in single node mode
docker-compose up -d --build



# For run Kafka in cluster node mode

docker-compose -f docker-compose-cluster.yaml up -d --build


After deploying kafka now we should create topic and group_id
kafka-topics.sh --create --zookeeper zookeeper:2181  --replication-factor 1  --partitions 1 --topic sample #create topic
kafka-topics.sh --zookeeper zookeeper:2181 --topic sample --list #list topic
