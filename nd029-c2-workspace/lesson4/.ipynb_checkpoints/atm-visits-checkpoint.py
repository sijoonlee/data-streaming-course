from pyspark.sql import SparkSession

# TO-DO: create a spark session, with an appropriately named application name

#TO-DO: set the log level to WARN

#TO-DO: read the atm-visits kafka topic as a source into a streaming dataframe with the bootstrap server localhost:9092, configuring the stream to read the earliest messages possible                                    

#TO-DO: using a select expression on the streaming dataframe, cast the key and the value columns from kafka as strings, and then select them

# TO-DO: create a temporary streaming view called "ATMVisits" based on the streaming dataframe
# it can later be queried with spark.sql

#TO-DO: using spark.sql, select * from ATMVisits

# TO-DO: write the stream to the console, and configure it to run indefinitely, the console output will look something like this:
# +--------------------+-----+
# |                 Key|Value|
# +--------------------+-----+
# |1593939359          |13...|
# +--------------------+-----+


