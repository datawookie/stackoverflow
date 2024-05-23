library(dplyr)
library(ggplot2)
library(ecotox)

df <- ecotox::lamprey_tox

lc <- function(data, dose='dose', months=c(), month='month', total='total', response='response') {
  data <- data%>% filter(month %in% c(months))

  myplots <- list()

  for (i in seq_along(months)){
    print(paste("Plotting data for", months[i]))
    a <- data[data$month %in% months[i],]

    lc <- LC_probit(
      (response/ total) ~ log10(as.numeric(dose)), p = c(50, 90),
      weights = total,
      data =a
    )
    LC50 <- lc$dose[1]
    LC90 <- lc$dose[2]

    myplots[[i]] <- ggplot(
      data=a,
      aes(x=log10(as.numeric(dose)),y=(response/total))
    )+
      geom_point(size=4)+
      geom_smooth(
        method="glm",
        method.args=list(family=binomial(link="probit")),
        aes(weight=total),colour="blue",se=TRUE, level=0.95
      ) +
      geom_segment(aes(x = log10(LC50), xend = log10(LC50), y=-Inf, yend=0.5), linetype='dashed', size=1) +
      geom_segment(aes(x = -Inf, xend = log10(LC50), y=0.5, yend=0.5), linetype='dashed', size=1) +
      geom_segment(aes(x = log10(LC90), xend = log10(LC90), y=-Inf, yend=0.9), linetype='dashed', size=1) +
      geom_segment(aes(x = -Inf, xend = log10(LC90), y=0.9, yend=0.9), linetype='dashed', size=1)
  }

  myplots
}

lc(df, months=c('May', 'June', 'August'))
