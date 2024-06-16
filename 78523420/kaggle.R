library(httr)
library(jsonlite)
library(purrr)

cookies = c(
  `ka_sessionid` = "451fd57b37420ec1e12752f641751e2c",
  `_ga_T7QHS60L4Q` = "GS1.1.1716874446.3.1.1716874528.0.0.0",
  `_ga` = "GA1.1.1156449516.1714279309",
  `ACCEPTED_COOKIES` = "true",
  `CSRF-TOKEN` = "CfDJ8C7919k9hp5Hq9pDr-pvzJo0YoYVuV4B8-HYu6l9DnUX_uPn4qcLLK8m5PnvCISNjVgET2285U7zYIDuYkQv3WcFmjJZhSESVZRJ8B3tDA",
  `XSRF-TOKEN` = "CfDJ8C7919k9hp5Hq9pDr-pvzJr-goMjc10reHohzKZi-G6mMTNKK0QN8Cu67RdutzyEBz-qvio9YH4oqvDaCzXTj9kRnHqt669dlbSC4IEJAdnveA",
  `CLIENT-TOKEN` = "eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc3MiOiJrYWdnbGUiLCJhdWQiOiJjbGllbnQiLCJzdWIiOiIiLCJuYnQiOiIyMDI0LTA1LTI4VDA1OjM1OjI3LjcyNDk3MDlaIiwiaWF0IjoiMjAyNC0wNS0yOFQwNTozNToyNy43MjQ5NzA5WiIsImp0aSI6ImFhZjI0NjlhLTA2YmUtNGQxOC1iMDNkLWJjYzEwN2VkYjY2MiIsImV4cCI6IjIwMjQtMDYtMjhUMDU6MzU6MjcuNzI0OTcwOVoiLCJhbm9uIjp0cnVlLCJmZiI6WyJLZXJuZWxzR2l0aHViU3luYyIsIkltcG9ydEtlcm5lbHNGcm9tQ29sYWIiLCJLZXJuZWxzRXhwb3J0TWV0YWRhdGEiLCJLZXJuZWxzRmlyZWJhc2VMb25nUG9sbGluZyIsIkNvbW11bml0eUxvd2VySGVhZGVyU2l6ZXMiLCJBbGxvd0ZvcnVtQXR0YWNobWVudHMiLCJGcm9udGVuZEVycm9yUmVwb3J0aW5nIiwiRGF0YXNldHNNYW5hZ2VkRm9jdXNPbk9wZW4iLCJDaGFuZ2VEYXRhc2V0T3duZXJzaGlwVG9PcmciLCJFeHBvcnREYXRhc2V0QXNDcm9pc3NhbnQiLCJNb2RlbHNDYWNoZWRUYWdTZXJ2aWNlRW5hYmxlZCIsIkRpc2N1c3Npb25zUmVhY3Rpb25zIiwiRGF0YXNldFVwbG9hZGVyRHVwbGljYXRlRGV0ZWN0aW9uIiwiRGF0YXNldHNMbG1GZWVkYmFja0NoaXAiLCJEYXRhc2V0c01ldGFkYXRhU3VnZ2VzdGlvbnMiLCJNb2RlbHNCb29rbWFya2luZyIsIlBpbm5lZFdvcmsiLCJNZXRhc3RvcmVDaGVja0FnZ3JlZ2F0ZUZpbGVIYXNoZXMiLCJDb21wZXRpdGlvbnNUYWJPbk1vZGVsUGFnZSIsIkhpZGVPbGRHZW5haVRPVSJdLCJmZmQiOnsiS2VybmVsRWRpdG9yQXV0b3NhdmVUaHJvdHRsZU1zIjoiMzAwMDAiLCJFbWVyZ2VuY3lBbGVydEJhbm5lciI6Int9IiwiQ2xpZW50UnBjUmF0ZUxpbWl0UXBzIjoiNDAiLCJDbGllbnRScGNSYXRlTGltaXRRcG0iOiI1MDAiLCJGZWF0dXJlZENvbW11bml0eUNvbXBldGl0aW9ucyI6IjYwMDk1LDU0MDAwLDU3MTYzIiwiQWRkRmVhdHVyZUZsYWdzVG9QYWdlTG9hZFRhZyI6ImRpc2FibGVkIiwiTW9kZWxJZHNBbGxvd0luZmVyZW5jZSI6IjMzMDEsMzUzMyIsIk1vZGVsSW5mZXJlbmNlUGFyYW1ldGVycyI6InsgXCJtYXhfdG9rZW5zXCI6IDEyOCwgXCJ0ZW1wZXJhdHVyZVwiOiAwLjQsIFwidG9wX2tcIjogNSB9IiwiU2ltQ29tcGV0aXRpb25JZHNUb0lnbm9yZVVwbG9hZExpbWl0IjoiNjAyNDMsNjEyNTAsNjEyNDciLCJDb21wZXRpdGlvbk1ldHJpY1RpbWVvdXRNaW51dGVzIjoiMzAiLCJUZkh1YkthZ2dsZUFubm91bmNlbWVudFVybCI6Ii9kaXNjdXNzaW9ucy9wcm9kdWN0LWZlZWRiYWNrLzQ0ODQyNSJ9LCJwaWQiOiJrYWdnbGUtMTYxNjA3Iiwic3ZjIjoid2ViLWZlIiwic2RhayI6IkFJemFTeUE0ZU5xVWRSUnNrSnNDWldWei1xTDY1NVhhNUpFTXJlRSIsImJsZCI6ImNlYjVjNTAxZGE5NGNlZWM4NTUyMjg4MjdhZWNmZjgzNjdiMTc3N2QifQ.",
  `recaptcha-ca-t` = "AaGzOmd8gDEwvpH-HAFi7d5WTB0YDnhu2W8JlMlQbzwISn-vre6A1QV3ysbcnyz4tou6PktDIZWHqMYf3Kig8-SOcjbVIHrlUbIzTMWcrHMxYVKW--oDMY0TwxAQAgrZ88Xeqd4BkVWfsRs:U=bc304e08a0000000"
)

headers = c(
  `User-Agent` = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
  `Accept` = "application/json",
  `Accept-Language` = "en-US,en;q=0.5",
  `Accept-Encoding` = "gzip, deflate, br",
  `content-type` = "application/json",
  `x-xsrf-token` = "CfDJ8C7919k9hp5Hq9pDr-pvzJr-goMjc10reHohzKZi-G6mMTNKK0QN8Cu67RdutzyEBz-qvio9YH4oqvDaCzXTj9kRnHqt669dlbSC4IEJAdnveA"
)

data = '{"verificationInfo":{"datasetId":2231405,"databundleVersionId":3786453},"firestorePath":"pIMnn9p2Sky87SJGFYyL/versions/6lHzXXVZfin9SfHfmEqP/files/sales_dataset.csv","tableQuery":{"skip":0,"take":225,"filter":{"constantFilter":{"value":true}},"selectedColumns":[],"sorts":[]}}'

res <- httr::POST(
  url = "https://www.kaggle.com/api/i/datasets.DatasetService/GetDataViewExternal",
  httr::add_headers(.headers=headers),
  httr::set_cookies(.cookies = cookies),
  body = data
)

table <- content(res)$dataView$dataTable$rows |>
  map(function(row) {
    data.frame(row$text) %>%
      setNames(c("budget", "sales"))
  }) |>
  list_rbind()
