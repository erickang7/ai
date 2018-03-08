#!/bin/bash

docker exec -ti tensorflow bash

python

import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

exit()

exit

docker logs tensorflow