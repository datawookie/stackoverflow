PACKAGES <- tempfile(fileext = "rds")

pkgversion <- function(package) {
  # Get list of packages from CRAN if
  #
  # - don't have local copy or
  # - local copy more than 5 minutes old.
  #
  if (
    !file.exists(PACKAGES) ||
    difftime(Sys.time(), file.mtime(PACKAGES), unit = "mins") > 5
  ) {
    download.file(
      "cran.r-project.org/src/contrib/PACKAGES.rds",
      PACKAGES,
      quiet = FALSE
    )
  }
  # Read and convert to data frame.
  packages <- readRDS("PACKAGES.rds") |> data.frame()
  # Filter for specified package and return version.
  packages[packages$Package == package,]$Version
}

pkgversion("dplyr")
pkgversion("ggplot2")
pkgversion("tidyr")
