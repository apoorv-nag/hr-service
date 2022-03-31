class ExampleListener():

    def callback(self, ch, method, properties, body):
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

