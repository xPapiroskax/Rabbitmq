#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('admin', 'pass')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmqServer', credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World2!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(f" [x] Sent {message}")
connection.close()
