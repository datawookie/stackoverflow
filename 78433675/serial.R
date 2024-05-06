start.time <- Sys.time()

library(caret)
library(dplyr)

data(iris)
iris <- iris[c(ncol(iris), 1:(ncol(iris) - 1))]

set.seed(2000)
Train <- iris %>% group_by(Species) %>% sample_frac(.5, replace = FALSE)
Valid <- anti_join(iris, Train)

BAGFDA <- data.frame(Variable_Name1 = character(0), Variable_Name2 = character(0), Accuracy = numeric(0), Kappa = numeric(0))

set.seed(3000)
for(i in 2:(ncol(Train) - 1)) {
  for (j in (i + 1):ncol(Train)) {
    tryCatch({
      formula <- as.formula(paste("as.factor(Species) ~", names(Train)[i], "+", names(Train)[j]))
      bag <- caret::bagFDA(formula, data = Train)
      bag_predict <- predict(bag, newdata = Valid)
      bag_CM <- confusionMatrix(bag_predict, Valid$Species)
      iteration_results <- data.frame(
        Variable_Name1 = names(Train)[i],
        Variable_Name2 = names(Train)[j],
        Accuracy = bag_CM$overall["Accuracy"],
        Kappa = bag_CM$overall["Kappa"]
      )
      BAGFDA <- rbind(BAGFDA, iteration_results)
      print("Good")
    }, error = function(e) {
      cat("ERROR:", conditionMessage(e), "\n")
    })
  }
}
print(BAGFDA)
end.time <- Sys.time()
time.taken <- round(end.time - start.time,2)
time.taken
