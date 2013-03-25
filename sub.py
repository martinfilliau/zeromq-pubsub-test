import zmq

context = zmq.Context()

sock = context.socket(zmq.SUB)
sock.connect('tcp://127.0.0.1:2000')

channel = raw_input('Suscribe to channel: ')

sock.setsockopt(zmq.SUBSCRIBE, channel)

while True:
    input = sock.recv()
    print input
