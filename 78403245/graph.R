Droughts <- data.frame("site_id" = c(1,1,1,2,2,2,2,3,3),
                       "Drought_start" = c(1962,1970,1980,1960,1970,1978,1990,1965,1988),
                       "Drought_end" = c(1964,1975,1984,1964,1974,1980,1993,1980,1993))

library(ggplot2)

Droughts$site_id <- factor(paste("Site", Droughts$site_id))

ggplot(Droughts) +
  geom_segment(aes(x = 1950, xend = 2000, y = site_id), lwd = 10, col = "#00a2ff") +
  geom_segment(aes(x = Drought_start, xend = Drought_end, y = site_id), lwd = 10, col = "#ffff00") +
  scale_x_continuous(NULL) +
  scale_y_discrete(NULL, limits = rev(levels(Droughts$site_id))) +
  theme_minimal()
