library(dplyr)
library(ggplot2)

N <- 50

df <- data.frame(
  mean = rnorm(N)
) %>% mutate(
  lower = mean - 1,
  upper = mean + 1,
  t = row_number()
)

# =============================================================================

# Add columns that indicate whether the confidence intervals includes or
# excludes zero.

df <- df %>% mutate(
  include = lower < 0 & upper > 0,
  exclude = !include
)

# =============================================================================

ggplot(df, aes(x = t, y = mean)) +
  geom_ribbon(aes(ymin = lower, ymax = upper), fill = "lightgrey") +
  geom_point(aes(col = exclude))
