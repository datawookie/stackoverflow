// [[Rcpp::depends(rstan)]]
#include <stan/math.hpp>
#include <iostream>
// [[Rcpp::depends(RcppArmadillo)]]
// [[Rcpp::plugins(cpp14)]]
// [[Rcpp::export]]
int simple() {
  std::cout << "log normal(1 | 2, 3)="
            << stan::math::normal_log(1, 2, 5)
            << std::endl;
  return 0;
}
