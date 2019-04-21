#!/usr/bin/env python
import time
import pika
import zlib

# start a connection with localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# this is a queue named hello
channel.queue_declare(queue='hello')

#img reading
VIDPATH = './example_01.mp4'
video = None

with open(VIDPATH, 'rb') as vid:
	video = vid.read()
	
#compress image
#print('original size: '+str(len(image)))
#video = zlib.compress(image)
#print('compressed size: '+str(len(image)))

#loop to send image
while(True):
	channel.basic_publish(exchange='',
	                  routing_key='hello',
	                  body=video)
	print('video size sent = ' + str(len(video)))
	time.sleep(30)


# close connection
connection.close()