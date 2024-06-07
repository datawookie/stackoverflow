library(httr)
library(jsonlite)
library(tidyr)

URL = "https://apims.doe.gov.my/data/public_v2/CAQM/last24hours.json"


res <- httr::GET(url = URL)

# Get table as matrix.
table <- fromJSON(content(res, as = "text"))[["24hour_api_apims"]]
# Convert to data frame.
table <- data.frame(table[-1,]) |>
  setNames(table[1,])

# Data should all be there... but it would be better to have it in long format.

pivot_longer(table, c(-"State", -"Location"), names_to = "time")
