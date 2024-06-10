#!/usr/bin/env python
import pika
import time

credentials = pika.PlainCredentials('admin', 'pass')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmqServer', credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True) # Когда RabbitMQ завершает работу или выходит из строя, он забывает очереди и сообщения, если вы не скажете ему этого не делать. durable=True гарантирует, что сообщения не будут потеряны. RabbitMQ не позволяет вам переопределить существующую очередь с другими параметрами и вернет ошибку любой программе, которая попытается это сделать(queue='task_queue').
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(f" [x] Received {body.decode()}")
    time.sleep(body.count(b'.'))
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1) # сообщает RabbitMQ не отправлять более одного сообщения работнику одновременно. Простыми словами, не отправляйте новое сообщение работнику, пока он не обработает и не подтвердит предыдущее. Вместо этого он отправит его следующему работнику, который еще не занят.
channel.basic_consume(queue='task_queue', on_message_callback=callback) # auto_ack=True отключили, чтобы отправить правильное подтверждение от работника, как только мы закончим задачу. Подтверждения сообщений вручную включены по умолчанию.

channel.start_consuming()
