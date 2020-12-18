## Lesson Overview
We’ll be reviewing action and transformation functions in RDDs/DataFrames/Datasets, and how they affect DAGs and lineage graphs. We’ll also take a look at how to use query plans to best optimize your queries. Lastly, we’ll learn how to join and aggregate on streaming datasets. We’ll use built-in-sinks to view the results of these joins and aggregations.

## Glossary of Key Terms You Will Learn in this Lesson
- Lazy evaluation: An evaluation method for expressions in which expressions are not evaluated until their value is needed.
- Action: A type of function for RDDs/DataFrames/Datasets where the values are sent to the driver. A new RDD/DataFrame/Dataset is not formed.
- Transformation: A lazily evaluated function where a new RDD/DataFrame/Dataset is formed. There are narrow and wide types of transformations - narrow transformations occur within the same partition, whereas wide transformations may occur across all partitions.
- Sink: Place for streaming writes (output).