import pika

params = pika.URLParameters(
    "amqps://gxttwwrl:GpfmS2JwgksYZCxQFlvD8rpUvXyo6YN_@cow.rmq2.cloudamqp.com/gxttwwrl"
)
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish():
    channel.basic_publish(exchange="", routing_key="admin", body="hello")
