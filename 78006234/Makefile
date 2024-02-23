f2py_module_name = foo

all: foo.pyf foo.cpython-311-x86_64-linux-gnu.so

clean:
	rm -f *.pyf *.so *wrappers* *module.c

foo.pyf: src/foo.f90
	f2py -m $(f2py_module_name) $< -h $@ --overwrite-signature

foo.cpython-311-x86_64-linux-gnu.so: src/foo.f90
	f2py -m $(f2py_module_name) -c $<

foo-f2pywrappers.f foomodule.c foo-f2pywrappers2.f90: src/foo.f90
	f2py -m $(f2py_module_name) $< --lower

test:
	python3 test.py
