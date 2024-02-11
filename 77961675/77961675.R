library(dplyr)
library(purrr)

df <- structure(list(Col_1 = c(NA, 77L, 82L, 172L), Col_2 = c(NA, 79L,
                                                              NA, 135L), Col_3 = c(NA, 81L, NA, 131L), Col_4 = c(NA_integer_,
                                                                                                                 NA_integer_, NA_integer_, NA_integer_), Col_5 = c(NA, NA, NA,
                                                                                                                                                                   33L), Col_6 = c(NA, NA, NA, 104L), Col_7 = c(NA, NA, NA, 106L
                                                                                                                                                                   ), Col_8 = c(NA, NA, NA, 93L), Col_9 = c(NA, NA, NA, 50L), Col_10 = c(NA,
                                                                                                                                                                                                                                         NA, NA, 48L), Col_11 = c(NA, NA, NA, 96L), Col_12 = c(NA_integer_,
                                                                                                                                                                                                                                                                                               NA_integer_, NA_integer_, NA_integer_), Col_13 = c(NA_integer_,
                                                                                                                                                                                                                                                                                                                                                  NA_integer_, NA_integer_, NA_integer_), Col_14 = c(NA_integer_,
                                                                                                                                                                                                                                                                                                                                                                                                     NA_integer_, NA_integer_, NA_integer_), Col_15 = c(NA_integer_,
                                                                                                                                                                                                                                                                                                                                                                                                                                                        NA_integer_, NA_integer_, NA_integer_)), class = c("tbl_df",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           "tbl", "data.frame"), row.names = c(NA, -4L))
sample_mean <- function(r) {
  r <- unlist(r) %>% na.omit()
  count <- length(r)
  if (count > 3) {
    mean(sample(r, 3))
  } else if (count > 0 && count <= 3) {
    mean(r)
  } else {
    NA_real_
  }
}

split(df, seq_len(nrow(df))) %>%
  map_dbl(sample_mean) %>%
  data.frame(inflo_mean = .)
