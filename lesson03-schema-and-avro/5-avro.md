## Intro to Apache Avro
Apache Avro is a widely used data schema system in the data engineering space, and especially in the Apache Kafka ecosystem. In this section, we’ll review key concepts as they relate to Avro and Stream Processing.

## What is Avro
- data serializtion system that uses binary compression
- data + instruction


## Avro Schema - Key Points
- Apache Avro records are defined in JSON.
- Avro records include a required name, such as "user"
- Avro records must include a type defined as record
- Avro records may optionally include a namespace, such as "com.udacity"
- Avro records are required to include an array of fields that define the names of the expected fields and their associated type. Such as `"fields": [{"name": "age", "type": "int"}]`
- Avro can support optional fields by specifying the field type as either null or some other type. Such as `"fields": [{"name": "age", "type": [“null”, "int"]}]`
- Avro records are made up of complex and primitive types
- Complex types are other records, arrays, maps, and others
- Please reference the Avro documentation for full documentation and additional examples
- Here is what a stock ticker price change schema might look like:
```
{
  “type”: “record”,
  “name”: “stock.price_change”,
  “namespace”: “com.udacity”,
  “fields”: [
      {“name”: “ticker”, “type”: “string”},
      {“name”: “prev_price”, “type”: “int”},
      {“name”: “price”, “type”: “int”},
      {“name”: “cause”, “type”: [“null”, “string”]}
  ]
}
```