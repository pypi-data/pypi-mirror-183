import json
import pika


class RabbitMQProducer():
    __connection = None
    __channel = None
    version = '0.0.2'    

    def __init__(self, rabbitmq_settings: dict, logs_app=None):
        self.host = rabbitmq_settings['host']
        self.username = rabbitmq_settings['user']
        self.password = rabbitmq_settings['password']
        self.queuename = rabbitmq_settings['queuename']
        self._logs_app = logs_app
    
    def log_error(self, msg: str):
        if self._logs_app:
            self._logs_app.register(msg)
        
        else:
            print(msg)

    def connect(self):
        self.__connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.host,
                credentials=pika.PlainCredentials(
                    self.username, 
                    self.password    
                )
            )
        )
        self.__channel = self.__connection.channel()
        self.__channel.queue_declare(queue=self.queuename)

    def disconnect(self):
        self.__connection.close()
    
    def __rabbitmq_send__(self, data: str):
        self.__channel.basic_publish(
            exchange='',
            routing_key=self.queuename,
            body=data
        )
                       
    def send(self, data):
        try:
            self.connect()
            self.__rabbitmq_send__(
                json.dumps(data)
            )
            self.disconnect()
        
        except pika.exceptions.AMQPConnectionError as error:
            self.log_error('Fail connection RabbitMQ')