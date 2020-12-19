sudo apt-get install python3-dev
sudo apt-get install librdkafka-dev

# List topic
kafka-topics --list --zookeeper localhost:2181
# Delete topic
kafka-topics --zookeeper localhost:2181 --delete --topic <your-topic-name>


sudo docker exec -it starter_kafka0_1 bash -rm


kafka-console-producer --topic quickstart-events --broker-list localhost:9092
kafka-console-consumer --bootstrap-server localhost:9092 --topic quickstart-events --from-beginning
org.chicago.cta.stations.table.v1
# List all subjects
`curl -X GET http://localhost:8081/subjects`

# Deletes all schema versions registered under the subject "Kafka-value"
`curl -X DELETE http://localhost:8081/subjects/Kafka-value`
  

# Deletes version 1 of the schema registered under subject "Kafka-value"
`curl -X DELETE http://localhost:8081/subjects/Kafka-value/versions/1`


# Deletes the most recently registered schema under subject "Kafka-value"
`curl -X DELETE http://localhost:8081/subjects/Kafka-value/versions/latest`

  
  
  can't use null instead of "null" for json schema
  
# List topic
`kafka-topics --list --zookeeper localhost:2181`

# Delete topic
`kafka-topics --zookeeper localhost:2181 --delete --topic <your-topic-name>`

# List all subjects (schema registry)
`curl -X GET http://localhost:8081/subjects`

# Deletes all schema versions registered under the subject "Kafka-value"
`curl -X DELETE http://localhost:8081/subjects/Kafka-value`

# delete wrong connector
`curl -X DELETE localhost:8083/connectors/stations`

# list all connectors
curl -X GET http://localhost:8083/

# get info connector stations
curl -X GET http://localhost:8083/connectors/stations

curl -X GET http://localhost:8083/connectors/stations/status

curl -X PUT http://localhost:8083/admin/loggers \
     -H "Content-Type:application/json" -d '{"level": "TRACE"}'

curl -X PUT http://localhost:8083/admin/loggers/io.confluent.connect.jdbc.dialect.DatabaseDialects \
     -H "Content-Type:application/json" -d '{"level": "INFO"}'