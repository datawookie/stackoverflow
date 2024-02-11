library(tidyquant)

TradingStrategy <- function(mktdata, mavga_period, mavgb_period) {
  returns <- c(NA, diff(log(mktdata$Close)))

  mavga <- SMA(mktdata$Close, mavga_period)
  mavgb <- SMA(mktdata$Close, mavgb_period)

  signal <- mavga / mavgb
  signal <- ifelse(is.na(signal), 0, ifelse(signal > 1, 1, -1))

  data.frame(return = signal * returns)
}

data <- tribble(
  ~Close,
  50,
  51,
  52,
  59,
  54,
  49,
  50,
  50,
  40,
  45,
  46,
  50,
  51,
  52,
  59,
  54,
  49,
  50,
  50,
  40,
  45,
  46
)

TradingStrategy(data, 1, 5)
