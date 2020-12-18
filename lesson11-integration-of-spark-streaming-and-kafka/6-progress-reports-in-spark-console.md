## Spark Console Shows Progress Reports
In this concept, we’ll take a look at the Progress Report that shows up in the console. All this information that is coming through the console could be cumbersome, but once we understand what each field is, it’ll be easier to understand.

You’ll see something like this in the Spark Console:
![img](./images/console.png)

This is called a Progress Report. There are obvious key value pairs, like timestamp and batchId, id for each unique query. But what we really need to take a look at are these three pieces of data, because they provide important information regarding the batch size and processed rows:

- numInputRows : The aggregate (across all sources) number of records processed in a trigger.
- inputRowsPerSecond : The aggregate (across all sources) rate of data arriving.
- processedRowsPerSecond : The aggregate (across all sources) rate at which Spark is processing data.
Also you can see that we’re using ConsoleSink which is one of the sinks we mentioned before.

## Breakdown of Report Component
Breakdown of ProgressReporter:
- currentBatchId[Long] : ID of current micro-batch
- Id: UUID of the streaming query
- Name: Name of the streaming query. This can be configured in your code
- Sink: Streaming sink of the streaming query

## Exercise: Generate Progress Report
Requirements:
- Add and change the value of maxRatePerPartition in your option
- Change the value of trigger
- Change the value of startingOffsets
- Again, you can use any Kafka library (pykafka, kafka, kafka-confluent, etc). But if you wish to use a library other than kafka-confluent or kafka-python, you will have to reinstall the library each time you wake up workspace (or anytime after you've refreshed, or woken up, or reset data, or used the "Get New Content" button). The idea here is for you to generate a Python file that has a Kafka producer, and this file should act as your bootstrap server.

## Discussion on Progress Reporter
Take a closer look in the last exercise at the progress reporter that was generated using your Kafka server and Structured Streaming application. With the variations on applications, like maxRatePerPartition and trigger, how did the progress report change? What do they mean? Pick 3-5 fields, and write down what each field means.