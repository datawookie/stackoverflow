library(dplyr)

NBUS <- 10

buses <- data.frame(
  id = seq(NBUS),
  active = FALSE,
  broken = FALSE,
  pbreakdown = 0.5
)

buses$active[1:5] <- TRUE

day <- 0
#
while (TRUE) {
  day <- day + 1
  cat(paste("* DAY", day, "===\n\n"))

  # Sample which buses break down.
  #
  active <- buses %>%
    filter(active) %>%
    mutate(
      random = runif(nrow(.)),
      broken = random < pbreakdown,
      pbreakdown = pbreakdown - ifelse(broken, 0, 0.01)
    )

  print(active)

  buses <- rbind(
    active %>% select(-random),
    buses %>% filter(!active)
  )

  # Set broken buses as inactive.
  #
  buses <- buses %>%
    mutate(
      active = active &! broken
    ) %>%
    arrange(broken)

  # Activate more buses.
  #
  buses <- buses %>%
    mutate(
      active = row_number() <= 5 & !broken
    )

  nactive <- sum(buses$active)

  cat(paste("Number of active buses:", nactive, "\n"))

  if (nactive == 0) break
}
