## Lazy Evaluation - Key Points
Lazy evaluation means an expression is not evaluated until a certain condition is met. In Spark, this is when an action triggers the DAG. Transformations are lazy and do not execute immediately. Spark adds them to a DAG of computation, and only when the driver requests some data (with an action function) does this DAG actually get executed.

These are some advantages of lazy evaluation:

Users can organize their Apache Spark program into smaller operations. It reduces the number of passes on data by grouping operations.
Saves resources by not executing every step. It saves the network trips between driver and cluster. This also saves time.