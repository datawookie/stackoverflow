set.seed(123)
library(dplyr)
library(doParallel)
library(magrittr)
library(tidyr)

# - Create dummy data for example -|

# Large data frame - example
df <- data.frame(matrix(nrow=150000, ncol=20))
colnames(df) <- c('id', 'dateFrom', 'dateTo', paste0('v', seq.int(from = 1, to = 17)))
df$id <- seq.int(from = 1, to = nrow(df))
df$dateFrom <- sample(seq(from = as.Date('2024/01/01'), to = as.Date('2024/01/31'), by="day"), nrow(df), replace=T)
df$dateTo <- df$dateFrom + sample(c(0:7), nrow(df), replace=T)
df[, grepl('v', colnames(df))] <- rbinom(nrow(df) * 17, 1, 0.05)

# Data to merge
mrg <- data.frame(matrix(nrow=120, ncol=4))
colnames(mrg) <- c('v', 'actionDate', 'numerator', 'denominator')
mrg$v <- c(rep('v20_n', 30), rep('v21_n', 30), rep('v22_n', 30), rep('v23_n', 30))
mrg$actionDate <- rep(seq(from = as.Date('2024/01/01'), to = as.Date('2024/01/30'), by = "day"), 4)
mrg$denominator <- sample(80000:120000, 120)
mrg$numerator <- floor(mrg$denominator * runif(120, min = 0.01, max = 0.15))

new <- unique(mrg$v)
# -------------------------------- |


# Simulation

registerDoParallel(cores=8)

system.time(
  bootstrap <- foreach(x=1:32, .combine = rbind.data.frame, .packages = c('dplyr', 'magrittr', 'tidyr')) %dopar% {

    df_copy <- df

    for(ch in new) {

      sampling <- df %>%
        select(id, dateFrom, dateTo) %>%
        cross_join(mrg %>%
                     filter(v == ch) %>%
                     select(actionDate, numerator, denominator)
        ) %>%
        filter(actionDate >= dateFrom - 3 &
                 actionDate <= dateTo
        ) %>%
        group_by(id) %>%
        summarise(numer = sum(numerator),
                  denom = sum(denominator),
                  avg = numer/denom,
                  weight = avg * (denom / 150000 * 0.2),
                  chance = rbinom(1, 1, weight)
        ) %>%
        select(id, chance) %>%
        rename(!!ch := chance) %>%
        ungroup()

      df_copy <- df_copy %>%
        left_join(sampling, by = 'id')

    }

    df_copy <- df_copy %>%
      mutate_at(vars(contains("_n")), replace_na, 0)

    df_copy <- df_copy %>%
      group_by(across(c(-v1, -id, -dateFrom, -dateTo))) %>%
      dplyr::summarise(Occurrences = n(), Events = sum(v1)) %>%
      ungroup()
  }

) ## Eight cores - 40 seconds elapsed on laptop
stopImplicitCluster()
