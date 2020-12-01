## Metrics for Consumer Performance
- Consumer
    - Consumer lag
        - lag = latest topic offset in the topic partition - consumer topic offset
        - if the lag increases over time, it means Consumer can't keep up
        - use Kafka Clyde tool to measure consumer lag
        - Adding compression may reduce network overhead, it may also introduce additional CPU-time to decompress the messages
    - Messages Per Second indicates throughput
    - Kafka Java Metrics Exporter provides real-time metrics

- Producer
    - Producer latency
        - latency = time broker received - time produced
        - High latency may indicate
            - too high acks setting
            - too many partitions
            - too many replicas
    - Producer response rate tracks overall delivery rate
        - how many messages are delivered over time
        - can be measured by produce delivery callbacks

- Broker
    - Disk usage
        - high disk usage can cause outrage
    - Network usage
        - high network usage may slow consume/produce
    - Election frequency is critical, should be infrequent
    - Elections stop all consume/produce, very disruptive
    - Frequent elections indicate broker instability


## Performance Considerations - Summary
Monitoring Kafka Consumers, Producers, and Brokers for performance is an important part of using Kafka. There are many metrics by which to measure your Kafka cluster. Focus on these key metrics to get started:
- Consumer Lag: The difference between the latest offset in the topic and the most recently committed consumer offset
- Producer Response Rate: The rate at which the broker is responding to the producer indicating message status
- Producer Request Latency: The length of time a producer has to wait for a response from the broker after sending a message
- Broker Disk Space
- Broker Elections

## Further Research
[DataDog blog post on monitoring Kafka](https://www.datadoghq.com/blog/monitoring-kafka-performance-metrics)
[Confluent article on monitoring Kafka](https://docs.confluent.io/current/kafka/monitoring.html)
[New Relic article on monitoring Kafka](https://blog.newrelic.com/engineering/new-relic-kafkapocalypse/)