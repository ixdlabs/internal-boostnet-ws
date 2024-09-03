# Internal Boostnet WS

## Instructions

### RabbitMQ

```shell
cd rabbitmq
docker build -t rabbitmq .
docker run -p 5432:5432 -p 15672:15672 -d --name rabbitmq rabbitmq
```

### WS Service

```shell
pip install -r requirements.txt
PYTHONPATH=src python main.py
```

### deploymment commands
#### rabbitmq
```shell
docker run -p 5672:5672 -p 15672:15672 -d --name rabmqcon -e RABBITMQ_DEFAULT_USER=super*** -e RABBITMQ_DEFAULT_PASS=********** rabbitmq:3-management
```

#### boostnet-ws
```shell
docker run -p 80:3000 -d --name boostnet-ws-con -e AMQP_URL='amqp://user:userpassword@rabbitmqserverip:5672' boostnet-ws
```
