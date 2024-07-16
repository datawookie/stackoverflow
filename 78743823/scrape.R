# library(httr)
# library(rvest)
# 
# cookies = c(
#   `ASP.NET_SessionId` = "4darg2wqzgyyldwileqxnmzg"
# )
# 
# headers = c(
#   `User-Agent` = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0"
# )
# 
# response <- httr::GET(
#   url = "https://fcainfoweb.nic.in/reports/Report_daily1_web_Statewise.aspx",
#   httr::add_headers(.headers=headers),
#   httr::set_cookies(.cookies = cookies)
# )
# 
# data <- content(response) |>
#   html_node("table") %>%
#   html_table()
# 
# head(data)

library(httr)

cookies = c(
  `ASP.NET_SessionId` = "4darg2wqzgyyldwileqxnmzg"
)

headers = c(
  `User-Agent` = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0"
)

data = list(
  `ctl00_MainContent_ToolkitScriptManager1_HiddenField` = ";;AjaxControlToolkit, Version=4.1.51116.0, Culture=neutral, PublicKeyToken=28f01b0e84b6d53e:en-US:fd384f95-1b49-47cf-9b47-2fa2a921a36a:475a4ef5:addc6819:5546a2b:d2e10b12:effe2a26:37e2e5c9:5a682656:c7029a2:e9e598a9",
  # `__EVENTTARGET` = "",
  # `__EVENTARGUMENT` = "",
  `__LASTFOCUS` = "",
  `__VIEWSTATE` = "8yKNzXYG2TWcKwAlH5IzsDjPucLH7+uLksJKhh/wJMiaFPd3YT5+U09FRvY6XghnW3FT9oR2Kf/26wRy4/2/bncSZWX5U4tdk3nzj6euJl6k8Lk3HovuUTiA4gMoHDyuPYMFj4ShV4MopnCJXsn3q87ibhJSeD5FhXIuOSHx9FL3KwUA34aRr4T220U8YmN+mJzaOLJG/nWMGVa8sx0CtrYC2gFa4i1I/K2kMRxwyWQ0ILRclPw9EptL+7Si/zJDwEKOo5E/7UpGk44NJg/tE5fZaDc+mRXbdEqx/mDvX5ngN7N9jjGBDcjWsw+G2JEyVITZnParT2n9H3KiuaNq2x77A0YujHj/6/FIvAPCtqJ4RcUDzq8bbO2/AwdGar/83SudSc4D4uSTXmEqJyqxzyuhXwHNjdrw+npo/MwImXtSPObS0SL7y4xIC4dSsHyVP86eDXljfFTK2iFpCN0mWfwcA5S3HEeUCQLoW7rHrlAu3X+Tow/ravgrxYcceSLdkLdC6xpMEJY/H7tTr35XNHDJy5Eob4vR8Uyb2xc101oapaGXX9H2AqM1f94TjuxyB+4+jke59ZGCO+8TIz1fCmxPByxNj93RYcaU9hGWDnY=",
  `__VIEWSTATEGENERATOR` = "37FEC614",
  `__VIEWSTATEENCRYPTED` = "",
  `__EVENTVALIDATION` = "C0AM6mHInEf5OZW58tzs1HoaUQVAayaWq5lmb3wRgulkODYJ8UcX5zQT2YEg3H8qOtJ8757obtSjR1lo7zie3MbYLX3XP+NohsMwTqkysQrRs5wyr8EkDrWLMq5ZJs+VqgJYc4m/oHwAZ9f0foMEEKOJ/YaY23QdSPw0RRACy/O002Qo12/KNIvkHjVg0HsQQ11RrVeo+69pCd9oRPZ1Mj7RkqYojDumHTzH65YBTI1IjK8TLC9LAxCeZTGDc53fDY6vKt/tl5xHyI04XAFzr8rk7zFbQfpWgZdClwyYrWhCRXMKfeQG5pAJgvhbe9trnglC5NW+Eyfg5L5HxPYRI0Q6zYv1we5q2HrKMedNQMX5SAw8NVF0d50R47X6dpqXC+vGOu6QWPYpW9IV5iphE2og2UnoI3YcWwCbnjKD1DGPTla1cZrlS09VikodPLChNn+qp2z5dPZSYQQw7i0I/Q==",
  `ctl00$MainContent$Ddl_Rpt_type` = "Retail",
  `ctl00$MainContent$ddl_Language` = "English",
  `ctl00$MainContent$Rbl_Rpt_type` = "Price report",
  `ctl00$MainContent$Ddl_Rpt_Option0` = "Daily Prices",
  `ctl00$MainContent$Txt_FrmDate` = "01/05/2024",
  `ctl00$MainContent$btn_getdata1` = "Get Data"
)

response <- httr::POST(url = "https://fcainfoweb.nic.in/reports/report_menu_web.aspx", httr::add_headers(.headers=headers), httr::set_cookies(.cookies = cookies), body = data, encode = "form")

data <- content(response) |>
  html_node("table") %>%
  html_table()

head(data)