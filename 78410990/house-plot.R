library(rddtools)

data(house)

house_rdd = rdd_data(x=x, y=y, data=house, cutpoint=0)
plot(house_rdd, ylim=c(0,1))

par(new=TRUE)

reg_para0 = rdd_reg_lm(rdd_object=house_rdd, slope =("same"))
plot(reg_para0, ylim=c(0,1), axes = FALSE, xlab = "", ylab = "")
