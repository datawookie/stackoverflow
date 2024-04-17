# devtools::install_github("jkeirstead/scholar")

library(tibble)
library(dplyr)
library(purrr)
library(scholar)

# Create some test data.
info <- tribble(
  ~first_name, ~last_name, ~affiliation,
  "Maggie", "Collier", NA,
  "Dennis", "Lichtenberger", NA,
  "Ingo", "Steinbach", "Ruhr-Universitaet Bochum",
  "Michael", "Sander", "ETH Zurich",
  "ray", "craib", NA
)
# Replicate the test data to 500 records.
info <- bind_rows(replicate(100, info, simplify = FALSE))

nrow(info)

scholar_ids <- pmap_chr(info, function(...) {
  print(Sys.time())
  Sys.sleep(15)
  get_scholar_id(...)
})
