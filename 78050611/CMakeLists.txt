cmake_minimum_required(VERSION 3.10)
project(project)

add_executable(executable main.cpp)

install(TARGETS executable DESTINATION bin)
