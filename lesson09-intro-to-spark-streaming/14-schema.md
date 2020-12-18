## What is a Schema?
Generally, a schema is the description of the structure of your data. It tells you how your data is organized - you can say it’s the blueprint of your data. DataFrames and Datasets use this concept when you create DataFrame and Dataset during run time (implicit) or compile time (explicit).

StructField objects are in tuple (name, type of your data, and nullified represented in True/False), and you need to wrap these objects in StructType to build a schema.

StructType and StructField belong to the org.apache.spark.sql.types package so these need to be imported separately.

## Creating a DataFrame or Dataset using a Schema - Summary
Creating a Schema helps eliminate some errors that can arise while generating your DataFrame.

A Dataset is already type-safe but because it’s a feature not available in Python, we’ll use StructType to build schema for a DataFrame. In this case, a DataFrame’s schema can be represented by StructType and we can apply this schema through the createDataFrame function of SparkSession object.

