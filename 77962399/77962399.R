library(dplyr)

rw.data <- tribble(
  ~fiveac, ~fiveem,
  "A", 1,
  "B", 2,
  "C", 3
)

rw.data %>%
  mutate(
    new_column = paste(fiveac, fiveem)
  )

rw.data %>%
  transmute(
    new_column = paste(fiveac, fiveem)
  )

library(tidyr)

rw.data %>%
  unite(
    "new_column",
    fiveac:fiveem,
    remove = FALSE
  )
