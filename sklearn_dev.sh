#!/bin/bash
git clone git://github.com/scikit-learn/scikit-learn.git
cd scikit-learn
pip install -U cython
python setup.py sdist
