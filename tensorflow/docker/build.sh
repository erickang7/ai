#!/bin/bash

docker rm -f tensorflow
docker rmi -f aiplayground/tensorflow:practice
docker build . --rm -t aiplayground/tensorflow:practice

docker rmi -f $(docker images -q --filter "dangling=true" )