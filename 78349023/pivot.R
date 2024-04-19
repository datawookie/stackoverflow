library(dplyr)
library(tidyr)

data <- read.csv(text = "
idno,sex,age_1,date_visit_1,height_in_cm_1,age_2,date_visit_2,height_in_cm_2,age_3,date_visit_3,height_in_cm_3
20,M,10,10/1/2010,100,11,10/1/2011,110,12,10/2/2012,115
21,F,11,10/2/2010,90,12,11/3/2011,100,13,12/5/2012,105
22,M,12,11/3/2010,100,13,12/4/2011,105,14,12/5/2012,110
")

data %>%
  mutate_all(as.character) %>%
  pivot_longer(cols = c(-idno, -sex)) %>%
  mutate(
    visit_no = sub(".*_", "", name),
    name = sub("_[0-9]$", "", name)
  ) %>%
  pivot_wider(
    names_from = name,
    values_from = value
  )
