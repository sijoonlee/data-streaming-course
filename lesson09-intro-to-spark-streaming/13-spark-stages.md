## Stage
- A stage is a group set of tasks
- It is a physical unit of the execution plan
- Spark stages are similar to the map/reduce stages in Hadoop MapReduce

## Spark Stages
- ShuffleMapStage
    - an intermediate Spark stage in the physical execution of DAGs
    - Produces data for other stages
- ResultSage
    - final stage in a Spark job
    - result of an action


## Example
```
lines = spark.read.text(file_path).rdd.map(lambda x:x[0])
counts = lines.flatMap(lambda x: x.split(' ')).map(lambda x(x, 1)).reduceByKey()

output = counts.write.parquet("file_path_to_save")
```
- In above example, there are two stages
    - ShuffleMapStage: read / map / flatMap / map
    - ResultSage: reduceByKey / write

