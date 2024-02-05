from confluent_kafka import Consumer, KafkaException
import json
import pandas as pd


def read_latest_message(consumer, topic):
    """Read the latest message from the specified Kafka topic."""
    consumer.subscribe([topic])

    try:
        msg = consumer.poll(timeout=10.0)
        if msg is None:
            return None
        if msg.error():
            if msg.error().code() == KafkaException._PARTITION_EOF:
                # End of partition event
                print('%% %s [%d] reached end at offset %d\n' %
                      (msg.topic(), msg.partition(), msg.offset()))
            else:
                raise KafkaException(msg.error())
        else:
            # Proper message
            record = json.loads(msg.value().decode('utf-8'))
            df = pd.DataFrame([record])
            return df
    finally:
        # Do not close the consumer here; it should be reused
        pass

