# Data from https://www.kaggle.com/datasets/ronaldonyango/global-suicide-rates-1990-to-2022.

library(dplyr)

Death <- read.csv("suicide_rates_1990-2022.csv")

# Remove outright duplicates.
#
Death <- Death %>% distinct()

Death <- Death %>%
  group_by(
    RegionName,
    CountryName,
    Year,
    Sex,
    AgeGroup,
    Population,
    GDP,
    GDPPerCapita,
    GrossNationalIncome,
    GNIPerCapita,
    InflationRate,
    EmploymentPopulationRatio
  ) %>%
  summarise(
    SuicideCount = mean(SuicideCount),
    CauseSpecificDeathPercentage = mean(CauseSpecificDeathPercentage),
    DeathRatePer100K = mean(DeathRatePer100K),
    CauseSpecificDeathPercentage = mean(CauseSpecificDeathPercentage),
    .groups = "drop"
  )

Death %>%
  filter(
    CountryName == "United States of America",
    AgeGroup == "25-34 years",
    Year == 2020,
    Sex == "Male"
  ) %>%
  nrow()
