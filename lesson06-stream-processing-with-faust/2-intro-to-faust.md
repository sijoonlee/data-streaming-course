## What is Faust?
- created at Robinhood
- Design goal was to replicate Kafka Streams in Python
- Shares conceptual design patterns with Kafka Streams
- Stream processing natively written in Python
- Concepts applicable in other frameworks as well

## Introduction to Faust
- Faust is built using modern Python features such as asyncio. 
- Faust is embeddable as a library in existing applications. 
- It can also be configured to be deployed as a stand-alone application in your infrastructure. 
- Faust implements storage, time windowing, streams, tables, and many of the aggregate functions discussed in Lesson 5. 
- It is important to note that Faust requires Python 3.6+ and does not support Avro or Schema Registry natively at this time.

## Robinhood Faust - Key Points
- [Built at Robinhood to tackle stream processing problems natively in Python](https://robinhood.engineering/faust-stream-processing-for-python-a66d3a51212d?gi=25dc91767251)
- Faust takes its design inspiration from [Kafka Streams, a JVM-only framework](https://kafka.apache.org/documentation/streams/)
- Faust is built using [modern Python features like asyncio, and requires Python 3.6 or higher](https://docs.python.org/3/library/asyncio.html)
- Faust’s API implements the storage, windowing, aggregation, and other concepts discussed in Lesson 5
- Faust is a native Python API, not a Domain Specific Language (DSL) for metaprogramming
- Requires no external dependency other than Kafka. Does not require a resource manager like Yarn or Mesos.
- Faust does not natively support Avro or Schema Registry

## Further Optional Research - Exploring Faust Functionality in More Depth
- [See the Faust documentation for in-depth documentation of how Faust works](https://faust.readthedocs.io/en/latest/introduction.html)
- Every Faust application has an [App which instantiates the top-level Faust application](https://faust.readthedocs.io/en/latest/userguide/application.html#what-is-an-application)
- The application must be assigned a [topic to subscribe to](https://faust.readthedocs.io/en/latest/userguide/application.html#app-topic-create-a-topic-description)
- An output Table or stream receives the output of the processing
- An asynchronous function is decorated with an agent which register the function as a callback for the application when data is received