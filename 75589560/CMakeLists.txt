cmake_minimum_required(VERSION 3.19)

set(CMAKE_CXX_STANDARD 17)
# set(DOWNLOAD_EXTRACT_TIMESTAMP true)
set(FETCHCONTENT_SOURCE_DIR_DOWNLOAD_EXTRACT_TIMESTAMP true)

add_compile_options(-fPIC)

project(RoutingLib C CXX)

set(CMAKE_CXX_FLAGS_OLD "${CMAKE_CXX_FLAGS}")
set(CMAKE_CXX_FLAGS "-O3")
include(get_grpc.cmake)
include(get_dependencies.cmake)
set(CMAKE_CXX_FLAGS ${CMAKE_CXX_FLAGS_OLD})

add_subdirectory(src)





# # Include FetchContent module
# include(FetchContent)

# # Fetch and make available your dependencies
# FetchContent_Declare(
#     igraph
#     URL https://github.com/igraph/igraph/releases/download/0.10.4/igraph-0.10.4.tar.gz
#     URL_HASH MD5=10a3f325425970c75a7ba8359376e208

# )

# FetchContent_MakeAvailable(igraph FIND_PACKAGE_ARGS NAMES igraph SYSTEM)
