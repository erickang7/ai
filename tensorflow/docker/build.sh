#!/bin/bash

docker rm -f tensorflow
docker rmi -f ericskang/tensorflow:practice
docker build . --rm -t ericskang/tensorflow:practice
docker push ericskang/tensorflow:practice

docker rmi -f $(docker images -q --filter "dangling=true" )