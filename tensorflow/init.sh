#!/bin/bash

docker run \
--name tensorflow \
-v $HOME/projects/ai/practice:/notebooks/workspace \
--mount source=tfvol,target=/notebooks/models \
-p 8888:8888 \
-p 6006:6006 \
-d aiplayground/tensorflow:practice

sleep 1
#docker exec -ti tensorflow bash -c /gitclone_models.sh
docker logs tensorflow | grep token