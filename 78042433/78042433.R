df3=structure(list(Scenario = c("Basic", "Basic", "Basic", "Basic", "Basic"
), Rating = c("1C", "2A", "2B", "2C", "3A"), Class = c("CORP",
                                                       "CORP", "CORP", "CORP", "RETAIL"), wePD1 = c(0.51,
                                                                                                    0.41, 0.58, 0.28,
                                                                                                    0.68), wePD2 = c(0.74, 0.01,
                                                                                                                     0.28, 0.92, 0.48
                                                                                                    ), wePD3 = c(0.43, 0.23, 0.04,
                                                                                                                 0.62, 0.71), eePD1 = c(NA, 0.37,
                                                                                                                                        0.96, 0.22, NA
                                                                                                                 ), eePD2 = c(NA, 0.06, 0.29, 0.22,
                                                                                                                              NA), eePD3 = c(NA, 0.81, 0.85,
                                                                                                                                             0.78, NA)), row.names = c(NA,
                                                                                                                                                                       -5L), class = c("data.table", "data.frame"))
colnames(df3)

df3$eePD1 <- ifelse(is.na(df3$eePD1) & df3$Class == "CORP", df3$wePD1, df3$eePD1)
df3$eePD2 <- ifelse(is.na(df3$eePD2) & df3$Class == "CORP", df3$wePD2, df3$eePD2)
df3$eePD3 <- ifelse(is.na(df3$eePD3) & df3$Class == "CORP", df3$wePD3, df3$eePD3)

for (target in grep("ee", colnames(df3), value=TRUE)) {
  source <- sub("^ee", "we", target)
  df3[[target]] <- ifelse(
    is.na(df3[[target]]) & df3$Class == "CORP",
    df3[[source]],
    df3[[target]]
  )
}
