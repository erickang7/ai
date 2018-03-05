#!/bin/bash
# FROM gcr.io/tensorflow/tensorflow \

docker rm -f tensorflow

docker run --name tensorflow \
-p 8888:8888 \
-p 6006:6006 \
-d ericskang/tensorflow:practice \
tail -f /dev/null

docker exec -ti tensorflow bash