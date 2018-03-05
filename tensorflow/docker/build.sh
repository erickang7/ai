#!/bin/bash

docker build . --rm -t ericskang/tensorflow:practice
#docker push ericskang/tensorflow:practice

docker rmi -f $(docker images -q --filter "dangling=true" )