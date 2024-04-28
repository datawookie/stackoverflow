spec.tgarch <- ugarchspec(
  variance.model = list(
    model = "fGARCH",
    submodel = "TGARCH",
    garchOrder = c(1,1)
  ),
  mean.model = list(armaOrder=c(1,0))
)
tGarchModel <- ugarchfit(spec.tgarch, data=dl_data)
tGarchModel

plt <- plot(
  dl_data,
  col = "darkgrey",
  xlab="",
  ylab="",
  main="Threshold GARCH Volatility",
  grid.col = "lightgrey"
)
plt <- addSeries(sigma(tGarchModel), col = "red", on = 1)
plt <- addSeries(-sigma(tGarchModel), col = "red", on = 1)
plt


# vol <- ts(tGarchModel@fit$sigma^2,end = c(2024,1), frequency = 12)
# plot(vol, xlab="", ylab="", main="Threshold GARCH Volatility")
#
# plot(ts_data, type = "l", col = "blue", ylab = "Price", xlab = "Time", main = "Comparison of Actual Volatility vs Model Predicted Volatility")
# lines(vol, col = "red")
#
# # Add a legend
# legend("topright", legend = c("Actual Volatility", "Model Predicted Volatility"), col = c("blue", "red"), lty = 1)
