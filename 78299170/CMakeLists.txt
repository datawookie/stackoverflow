cmake_minimum_required(VERSION 3.8)

set(CMAKE_CXX_STANDARD 14)

project(glcrash)

file(GLOB_RECURSE COMPILABLE_FILES CONFIGURE_DEPENDS main.cpp)

find_package(GLEW REQUIRED)
find_package(glfw3 REQUIRED)

add_executable(${PROJECT_NAME} ${COMPILABLE_FILES})

target_link_libraries(${PROJECT_NAME}
    GLEW::GLEW
    glfw
)
