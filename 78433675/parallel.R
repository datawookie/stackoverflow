start.time <- Sys.time()

library(foreach)
library(doParallel)
library(caret)
library(dplyr)

data(iris)
iris <- iris[c(ncol(iris), 1:(ncol(iris) - 1))]

cores = parallel::detectCores() - 1
cluster = parallel::makeCluster(cores, type = "PSOCK")
doParallel::registerDoParallel(cluster)
if (!foreach::getDoParRegistered()) {
  print("ERROR")
}
print(foreach::getDoParWorkers())

set.seed(2000)
Train <- iris %>% group_by(Species) %>% sample_frac(.5, replace = FALSE)
Valid <- anti_join(iris, Train)

BAGFDA <- data.frame(Variable_Name1 = character(0), Variable_Name2 = character(0), Accuracy = numeric(0), Kappa = numeric(0))

set.seed(1001)
results <- foreach(i = 2:(ncol(Train) - 1), .combine=rbind) %:%
  foreach (j = (i + 1):ncol(Train), .combine=rbind) %dopar% {
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
    }, error = function(e) {
      cat("ERROR:", conditionMessage(e), "\n")
    })
    iteration_results
  }
results


results <- foreach(i = 2:(ncol(Train) - 1), .combine=rbind) %:%
  foreach (j = (i + 1):ncol(Train), .combine=rbind, .packages = c("caret")) %dopar% {
    tryCatch({
      formula <- as.formula(paste("Species ~", names(Train)[i], "+", names(Train)[j]))
      bag <- caret::bagFDA(formula, data = Train)
      bag_predict <- predict(bag, newdata = Valid)
      bag_CM <- confusionMatrix(bag_predict, Valid$Species)

      data.frame(
        Variable_Name1 = names(Train)[i],
        Variable_Name2 = names(Train)[j],
        Accuracy = bag_CM$overall["Accuracy"],
        Kappa = bag_CM$overall["Kappa"]
      )
    }, error = function(e) {
      cat("ERROR:", conditionMessage(e), "\n")
    })
  }
results

set.seed(1001)
foreach(i = 2:(ncol(Train) - 1)) %:%
  foreach (j = (i + 1):ncol(Train), .packages = c("caret")) %dopar% {
    runif(3)
  }

print(BAGFDA)
stopCluster(cluster)
end.time <- Sys.time()
time.taken <- round(end.time - start.time,2)
time.taken
