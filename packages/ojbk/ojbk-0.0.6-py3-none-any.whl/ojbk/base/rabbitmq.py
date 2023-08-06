import codefast as cf
import pika
from ojbk.auth import auth
import time
import json


class Connector(object):
    def __init__(self, amqp_url: str, queue_name: str) -> None:
        self.amqp_url = amqp_url
        self.queue_name = queue_name
        params = pika.URLParameters(amqp_url)
        params.socket_timeout = 5
        connection = pika.BlockingConnection(params)

        self.channel = connection.channel()
        self.channel.queue_declare(queue=queue_name)


class Publisher(Connector):
    def __init__(self, amqp_url: str, queue_name: str) -> None:
        super().__init__(amqp_url.strip(), queue_name.strip())

    def post(self, msg: str) -> None:
        # Alias of self.publish
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue_name,
                                   body=msg)
        import json
        cf.info("{} sent to {}".format(json.loads(msg), self.queue_name))
        return

    def publish(self, msg: str) -> None:
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue_name,
                                   body=msg)
        cf.info("{} sent to {}".format(msg, self.queue_name))
        return


class Consumer(Connector):
    def __init__(self, amqp_url: str, queue_name: str) -> None:
        super().__init__(amqp_url, queue_name)
        self.channel.basic_qos(prefetch_count=10)
        return

    def consume(self, callback: callable) -> None:
        self.channel.basic_consume(queue=self.queue_name,
                                   on_message_callback=callback,
                                   auto_ack=True)
        cf.info("Start consuming messages. To exit press CTRL+C")
        self.channel.start_consuming()
        return


def post_message(content: str):
    AMQP_URL = auth.amqp_url
    publisher = Publisher(AMQP_URL, 'telegram_message')
    msg = {'timestamp': time.time(), 'content': content}
    publisher.post(json.dumps(msg))
