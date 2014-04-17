__filename__ = 'amqp_consumer'
__author__ = 'jwestover@sonobi.com'


import pika
import json
import sys

class Con(object):

    def __init__(self, jsonify = False, dict_input = False):

        if jsonify:
            if dict_input:
                self.queue = 'hello3'
            else:
                self.queue = 'hello2'
        else:
            self.queue = 'hello1'
        self.conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.conn.channel()
        self.channel.queue_declare(queue=self.queue)

    def receive_messages(self):

        print 'Listening for Messages'

        self.channel.basic_consume(self.callback,
                              queue = self.queue,
                              no_ack = True)


    def callback(self, ch, method, properties, body):
        print 'Received a message: {0}'.format(body)
        if self.queue == 'hello2':
            self.demo2(body)
        elif self.queue =='hello3':
            self.demo3(body)
    def demo2(self, this_list):
        this_list = json.loads(this_list)
        for item in this_list:
            print item


    def demo3(self, this_list):
        this_list = json.loads(this_list)
        for item in this_list:
            print item
        
if __name__ == '__main__':
    app = Con()
    app.receive_messages()