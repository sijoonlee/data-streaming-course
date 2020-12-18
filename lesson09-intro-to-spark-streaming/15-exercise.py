"""
Exercise: Create a DataFrame / Dataset Using Schema
Please complete the TODO items in the code below, then execute it in the terminal using the command spark-submit <filename>.py.

Once you execute the code using the spark-submit command with SparkSession as the entry point, you’ll see a “spark-warehouse” directory appear. It's a metastore that gets generated automatically and this is where Spark SQL persists its tables/dataframes. This directory can be configured to be generated somewhere else, but in the Standalone mode of execution it will always appear where your execution code is.
"""


from pyspark.sql import SparkSession, Row
from pyspark.sql.types import *


def create_spark_session():
    """
    Create SparkSession
    :return:
    """

    spark = SparkSession.builder \
        .master("local[2]") \
        .appName("Schema example") \
        .getOrCreate()

    # TODO build schema for below rows
    schema = StructType([StructField('name', StringType()),
                         StructField('age', IntegerType()),
                         StructField('address', StringType()),
                         StructField('phone_number', StringType())])

    rows = [Row(name='Jake', age=33, address='123 Main Street', phone_number='111-222-3333'),
            Row(name='John', age=48, address='872 Pike Street', phone_number='8972341253')]

    # TODO create dataframe using the rows and schema
    df = spark.createDataFrame(rows, schema)

    # check if schema is created correctly
    df.printSchema()


if __name__ == "__main__":
    create_spark_session()
    """
    root
    |-- name: string (nullable = true)
    |-- age: integer (nullable = true)
    |-- address: string (nullable = true)
    |-- phone_number: string (nullable = true)
    """