# Principal.
P = 50000
# Number of payments.
n = 30 * 12
# Payment amount.
A = 1000

amortization <- function(r, A, P, n) {
  A - (P * r * (1 + r)^n) / ((1 + r)^n - 1)
}

# Solve for monthly interest rate.
#
result <- uniroot(amortization, lower = 0.01, upper = 0.05, A = A, P = P, n = n)
result$root

repayments <- seq(600, 2000, 100)

rates <- sapply(
  repayments,
  function(A) {
    uniroot(amortization, lower = 0.01, upper = 0.05, A = A, P = P, n = n)$root
  }
)

data <- data.frame(repayments, rates)

library(ggplot2)

ggplot(data, aes(x = repayments, y = rates)) + geom_line()
