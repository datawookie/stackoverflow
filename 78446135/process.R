library(dplyr)
library(purrr)

input <- data.frame(
  id = c(1, 1, 2, 1),
  val1 = c(NA, "world", "good", NA),
  val2 = c(NA, NA, "morning", "spark"),
  val3 = c("hello", NA, "spark", NA)
)

# dummy list
list_outcome <- list()

# Get the columnnames to loop over

loop_var <- colnames(input)[2:4]

for(i in loop_var){
  nr <- input %>% group_by(id) %>% filter(!is.na(.data[[i]])) %>% select(id, all_of(i))
  # Save every iteration in the loop as the ith element of the list
  list_outcome[[i]] <- nr
}

# merge the elements within list by Reduce function, uses common variable name within the list on which the merge will take place

Reduce(merge, list_outcome)

input %>% summarize(across(everything(), ~ first(na.omit(.))), .by=id)

lapply(input, na.omit) %>% data.frame()

input %>%
  group_by(id) %>%
  map(print)
