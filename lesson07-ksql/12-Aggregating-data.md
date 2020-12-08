## KSQL Aggregations
- Example
    ```
    SELECT currency SUM(amount)
    FROM purchase
    WINDOW SESSION (30 MINUTES)
    GROUP BY currency;
    ```
- [Use GROUP BY to create aggregations in KSQL](https://docs.confluent.io/current/ksql/docs/developer-guide/aggregate-streaming-data.html)
- GROUP BY always creates a KSQL Table
- [KSQL supports aggregations like COUNT, MAX, MIN, SUM, TOPK, HISTOGRAM and more](https://docs.confluent.io/current/ksql/docs/developer-guide/syntax-reference.html#aggregate-functions)
