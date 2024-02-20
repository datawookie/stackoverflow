#!/bin/bash

g++ -g -o leaky leaky.cpp
valgrind --leak-check=full ./leaky
