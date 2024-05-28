library(rvest)
library(stringr)

url <- "https://www.pro-football-reference.com/boxscores/202402110kan.htm"

# Ingest HTML from URL and convert to string.
html <- as.character(read_html(url))

# writeLines(as.character(html), con = "page.html")

# Use regular expressions to remove comments
cleaned <- str_remove_all(html, "(<!--|-->)")

# Ingest HTML from string.
html <- read_html(cleaned)

# writeLines(as.character(html), con = "page-cleaned.html")

html %>%
  html_nodes("div.table_container")

defense <- html %>%
  html_node("#player_defense") %>%
  html_table()

# Transfer first row (actually second <th> row) to column names.
colnames(defense) <- defense[1,]
# Drop first row.
defense <- defense[-1,]

defense
