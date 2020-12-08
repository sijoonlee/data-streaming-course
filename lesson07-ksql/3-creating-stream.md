## Creating Stream
Streams can be created from a Kafka Topic or from a query

```
CREATE STREAM purchases (
    username VARCHAR,
    currency VARCHAR,
    amount INT
) WITH (
    KAFKA_TOPIC = "purchase",
    VALUE_FORMAT = "JSON"
)
```
```
CREATE STREAM purchases_hight_value AS
    SELECT *
    FROM purchases
    WHERE amount > 100000;
```