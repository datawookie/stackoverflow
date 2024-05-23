library(raster)

files <- list.files(pattern = ".nc", full.names=TRUE)

region <- extent(-180, -176, -40, -36)

data <- lapply(files, function(path) {
  # Load and crop.
  d <- brick(path, stopIfNotEqualSpaced = FALSE, varname = "chlor_a") |>
    crop(region)

  # Get raster values.
  values <- getValues(d)
  # Get coordinates.
  coords <- coordinates(d)

  cbind(coords, values) |>
    data.frame() |>
    setNames(c("lon", "lat", "value")) |>
      na.omit()
})

head(data[[1]])

# print(files)
#
# nc <- ncdf4::nc_open("./AQUA_MODIS.20030101.L3b.DAY.CHL.nc")
#
# # List all variable names
# vars <- names(nc$var)
# print(vars)
#
# # Close the file
# ncdf4::nc_close(nc)

raster_brick <- data[[2]]

# Get the raster values
values <- getValues(raster_brick)

# Get the coordinates
coords <- coordinates(raster_brick)

# Combine coordinates and values into a data frame
data_df <- data.frame(lon = coords[, 1], lat = coords[, 2], chlor_a = values)

# Display the first few rows of the data frame
head(data_df)





cropped_raster <- crop(data[[1]], filter_extent)
