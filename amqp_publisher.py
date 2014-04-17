__filename__ = 'amqp_publisher'
__author__ = 'jwestover@sonobi.com'


import pika
import json
import sys

class Pub(object):

    def __init__(self, jsonify = False, dict_input = False):

        if jsonify:
            if dict_input:
                temp_message = {}
                for i, item in enumerate(sys.argv):
                    temp_message[i]=item
                self.message=json.dumps(temp_message)
                self.queue = 'hello3'
            else:
                self.message=json.dumps(sys.argv)
                self.queue = 'hello2'
        else:
            self.message = 'this is my silly message'
            self.queue = 'hello1'
        self.conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.conn.channel()
        self.channel.queue_declare(queue=self.queue)

    def send_message(self):
        print 'Sending message: {0}'.format(self.message)
        self.channel.basic_publish(exchange='', routing_key=self.queue, body=self.message)
        print 'Sent'
        self.conn.close()

if __name__ == '__main__':
    app = Pub()
    app.send_message()




