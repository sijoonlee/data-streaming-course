## Spark SQL
- Spark SQL lets you query DataFrame using SQL syntax
- Example
```
spark = SparkSession \
    .builder \
    .appName("Data wrangling with Spark SQL") \
    .getOrCreate()

path = "data/sparkify_log_small.json"

user_log = spark.read.json(path)

user_log.createOrReplaceTempView("user_log_table")

spark.sql("SELECT * FROM user_log_table LIMIT 2").show()
```

## Spark SQL resources
Here are a few resources that you might find helpful when working with Spark SQL
- [Spark SQL built-in functions](https://spark.apache.org/docs/latest/api/sql/index.html)
- [Spark SQL guide](https://spark.apache.org/docs/latest/sql-getting-started.html)

