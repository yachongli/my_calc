#/bin/bash
service rabbitmq-server start
rabbitmqctl add_user nca47 nca47
rabbitmqctl set_permissions nca47 ".*" ".*" ".*"

