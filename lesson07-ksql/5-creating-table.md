## Creating a Table
- Tables can be created from a Kafka Topic or from a query
```
CREATE TABLE users(
    username VARCHAR,
    address VARCHAR,
    email VARCHAR,
    phone_number VARCHAR
) WITH (
    KAFKA_TOPIC = 'purchases',
    VALUE_FORMAT = 'JSON'
    KEY = 'username' 
)
```
**KEY should be string(VARCHAR), can't be Avro or JSON**

```
CREATE TABLE purchases_high_value AS
    SELECT *
    FROM purchases
    WHERE amount > 100000;
```