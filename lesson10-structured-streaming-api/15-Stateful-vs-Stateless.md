## State
- the intermediate data maintained between records
- you will want to retrieve state later

## Stateful vs Stateless
- Stateful stream processing means past events can affect the way current and future events are processed
- Stateful systems can keep track of windows and perform counts
    - these metrics can be checkpointed
- Stateless stream processing is easy to scale up because events are processed independently

## Need of State Store
- important because state is intermediary object that you will want to retrieve later
- can use in-memory hashmap, HDFS, Cassandra, AWS DynamoDB, etc
- when a failure occurs in the driver or the executor, users can recover from the state right before the failure

## Recovery of State
The accumulating result of the state should be stored in a fault-tolerant state store of your choice.

The purpose of state store is to provide a reliable place in your services so that the application (or the developer) can read the intermediary result of stateful aggregations. Even in the case of driver or worker failures, Spark is able to recover the processing state at the point right before the failure. The state stored is supported by HDFS compatible file system. To guarantee recoverability, Spark recovers the two most recent versions. If batch number 10 fails, then the batch number 9 and 8 are both recovered.

We can implement the state store by implementing org.apache.spark.sql.execution.streaming.state.StateStore properties.

## Sample Code for Checkpointing
We are providing the code here rather than in a workspace, because checkpoint requires a HDFS-compatible file system but our classroom workspaces do not currently offer HDFS-compatible file systems.

```
from pyspark.sql import SparkSession

def checkpoint_exercise():
    """
    note that this code will not run in the classroom workspace because we don't have HDFS-compatible file system
    :return:
    """
    spark = SparkSession.builder \
            .master("local") \
            .appName("Checkpoint Example") \
            .getOrCreate()

    df = spark.readStream \
        .format("rate") \
        .option("rowsPerSecond", 90000) \
        .option("rampUpTime", 1) \
        .load()

    rate_raw_data = df.selectExpr("CAST(timestamp AS STRING)", "CAST(value AS string)")

    stream_query = rate_raw_data.writeStream \
        .format("console") \
        .queryName("Default") \
        .option("checkpointLocation", "/tmp/checkpoint") \ #this checkpoint location requires HDFS-like filesystem
        .start()

if __name__ == "__main__":
    checkpoint_exercise()
```