import pika, json

params = pika.URLParameters('amqps://fhwpxkma:QT7w_DVKY1BTNx8VgmqooTC-e_ChH5A7@woodpecker.rmq.cloudamqp.com/fhwpxkma')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)