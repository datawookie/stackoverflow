library(mlrMBO)

set.seed(13)

x <- seq(0, 10, 0.1)
s <- sin(0.5 * x + 5) / -1
sn <- s + rnorm(length(s), sd = 0.3)

plot(sn, t="l", col=8,lty=2)
lines(s, col=4)
points(which.min(s), min(s), lwd=5 , col=4)

# SMOOTHE ----------------------------------------------------------------------

smoothed <- lowess(x, sn, f = 0.3)
lines(smoothed$y, col = "blue")

# OPTIMISE ---------------------------------------------------------------------

fit <- function(i) smoothed$y[ round(i,0) ]

obj.fun = makeSingleObjectiveFunction(
  name = "noisy_fu",
  fn = fit,
  has.simple.signature = TRUE,
  par.set = makeNumericParamSet(
    "i",
    len = 1,
    lower = 1,
    upper = length(sn)
  ),
  noisy = TRUE
)

ctrl = makeMBOControl(final.method = "best.predicted", final.evals = 10)
ctrl = setMBOControlInfill(ctrl, crit = crit.eqi)
ctrl = setMBOControlTermination(ctrl, iters = 10)

configureMlr(on.learner.warning = "quiet", show.learner.output = FALSE)
res = mbo(obj.fun, control = ctrl, show.info = T)

points(res$x, res$y, lwd=5 , col=3)

# PLOT -------------------------------------------------------------------------

fit <- function(i) sn[ round(i,0) ]

x <- seq(1, 101, 0.01)
y <- fit(x)

plot(x, y, type = "l", xlab = "Index")
