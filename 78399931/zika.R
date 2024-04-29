library(rentrez)
library(Biostrings)

tmp <- tempfile()

writeLines(
  entrez_fetch(
    db = "nuccore",
    id = "NC_012532.1",
    rettype = "fasta",
    retmode = "text"
  ),
  tmp
)

dna <- readDNAStringSet(tmp, format = "fasta")

print(dna)

dput(dna)
