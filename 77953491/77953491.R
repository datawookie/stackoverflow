library(tidyverse)
library(rvest)
library(httr2)

# timestamp helper
timestamp_ <- \() sprintf("%.0f", as.numeric(Sys.time()) * 1000)

# Web scrape the main page
link = "https://puc.overheid.nl/rsj/wettelijkkader/pagina/G/-/gdlv/1/"

page = read_html(link)

# Get link of all sub pages
sub_pages <- page %>% 
  html_nodes(".paging") %>%
  html_nodes("a") %>%
  html_attr("href")

# Change to right link and Get every nth link (there a dups)
links_subpages <- paste0("https://puc.overheid.nl", sub_pages)

links <- links_subpages[1] %>%
  read_html() %>%
  html_nodes(".search_result") %>%
  html_nodes("a") %>%
  html_attr("href")

# correct url link
links <- paste0("https://puc.overheid.nl", links[seq(1, length(links), 2)])

onclick <- links[1] %>%
  read_html() %>%
  html_nodes(".download-als a") %>%
  html_attr("onclick") 

(req_param <- str_extract_all(onclick, "(?<=')[^\\s']+(?=')")[[1]])
#> [1] "PUC_750817_21_1" "rsj"             "pdf"

# submit request / get ticket ---------------------------------------------
ticket <- 
  request("https://puc.overheid.nl/PUC/Handlers/ManifestatieService.ashx") %>% 
  req_url_query(actie      = "maakmanifestatie",
                kanaal     = req_param[2],
                identifier = req_param[1],
                soort      = req_param[3],
                `_`        = timestamp_()) %>% 
  req_perform() %>% 
  resp_body_json(check_type = FALSE)

jsonlite::toJSON(ticket, auto_unbox = TRUE,  pretty = TRUE)
#> {
#>   "ticket": "3c4826c1-6949-4c0f-b476-d252c4713b37"
#> }

Sys.sleep(5)
pdf_url <- 
  request("https://puc.overheid.nl/PUC/Handlers/ManifestatieService.ashx") %>% 
  req_url_query(actie      = "haalstatus",
                ticket     = ticket$ticket,
                `_`        = timestamp_()) %>% 
  req_perform() %>% 
  resp_body_json(check_type = FALSE)

jsonlite::toJSON(pdf_url, auto_unbox = TRUE,  pretty = TRUE)
#> {
#>   "result": {
#>     "status": "available",
#>     "url": "/puc-opendata/request-result/3c4826c1-6949-4c0f-b476-d252c4713b37/RSJ%2023%2F31577%2FGA%2012%20december%202023%20beroep.pdf",
#>     "filename": "RSJ 23/31577/GA 12 december 2023 beroep.pdf"
#>   }
#> }

# download pdf ------------------------------------------------------------
request("https://puc.overheid.nl/PUC/Handlers/ManifestatieService.ashx") %>% 
  req_url_query(actie = "download",
                identifier = req_param[1],
                url = pdf_url$result$url,
                filename = pdf_url$result$filename) %>% 
  req_perform(path = pdf_url$result$filename %>% gsub("[ /]", "-", .))
#> Error:
#> ! Failed to open file RSJ 23/31577/GA 12 december 2023 beroep.pdf.
#> Backtrace:
#>     ▆
#>  1. ├─... %>% req_perform(path = pdf_url$result$filename)
#>  2. └─httr2::req_perform(., path = pdf_url$result$filename)
#>  3.   └─base::tryCatch(...)
#>  4.     └─base (local) tryCatchList(expr, classes, parentenv, handlers)
#>  5.       └─base (local) tryCatchOne(expr, names, parentenv, handlers[[1L]])
#>  6.         └─value[[3L]](cond)