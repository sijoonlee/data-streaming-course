## Kafka Producers
In this section you will learn the specifics of how Kafka Producers are created and managed. Specifically, you will see how to:

- Synchronously and asynchronously send data to Kafka
- Use key configuration options, such as batch size, client identifiers, compression, and acknowledgements
- Specify data serializers

## Synchronous Production
- Synchronous producers block producer program execution until the broker has confirmed receipt
- use sync. producers only as necessary!
- ex) money transaction

## Asynchronous Production
- Asynchronous producers send the data and immediately continues
- Kafka clients offer callbacks for when messages are delivered or an error occurs
- Your application code will be given a chance to take rectifying actions
- Producers can decide to fire and forget
