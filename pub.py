import zmq
import random
from time import sleep

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind('tcp://127.0.0.1:2000')

while True:
    channel = raw_input("Channel to publish: ")
    content = raw_input("> ")
    socket.send("{channel} {content}".format(channel=channel, content=content))
