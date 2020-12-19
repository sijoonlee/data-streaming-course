from pyspark.sql import SparkSession

# TO-DO: create a spark session, with an appropriately named application name

#TO-DO: set the log level to WARN

#TO-DO: read the gear-position kafka topic as a source into a streaming dataframe with the bootstrap server localhost:9092, configuring the stream to read the earliest messages possible                                    

#TO-DO: using a select expression on the streaming dataframe, cast the key and the value columns from kafka as strings, and then select them

# TO-DO: create a temporary streaming view called "GearPosition" based on the streaming dataframe
# it can later be queried with spark.sql, we will cover that in the next section 

# TO-DO: write the stream from the select expression earlier to the console, and configure it to run indefinitely, the console output will look something like this:
# +--------------------+-----+
# |                 Key|Value|
# +--------------------+-----+
# |1593939359          |13...|
# +--------------------+-----+