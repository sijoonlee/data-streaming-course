from pyspark.sql import SparkSession

logFile = "/home/workspace/Test.txt"  # Should be some file on your system
spark = SparkSession.builder.appName("HelloSpark").getOrCreate()
spark.sparkContext.setLogLevel('WARN')

logData = spark.read.text(logFile).cache()

numAs = logData.filter(logData.value.contains('a')).count()
numBs = logData.filter(logData.value.contains('b')).count()

print("*******")
print("*******")
print("*****Lines with a: %i, lines with b: %i" % (numAs, numBs))
print("*******")
print("*******")
spark.stop()