FROM fedora:39

RUN dnf install -y wget gcc-gfortran hdf5-devel cgnslib openmpi openmpi-devel

RUN wget https://dl.fedoraproject.org/pub/fedora/linux/releases/39/Everything/x86_64/os/Packages/c/cgnslib-devel-4.4.0-2.fc39.x86_64.rpm && \
    rpm -i cgnslib-devel-4.4.0-2.fc39.x86_64.rpm && \
    rm -f cgnslib-devel-4.4.0-2.fc39.x86_64.rpm

ENV PATH=$PATH:/usr/lib64/openmpi/bin/

COPY *.f90 .

RUN mpif90 cgnsreading.f90 -c -I/usr/lib64/gfortran/modules/
RUN mpif90 cgnsread.f90 -c
RUN mpif90 cgnsreading.o cgnsread.o -lcgns -o cgnsread
