build:
	mpif90 cgnsreading.f90 -c -I/usr/include/
	mpif90 cgnsread.f90 -c
	mpif90 cgnsreading.o cgnsread.o -lcgns -o cgnsread
