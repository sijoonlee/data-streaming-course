## Kafka Topics in Depth

Kafka Topics are rich in configuration options. To get the most out of Kafka you will need to develop a strong understanding of how these options impact performance. This will include understanding how to replicate topics in Kafka

- data replication can be set on a per-topic basis
- a broker must be an 'in sync replica(ISR)' to become a leader
- desired number of ISRs can be set on topics
- number of ISRs must succeed when data is sent
