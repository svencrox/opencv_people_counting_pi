#!/usr/bin/env python
import pika
import time
from datetime import datetime
import zlib
import glob
import os
import latestFile
import counting as pc
import csvWrite as csv

# start a connection IF connection is to a remote server
credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('172.17.9.74', 5672, '/', credentials))
# IF host server is local machine then uncomment the below
#connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()

# this is a queue named hello
channel.queue_declare(queue='hello')

# subscirbing callback func to queue, using the callback function to print message
def callback(ch, method, properties, body):
  #initialize count and total
  count = 0
  
  print('received video of size: ' + str(len(body)))
  #open the file that is received at the file location
  with open('./videos/' + str(time.time()) + '.mp4', 'wb') as f:
    f.write(body)

  #getting the latest file from latestFile.py and print it out 
  lat = latestFile.latest()
  print("latest: " + lat)

  #count = return of the counting of totalPeople after runnning image recognition and print output
  count = pc.main("./mobilenet_ssd/MobileNetSSD_deploy.prototxt", "./mobilenet_ssd/MobileNetSSD_deploy.caffemodel",
   lat , "./output/webcam_output.avi")
  print("Total= ", count)

  csv.saveToFile(count)


#start with some initialization for consuming and running callback function
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

    
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()