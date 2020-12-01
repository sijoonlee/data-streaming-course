from dataclasses import dataclass, field
import json
import random

from confluent_kafka import Consumer, Producer
from confluent_kafka.admin import AdminClient, NewTopic
from faker import Faker


faker = Faker()

BROKER_URL = "PLAINTEXT://localhost:9092"
TOPIC_NAME = "org.udacity.exercise4.purchases"


def produce(topic_name):
    """Produces data synchronously into the Kafka Topic"""
    #
    # TODO: Configure the Producer to:
    #       1. Have a Client ID
    #       2. Have a batch size of 100
    #       3. A Linger Milliseconds of 1 second
    #       4. LZ4 Compression
    #
    #       See: https://github.com/edenhill/librdkafka/blob/master/CONFIGURATION.md
    #
    p = Producer(
        {
            "bootstrap.servers": BROKER_URL,
            "client.id": "ex4",
            "batch.num.messages": 100,
            "linger.ms": 1000, 
            "batch.num.messages":1000,
            "queue.buffering.max.messages":1000000,
            "queue.buffering.max.kbytes":10000,
            "compression.type": "lz4"
        }
    )
    """
    linger.ms: Alias for queue.buffering.max.ms
            Delay in milliseconds to wait for messages in the producer queue 
            to accumulate before constructing message batches (MessageSets) 
            to transmit to brokers. A higher value allows larger and more effective 
            (less overhead, improved compression) batches of messages to accumulate 
            at the expense of increased message delivery latency.
            Type: float
    batch.num.messages: Maximum number of messages batched in one MessageSet. 
            The total MessageSet size is also limited by batch.size and message.max.bytes.
            Type: integer
    queue.buffering.max.messages: Maximum number of messages allowed on the producer queue. 
            This queue is shared by all topics and partitions.
            Type: integer
    queue.buffering.max.kbytes: Maximum total message size sum allowed on the producer queue. 
            This queue is shared by all topics and partitions. This property has higher priority than queue.buffering.max.messages.
            Type: integer
    """

    while True:
        p.produce(topic_name, Purchase().serialize())


def main():
    """Checks for topic and creates the topic if it does not exist"""
    create_topic(TOPIC_NAME)
    try:
        produce(TOPIC_NAME)
    except KeyboardInterrupt as e:
        print("shutting down")


def create_topic(client):
    """Creates the topic with the given topic name"""
    client = AdminClient({"bootstrap.servers": BROKER_URL})
    futures = client.create_topics(
        [NewTopic(topic=TOPIC_NAME, num_partitions=5, replication_factor=1)]
    )
    for _, future in futures.items():
        try:
            future.result()
        except Exception as e:
            pass


@dataclass
class Purchase:
    username: str = field(default_factory=faker.user_name)
    currency: str = field(default_factory=faker.currency_code)
    amount: int = field(default_factory=lambda: random.randint(100, 200000))

    def serialize(self):
        """Serializes the object in JSON string format"""
        return json.dumps(
            {
                "username": self.username,
                "currency": self.currency,
                "amount": self.amount,
            }
        )


if __name__ == "__main__":
    main()
