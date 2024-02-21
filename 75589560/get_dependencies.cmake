include(FetchContent)

message(STATUS "Getting iGraph")
FetchContent_Declare(
    igraph
    URL https://github.com/igraph/igraph/releases/download/0.10.4/igraph-0.10.4.tar.gz
    URL_HASH MD5=10a3f325425970c75a7ba8359376e208
    FIND_PACKAGE_ARGS NAMES igraph
    SYSTEM
)

FetchContent_MakeAvailable(igraph)
target_compile_options(igraph PRIVATE -O3)

message(STATUS "Getting GEOS")
FetchContent_Declare(
    GEOS
    URL https://download.osgeo.org/geos/geos-3.11.1.tar.bz2
    URL_HASH MD5=5732ec96b391ecddc35bda9795b654ea
    FIND_PACKAGE_ARGS NAMES GEOS
    SYSTEM
)

FetchContent_MakeAvailable(GEOS)
