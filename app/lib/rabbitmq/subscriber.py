import pika

print(' Connecting to server ...')

connection=None

try:
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
except pika.exceptions.AMQPConnectionError as exc:
    print("Failed to connect to RabbitMQ service. Message wont be sent.")
    exit(0)

channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

print(' Waiting for messages...')


def callback(ch, method, properties, body):
    print(" Received ==> %s" % body.decode())
    print(" Done")
    print(f"--- ch ------------")
    print(dir(ch))
    print(f"--- method ------------")
    print(dir(method))
    print(f"--- properties ------------")
    print(dir(properties))
    print(f"--- body ------------")
    print(dir(body))
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()