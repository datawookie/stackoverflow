df1 <- structure(list(scientific_name = c("branta canadesis", "alopochen aegyptiaca",
                                          "anas platyrhychos", "cygnus olor", "buteo buteo"), common_name = c("canadian goose",
                                                                                                              "egyptian goose", "mallard", "mute swan", "common buzzard"),
                      geographic_area = c("western europe", "western europe", "western europe",
                                          "western europe", "western europe"), n_sampled = c(1L, 2L,
                                                                                             1L, 1L, 5L)), row.names = c(NA, 5L), class = "data.frame")

df2 <- structure(list(scientific_name = c("Accipiter albogularis", "Accipiter badius",
                                          "Accipiter bicolor", "Accipiter brachyurus", "Accipiter brevipes"
), Hand.Wing.Index = c(33.9, 32.9, 24.6, 31.7, 40.2), Habitat = c("Forest",
                                                                  "Shrubland", "Woodland", "Forest", "Forest"), Habitat.Density = c(1L,
                                                                                                                                    2L, 2L, 1L, 1L), Trophic.Level = c("Carnivore", "Carnivore",
                                                                                                                                                                       "Carnivore", "Carnivore", "Carnivore"), Trophic.Niche = c("Vertivore",
                                                                                                                                                                                                                                 "Vertivore", "Vertivore", "Vertivore", "Vertivore"), Primary.Lifestyle = c("Insessorial",
                                                                                                                                                                                                                                                                                                            "Insessorial", "Generalist", "Insessorial", "Generalist"), Migration = c(2L,
                                                                                                                                                                                                                                                                                                                                                                                     3L, 2L, 2L, 3L)), row.names = c(NA, 5L), class = "data.frame")

merge(df1, df2, by="scientific_name", all=T)

cbind(
  df1,
  df2
)

library(dplyr)
library(stringr)

merge(
  df1,
  df2 %>% mutate(scientific_name = str_to_lower(scientific_name)),
  by = "scientific_name",
  all = TRUE
)
