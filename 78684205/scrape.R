library(RSelenium)

URL <- "https://www.immobiliare.it/vendita-case/belluno-provincia/?criterio=rilevanza"

driver <- remoteDriver(browserName = "chrome", port = 4444)

driver$open()

driver$navigate(URL)

Sys.sleep(5)

# Accept cookies & conditions.
#
accept <- tryCatch({
  suppressMessages(
    driver$findElement(using = "css selector", "#didomi-notice-agree-button")
  )
}, error = function(e) {
  NULL
})
if (!is.null(accept)) accept$clickElement()

while (TRUE) {
  # Scroll to bottom of main section.
  #
  main <- driver$findElement(using = "css selector", "main section")
  driver$executeScript("arguments[0].scrollTop = arguments[0].scrollHeight;", list(main))

  # Find link to next page.
  #
  paginate <- tryCatch({
    suppressMessages(
      driver$findElement(using = "css selector", "[data-cy='pagination-next'] a:first-child")
    )
  }, error = function(e) {
    NULL
  })
  if (is.null(paginate)) break
  URL <- paginate$getElementAttribute("href")[[1]]

  cat("Next page: ", URL, ".\n", sep = "")

  # Pause before advancing to next page.
  #
  Sys.sleep(15)
  driver$navigate(URL)
}

driver$close()
