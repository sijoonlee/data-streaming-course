## Joins
- You can join streams and tables in these ways:
    - Join multiple streams to create a new stream.
    - Join multiple tables to create a new table.
    - Join multiple streams and tables to create a new stream.
- ksqlDB supports a large set of join operations for streams and tables, including INNER, LEFT OUTER, and FULL OUTER. Frequently, LEFT OUTER is shortened to LEFT JOIN, and FULL OUTER is shortened to OUTER JOIN.
    | |Type|	INNER|	LEFT OUTER|	FULL OUTER|
    |---|---|---|---|---|
    |Stream-Stream	|Windowed	|Supported	|Supported	|Supported|
    |Table-Table	|Non-windowed	|Supported	|Supported	|Supported|
    |Stream-Table	|Non-windowed	|Supported	|Supported	| Not Supported|

- Co-partitioned data  
    Input data must be co-partitioned when joining. This ensures that input records with the same key, from both sides of the join, are delivered to the same stream task during processing. It's your responsibility to ensure data co-partitioning when joining. For more information, see [Partition Data to Enable Joins](https://docs.ksqldb.io/en/latest/developer-guide/joins/partition-data/).
- Example
```
SELECT p.username, p.amount, u.email
FROM purchase p
JOIN users u ON p.username = u.username;
```
- In above example, if purchase and users are not co-partitioned, we can re-partition.
    - you can use group-by to create intermediate stream that is appropriately co-partitioned for the join

- KSQL JOINs KEY POINTS
    - [KSQL supports Stream to Stream, Stream to Table, and Table to    Table JOINs](https://docs.confluent.io/current/ksql/docs/developer-guide/join-streams-and-tables.html#join-event-streams-with-ksql)
    - [Limitations on the kind of JOINs supported exist for each of the types of JOINs](https://docs.confluent.io/current/ksql/docs/developer-guide/join-streams-and-tables.html#join-capabilities)
    - [Stream to Stream JOINs may be windowed](https://docs.confluent.io/current/ksql/docs/developer-guide/join-streams-and-tables.html#joins-and-windows)
    - [JOINed entities must be co-partitioned](https://docs.confluent.io/current/ksql/docs/developer-guide/join-streams-and-tables.html#join-requirements)
    - [JOINed data must share the same KEY in KSQL as used for the Kafka record](https://docs.confluent.io/current/ksql/docs/developer-guide/join-streams-and-tables.html#join-requirements)