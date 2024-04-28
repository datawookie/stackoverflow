# Test data ====================================================================

ID <- seq(100)

pbp_2020_novbid <- data.frame(bid_id = sample(ID, 5, replace = TRUE))
pbp_2020_vbid_nodup <- data.frame(bid_id = sample(ID, 7, replace = TRUE))
pbp_2020_total <- data.frame(bid_id = sample(ID, 5, replace = TRUE))
pbp_2021_novbid <- data.frame(bid_id = sample(ID, 9, replace = TRUE))
pbp_2021_vbid_nodup <- data.frame(bid_id = sample(ID, 5, replace = TRUE))
pbp_2021_total <- data.frame(bid_id = sample(ID, 11, replace = TRUE))
pbp_2022_novbid <- data.frame(bid_id = sample(ID, 13, replace = TRUE))
pbp_2022_vbid_nodup <- data.frame(bid_id = sample(ID, 3, replace = TRUE))
pbp_2022_total <- data.frame(bid_id = sample(ID, 5, replace = TRUE))
pbp_2023_novbid <- data.frame(bid_id = sample(ID, 12, replace = TRUE))
pbp_2023_vbid_nodup <- data.frame(bid_id = sample(ID, 9, replace = TRUE))
pbp_2023_total <- data.frame(bid_id = sample(ID, 5, replace = TRUE))

# ==============================================================================

Year <- c(rep(2020:2023, each=3))

VBID <- c(rep(c("novbid", "vbid_nodup", "total"), time=4))

# Total_plan_number <- c(length(unique(pbp_2020_novbid$bid_id)), length(unique(pbp_2020_vbid_nodup$bid_id)), length(unique(pbp_2020_total$bid_id)),length(unique(pbp_2021_novbid$bid_id)), length(unique(pbp_2021_vbid_nodup$bid_id)), length(unique(pbp_2021_total$bid_id)),length(unique(pbp_2022_novbid$bid_id)), length(unique(pbp_2022_vbid_nodup$bid_id)), length(unique(pbp_2022_total$bid_id)),length(unique(pbp_2023_novbid$bid_id)), length(unique(pbp_2023_vbid_nodup$bid_id)), length(unique(pbp_2023_total$bid_id)))
# df <- data.frame(Year, VBID, Total_plan_number)

library(dplyr)

data.frame(Year, VBID) %>%
  mutate(
    Total_plan_number = sapply(
      paste("pbp", Year, VBID, sep = "_"),
      function(name) {
        length(unique(get(name)$bid_id))
      }
    )
  )
