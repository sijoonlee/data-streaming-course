## Configurations/Tuning Key Points
There are a few ways to tune your Spark Structured Streaming application. But before that, go through your application and try to answer these questions.

- Study the memory available for your application. Do you have enough memory to process your Spark job? If not, consider vertical scaling. If you do have enough memory but limited resources, consider horizontal scaling.
- Study your query plans - do they make sense? Are you doing unnecessary shuffles/aggregations? Can you reduce your shuffles?
- What’s the throughput/latency of your data?
- How are you saving your data? Are you persisting your data to memory or to disk only, or to both memory and disk?
- Are you breaking your lineage anywhere?


## Useful properties
- Spark.executor.memory
- Spark.driver.memory
- Spark.sql.shuffle.partitions
- Spark.default.parallelism