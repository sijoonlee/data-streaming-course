## Kafka Consumers - intro
In this section you will learn the specifics of how Kafka Consumers are created and managed. Specifically, you will see how to:

- Pull data from one or more Kafka topics into your application
- Use key configuration options, such as consumers and consumers groups, offsets, and offset commits
- Understand and handle topic rebalances
- Specify data deserializers

## Kafka Consumers 
- Kafka consumers subscribe to one or more topics
- Subscribing to a topic that does not exist will create it with default settings
- Topics are polled for data by the Kafka client
- Key Points
    - client.id is an optional setting which is useful in debugging and resource limiting
    - group id is mandatory
    - Poll for data to read data from Kafka
    - poll
    - consume

## Kafka Consumer Offsets
- Kafka keeps track of what data a consumer has seen with offsets
    - Kafka stores offsets in a **private internal topic**
    - Offset tells Kafka Consumer where to start on restart
    - Most client libraries automatically send offsets to Kafka for you on a periodic basis
    - You may opt to commit offsets yourself, but it is not recommended unless there is a specific use-case.
    - Offsets may be sent synchronously or asynchronously
    - Committed offsets determine where the consumer will start up
        - If you want the consumer to start from the first known message, [set auto.offset.reset to earliest]
        - This will only work the first time you start your consumer. On subsequent restarts it will pick up wherever it left off
        - If you always want your consumer to start from the earliest known message, you must manually assign your consumer to the start of the topic on boot