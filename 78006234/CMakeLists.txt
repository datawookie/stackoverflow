cmake_minimum_required(VERSION 3.12)
project(foo_f2py)

find_package(Python 3.12 REQUIRED COMPONENTS Interpreter Development.Module NumPy)

set(f2py_module_name foo)

add_custom_target(generate_foo_pyf
    COMMAND f2py -m ${f2py_module_name} src/foo.f90 -h foo.pyf --overwrite-signature
    COMMENT "Generate foo.pyf."
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    VERBATIM
)

add_custom_target(generate_foo_so
    COMMAND f2py -m ${f2py_module_name} -c src/foo.f90
    COMMENT "Generate foo.cpython-311-x86_64-linux-gnu.so."
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    VERBATIM
)

add_custom_target(clean_files
    COMMAND rm -f *.pyf *.so *wrappers* *module.c
    COMMENT "Clean files."
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    VERBATIM
)

add_custom_target(run_tests
    COMMAND python3 test.py
    COMMENT "Run test."
    WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
    VERBATIM
)

add_dependencies(generate_foo_so generate_foo_pyf)

# Set default target.
add_custom_target(default_target ALL DEPENDS generate_foo_so)
