t1 <- structure(c(`30` = 3L, `40` = 3L, `45` = 2L, `60` = 5L, `65` = 1L,
                  `70` = 2L, `75` = 1L, `78` = 1L, `80` = 1L, `90` = 5L, `95` = 1L,
                  `100` = 1L, `101` = 1L, `120` = 3L, `144` = 1L, `150` = 1L, `180` = 1L,
                  `185` = 1L, `240` = 2L), dim = 19L, dimnames = list(c("30", "40",
                                                                        "45", "60", "65", "70", "75", "78", "80", "90", "95", "100",
                                                                        "101", "120", "144", "150", "180", "185", "240")), class = "table")

t2 <- structure(c(`2` = 2L, `10` = 2L, `15` = 1L, `20` = 2L, `30` = 3L,
                  `38` = 1L, `40` = 4L, `45` = 4L, `50` = 3L, `55` = 2L, `60` = 11L,
                  `70` = 1L, `72` = 1L, `73` = 1L, `75` = 1L, `80` = 2L, `90` = 10L,
                  `95` = 1L, `100` = 1L, `105` = 1L, `110` = 1L, `120` = 11L, `130` = 2L,
                  `150` = 2L, `180` = 5L, `200` = 1L, `240` = 3L, `300` = 3L, `500` = 1L
), dim = 29L, dimnames = structure(list(c("2", "10", "15", "20",
                                          "30", "38", "40", "45", "50", "55", "60", "70", "72", "73", "75",
                                          "80", "90", "95", "100", "105", "110", "120", "130", "150", "180",
                                          "200", "240", "300", "500")), names = ""), class = "table")

t1

library(dplyr)
library(ggplot2)

counts <- rbind(
  data.frame(t1) %>% mutate(gender = "F"),
  data.frame(t2) %>% mutate(gender = "M")
) %>%
  rename(
    duration = Var1,
    frequency = Freq
  ) %>%
  mutate(
    duration = as.integer(duration)
  )

ggplot(counts) +
  geom_point(aes(x = duration, y = frequency, col = gender)) +
  labs(x = "X", y = "Y", title = "Female and Male task duration") +
  theme_minimal() +
  scale_colour_manual(values = c("blue", "red"))
