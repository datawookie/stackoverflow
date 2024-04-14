program SaveGrid
    implicit none

    integer :: nv
    integer :: Nx, Ny, Nzt
    real, dimension(:), allocatable :: xx, yy, zz
    integer :: i

    nv = 3
    Nx = 5
    Ny = 7
    Nzt = 10

    allocate(xx(Nx), yy(Ny), zz(Nzt))

    do i = 1, Nx
        xx(i) = float(i)
    end do
    do i = 1, Ny
        yy(i) = float(i) * 2.0
    end do
    do i = 1, Nzt
        zz(i) = float(i) * 3.0
    end do

    open(unit=11, file="ring.grid", form="unformatted")

    write(11) nv
    write(11) Nx, Ny, Nzt
    write(11) xx
    write(11) yy
    write(11) zz

    close(11)

    deallocate(xx, yy, zz)
end program SaveGrid
