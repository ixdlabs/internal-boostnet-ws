FROM rabbitmq:3-alpine
RUN apk add wget
RUN wget https://github.com/rabbitmq/rabbitmq-delayed-message-exchange/releases/download/v3.12.0/rabbitmq_delayed_message_exchange-3.12.0.ez \
    -O /opt/rabbitmq/plugins/rabbitmq_delayed_message_exchange.ez
RUN rabbitmq-plugins enable --offline rabbitmq_delayed_message_exchange
RUN rabbitmq-plugins enable --offline rabbitmq_management
RUN apk del wget