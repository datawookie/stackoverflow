library(tidyr)
library(dplyr)

t1 <- tibble::tribble(
  ~row_labels,         ~"#Total", ~"Dept 1", ~"Dept 2", ~"Dept 3", ~"Dept 4",
  "c3|Mean",           21.2,      21.6,    16,      33.5,    26.7,
  "c3|Median",         17.5,      16,      16,      33.5,    22,
  "c3|75th Perc.75%",  27.8,      33.5,    19,      45,      45,
  "c3|Valid N",        6,         5,       2,       2,       3
)

t1 %>%
  # Transpose data frame.
  pivot_longer(names_to = "col", values_to = "value", cols = !row_labels) %>%
  pivot_wider(names_from = row_labels, values_from = value) %>%
  # Apply logic.
  mutate(
    `c3|Mean` = ifelse(`c3|Valid N` <= 4, NA, `c3|Mean`),
    `c3|Median` = ifelse(`c3|Valid N` <= 4, NA, `c3|Median`),
    `c3|75th Perc.75%` = ifelse(`c3|Valid N` <= 5, NA, `c3|75th Perc.75%`),
  ) %>%
  # Transpose back again.
  pivot_longer(names_to = "row_labels", values_to = "value", cols = !col) %>%
  # Replace NA with "--".
  mutate(value = ifelse(is.na(value), "--", value)) %>%
  pivot_wider(names_from = col, values_from = value)
