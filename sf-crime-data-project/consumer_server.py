from kafka import KafkaConsumer
import json
import logging

logger = logging.getLogger(__name__)

class ConsumerServer():

    def __init__(self, topic, **kwargs):
        self.consumer = KafkaConsumer(topic,**kwargs)

    def run(self):
        logger.info("run consumer")
        for message in self.consumer:
            print(f"-------- offset - {message.offset} ----------")
            print(message.value)

if __name__ == "__main__":
    c = ConsumerServer(
        topic='sf.police.calls',
        group_id='sf.police.consumer',
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
        auto_offset_reset='earliest',
        enable_auto_commit=False,
    )
    c.run()