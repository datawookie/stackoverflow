import time
import numpy as np
from netCDF4 import Dataset

netcdf_file_path = "/data/test_echam_spectral-deflated.nc"

start_time = time.time()

dataset = Dataset(netcdf_file_path, mode="r")

for var in dataset.variables:
    np.array(dataset.variables[var][:])

end_time = time.time()

elapsed_time = end_time - start_time

print(f"Time taken to load the NetCDF file: {elapsed_time} seconds")

dataset.close()
