## Streams and Tables
In this section you will learn to distinguish between streams and tables in stream processing frameworks. You will also learn when to apply each type of approach.

## Stream
- Never-ending immutable series of ordered events
- As new events occur, they are simply appended to the end of the stream.
- Steams are commonly used to enrich data with new fields

## Table
- Tables are the result of aggregation operations in stream processing applications. 
- They are a roll-up, point-in-time view of data. (snapshot)\
- Tables are frequently used to create running summations of critical data

## Streams vs Tables
- Streams and tables are not opposing concepts. 
- In practice, the differentiation of a stream from a table in a stream processing application serves as a description of the type of data that is produced. Applications that are performing aggregations across incoming data are creating tables. Applications that are transforming incoming data into an unending sequence of events are streams.