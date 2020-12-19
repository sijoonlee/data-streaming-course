from kafka import KafkaProducer
import json
import time
import logging

logger = logging.getLogger(__name__)

class ProducerServer(KafkaProducer):

    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    #TODO we're generating a dummy data
    def generate_data(self):
        logger.info("generate data")
        with open(self.input_file) as f:
            for line in json.load(f):
                message = self.dict_to_binary(line)
                # TODO send the correct data
                self.send(self.topic, message)
                time.sleep(0.1)

    # TODO fill this in to return the json dictionary to binary
    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode('utf-8')


if __name__ == "__main__":
    p = ProducerServer(
        input_file='police-department-calls-for-service.json',
        topic='sf.police.calls',
        bootstrap_servers="localhost:9092",
        client_id="sf.police.producer")
    p.generate_data()
        