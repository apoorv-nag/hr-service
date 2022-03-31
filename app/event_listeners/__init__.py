from app.event_listeners.example import ExampleListener


def add_channel(channel):
    channel.basic_qos(prefetch_count=1)

    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_consume(queue='task_queue', on_message_callback=ExampleListener().callback)

    channel.start_consuming()