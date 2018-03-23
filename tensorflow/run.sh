#!/bin/sh

docker start tensorflow

docker logs tensorflow | grep token