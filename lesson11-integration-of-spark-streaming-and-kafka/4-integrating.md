## Recap of Lesson So Far
We have looked at a few key points regarding the integration of Kafka and Spark.

- KafkaSourceProvider provides a consumer for Kafka within Spark, therefore we will not need to create separate consumer modules for consumption.
- Managing offsets becomes crucial to making your Kafka and Spark microservices be best optimized. You’re in full control of your offset management, and you’ll have to make decisions best fitting your business context.

## Integrating Spark and Kafka
Now that we’ve looked over important features on the Kafka API in Spark, we’re ready to integrate Spark and Kafka.

## Kafka Broker with Spark Structured Streaming
To recap from previous lessons, a Kafka broker receives messages from producers. A Kafka broker is a server, and we can think of a Kafka cluster as comprised of one or more Kafka brokers. Producers publish the data (or push messages) into Kafka topics. And then the Kafka consumer pulls messages from a Kafka topic.

Spark Streaming and Structured Streaming already provide a quick way to integrate Kafka to read data and write data back to Kafka.

Once received from Kafka, the source will have the following schema:

- key[binary]
- value[binary]
- topic[string]
- partition[int]
- offset[long]
- timestamp[long]
- timestampType[int]

The value column should contain the most useful (the content) of the messages.

![img](./images/sample.png)

## Sample Integration
```
import logging
import json
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as psf

def run_spark_job(spark):

    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "JSON_TOPIC") \
        .option("startingOffsets", "earliest") \
        .option("maxRatePerPartition", 100) \ # set max number of messages per partition per batch
        .option("maxOffsetsPerTrigger", 10) \
        .load()

    df.printSchema()

    """
    key(binary)
    value(binary)
    topic(string)
    partition(int)
    offset(long)
    timestamp(long)
    timestampType(int)
    """

    kafka_df = df.selectExpr("CAST(value AS STRING"))

    json_df = kafka_df \
        .select(psf.from_json(psf.col('value'), jsonSchema).alias("JSON_TOPIC")) \
        .select("JSON_TOPIC.*")

    query = json_df \
        .writeStream \
        .outputMode("append") \
        .format("console") \
        .start()

    query.awaitTermination()

```