library(rvest)
library(httr)

url <- 'https://www.anbima.com.br/informacoes/est-termo/CZ-down.asp'

form_data <- list(
  'escolha' = '2',
  'Idioma' = 'PT',
  'saida' = 'xls',
  'Dt_Ref_Ver' = '20240607',
  'Dt_Ref' = '14/06/2024'
)

headers <- c(
  'User-Agent' = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
)

response <- POST(url, body = form_data, add_headers(headers))

if (status_code(response) == 200) {
  writeBin(content(response, "raw"), "download.xls")
} else {
  cat("Failed to submit form. Status code:", httr::status_code(response), "\n")
  cat(content(response, "text"))
}
