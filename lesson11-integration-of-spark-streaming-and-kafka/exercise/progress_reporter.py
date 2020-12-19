import logging
from pyspark.sql import SparkSession
# https://pypi.org/project/pyspark/
def run_spark_job(spark):

    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:<your port>") \
        .option("subscribe", "<your topic name>") \
        .option("startingOffsets", "earliest") \
        .option("maxOffsetsPerTrigger", 10) \
        .option("maxRatePerPartition", 10) \
        .option("stopGracefullyOnShutdown", "true") \
        .load()

    # Show schema for the incoming resources for checks
    df.printSchema()
    
    agg_df = df.count()
    
    # play around with processingTime to see how the progress report changes
    # https://spark.apache.org/docs/latest/api/java/org/apache/spark/sql/streaming/Trigger.html#ProcessingTime-scala.concurrent.duration.Duration-
    query = agg_df \
        .writeStream \
        .trigger(processingTime="<change this>") \
        .outputMode('Complete') \
        .format('console') \
        .option("truncate", "false") \
        .start()
        
if __name__ == "__main__":
    logger = logging.getLogger(__name__)

    spark = SparkSession \
        .builder \
        .master("local[*]") \
        .appName("StructuredStreamingSetup") \
        .getOrCreate()

    logger.info("Spark started")

    run_spark_job(spark)

    spark.stop()
