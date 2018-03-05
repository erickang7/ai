#!/bin/bash
# FROM gcr.io/tensorflow/tensorflow \

docker rm -f tensorflow

docker run \
--name tensorflow \
--mount source=tfvol,target=/notebooks/models \
-p 8888:8888 \
-p 6006:6006 \
-d ericskang/tensorflow:practice

docker exec -ti tensorflow bash -c /gitclone_models.sh

docker logs tensorflow | grep token