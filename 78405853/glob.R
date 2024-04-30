filedir <- "somedata"

s <- c("sasmin", "sasmax", "sas")

p <- glob2rx(paste0(s, "_", filedir, ".txt"))

list.files(filedir, p, full.names=TRUE)
