# Internal Boostnet WS

## Instructions

### RabbitMQ

```shell
cd rabbitmq
docker build -t rabbitmq .
docker run -p 5432:5432 -d --name rabbitmq rabbitmq
```

### WS Service

```shell
pip install -r requirements.txt
PYTHONPATH=src python main.py
```
