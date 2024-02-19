library(dplyr)
library(tidyr)

data <- read.table(header = TRUE, text = "
  Factors       Group       n     Average     Max      Min
  Calcium       Above       1599  0.412       42.872   0.017
  Calcium       Below       1040  0.011       0.017    -0.01
  Lead          Above       1345  1.312       0.043    0.037
  Lead          Below       882   0.614       64.65    0.065
")

data %>%
  rename(Factor = Factors) %>%
  group_by(Factor) %>%
  mutate(
    n = sprintf("%d (%.1f%%)", n, n / sum(n) * 100),
    "Max,Min" = paste(Max, Min, sep = ","),
    Average = as.character(Average)
  ) %>%
  select(-Max, -Min) %>%
  pivot_longer(n:last_col()) %>%
  pivot_wider(names_from = Group, values_from = value)
