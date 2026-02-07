#!/usr/bin/env bash
#Tell Python to use the unittest standard library to run all the tests (discover) 
# it can find in the src directory
python3 -m unittest discover -s src
