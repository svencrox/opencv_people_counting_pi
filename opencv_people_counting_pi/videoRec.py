#!/usr/bin/env python
import pika
import time
import datetime
import zlib
import glob
import os
import latestFile
import counting as pc

# start a connection with localhost
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# this is a queue named hello
channel.queue_declare(queue='hello')

#pc.listen()

# subscirbing callback func to queue, using the callback function to print message
def callback(ch, method, properties, body):
    print('received video of size: ' + str(len(body)))
    with open('./videos/' + str(time.time()) + '.mp4', 'wb') as f:
    	f.write(body)
    lat = latestFile.latest()
    # lat = "./videos/" + str(lat)
    print("latest: " + lat)
    count = 0
    count = pc.main("./mobilenet_ssd/MobileNetSSD_deploy.prototxt", "./mobilenet_ssd/MobileNetSSD_deploy.caffemodel",
     lat , "./output/webcam_output.avi")
    print("Total= ", count)



channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

    
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()