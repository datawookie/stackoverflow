function read_fortran_binary(filename)
    open(filename, "r") do file
        # Read record marker.
        record_size = read(file, Int32)
        # Read data.
        nv = read(file, Int32)
        # Read record marker.
        end_record_size = read(file, Int32)

        # Read record marker.
        read(file, Int32)
        # Read data.
        Nx = read(file, Int32)
        Ny = read(file, Int32)
        Nzt = read(file, Int32)
        # Read record marker.
        read(file, Int32)

        return nv, Nx, Ny, Nzt
    end
end

nv, Nx, Ny, Nzt = read_fortran_binary("/mnt/ring.grid")

println("nv:  ", nv)
println("Nx:  ", Nx)
println("Ny:  ", Ny)
println("Nzt: ", Nzt)
