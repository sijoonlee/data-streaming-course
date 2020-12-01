## How Kafka Works - Summary
In this section we learned:

- A Kafka Broker is an individual Kafka server
- A Kafka Cluster is a group of Kafka Brokers
- Kafka uses Zookeeper to elect topic leaders and store its own configuration
- Kafka writes log files to disk on the Kafka brokers themselves
- How Kafka achieves scale and parallelism with topic partitions
- How Kafka provides resiliency and helps prevent data loss with data replication
- How Kafka Works - Further Research

You might be interested in optional reading about some of these related topics, which are beyond the scope of this course:

[Why does Kafka need Zookeeper?](https://www.cloudkarafka.com/blog/2018-07-04-cloudkarafka_what_is_zookeeper.html)  
[Kafka Design](https://kafka.apache.org/documentation/#design)  
[Partitioning](https://kafka.apache.org/documentation/#intro_topics)  
[Data Replication](https://kafka.apache.org/documentation/#replication)