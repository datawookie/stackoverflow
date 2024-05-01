library(dplyr)

numbers <- c(1, 5, 7)
all_combinations <- data.frame(expand.grid(rep(list(numbers), 6)))

all_combinations %>%
  mutate(
    starts_with_1 = ifelse(Var1 == 1, "yes", "no"),
    numbers_ascending = apply(., 1, function(x) all(diff(as.numeric(x)) >= 0)),
    numbers_ascending = ifelse(numbers_ascending , "yes", "no"),
    at_least_two_ones = apply(., 1, function(x) sum(x == 1) >= 2),
    at_least_two_ones = ifelse(at_least_two_ones, "yes", "no")
  ) %>%
  filter(
    starts_with_1 == "yes",
    numbers_ascending == "yes",
    at_least_two_ones == "yes"
  )

all_combinations %>%
  mutate(
    numbers_ascending = apply(., 1, function(x) all(diff(as.numeric(x)) >= 0)),
    at_least_two_ones = apply(., 1, function(x) sum(x == 1) >= 2)
  ) %>%
  filter(
    Var1 == 1,
    numbers_ascending,
    at_least_two_ones
  )
