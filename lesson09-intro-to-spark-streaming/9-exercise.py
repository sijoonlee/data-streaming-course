
"""
Please complete the TODO items in the code below, 
then execute it in the terminal using the command <filename>.py .

Once you execute the code using the spark-submit command 
with SparkSession as the entry point, you’ll see a “spark-warehouse” 
directory appear. It's a metastore that gets generated automatically 
and this is where Spark SQL persists its tables/dataframes. 
This directory can be configured to be generated somewhere else, 
but in the Standalone mode of execution it will always appear 
where your execution code is.
"""
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import pathlib


def run_spark_streaming():
    """
    In this lesson, we're going to import a static json file first to explore the data
    Then load that static data as streaming data
    and show in our terminal
    :return:
    """
    spark = SparkSession.builder \
            .master("local") \
            .appName("spark streaming example") \
            .getOrCreate()


    # read the data file
    file_path = './data/json/data.txt'
    df = spark.read.json(file_path)

    df.show(10, False)

    # TODO based on the df.show, build schema
    jsonSchema = StructType([StructField("status", StringType(), True),
                             StructField("timestamp", TimestampType(), True)])

    # TODO create streamning input dataframe that reads the same dataset, with jsonSchema you created
    streamingInputDF = (
        spark
            .readStream
            .schema(jsonSchema)  # Set the schema of the JSON data
            .option("maxFilesPerTrigger", 1)  # Treat a sequence of files as a stream by picking one file at a time
            .json(file_path)
    )

    # This will be given
    streamingCountsDF = (
        streamingInputDF
            .groupBy(
            streamingInputDF.status,
            window(streamingInputDF.timestamp, "1 hour"))
            .count()
    )

    streamingCountsDF.isStreaming

    # TODO Write query output to console
    query = (
        streamingCountsDF
            .writeStream
            .format("console")  # memory = store in-memory table (for testing only in Spark 2.0)
            .queryName("counts")  # counts = name of the in-memory table
            .outputMode("complete")  # complete = all the counts should be in the table
            .start()
    )


if __name__ == "__main__":
    run_spark_streaming()