library(rvest)
library(dplyr)

url <- "https://www.immobiliare.it/search-list/?idContratto=1&idCategoria=1&idTipologia%5B0%5D=7&idTipologia%5B1%5D=12&idTipologia%5B2%5D=13&idTipologia%5B3%5D=11&criterio=rilevanza&__lang=it&fkRegione=ven&idProvincia=VE&idNazione=IT&pag=1&dtCookie=v_4_srv_3_sn_9E341BF8AC6892004B9D2502432FB6E5_perc_100000_ol_0_mul_1_app-3Aea7c4b59f27d43eb_0"

# Create a live session.
session <- read_html_live(url)

# Pop up browser window showing live site.
session$view()

# Extract the price of the first listing.
session %>% html_element("div.in-listingCardPrice")
