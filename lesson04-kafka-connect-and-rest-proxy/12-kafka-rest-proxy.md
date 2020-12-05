## Kafka REST Proxy
Some applications, for legacy reasons or otherwise, will not be able to integrate a Kafka client directly. Kafka REST Proxy can be used to send and receive data to Kafka topics in these scenarios using only HTTP.

## Overview
- Web server written in Java and Scala, runs on VM
- May run as one instance or in a cluster
- Allows publish/consumption to Kafka over HTTP REST
- Cannot create topics, may only GET topic metadata
- Can be integrated with Schema Registry and use Avro
- Best in scenarios where you can't use a client library
    - using client library has benefits in speed/payload