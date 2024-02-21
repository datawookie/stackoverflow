cmake_minimum_required(VERSION 3.15)
SET(CMAKE_CXX_STANDARD 17)

add_compile_options(-fPIC)

project(RoutingLib C CXX)

set(CMAKE_CXX_FLAGS_OLD "${CMAKE_CXX_FLAGS}")
set(CMAKE_CXX_FLAGS "-O3")
include(get_grpc.cmake)
include(get_dependencies.cmake)
set(CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS_OLD})

add_subdirectory(src)
