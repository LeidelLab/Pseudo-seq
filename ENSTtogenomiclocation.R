# Load required libraries
library(AnnotationHub)
library(ensembldb)
library(AnnotationForge)

# Load EnsDb object
ah <- AnnotationHub()
EnsDb.Hsap <- query(ah, c("EnsDb", "Homo sapiens"))
EnsDb.Hsap <- EnsDb.Hsap[["AH109336"]]

# Alternatively, load EnsDb from a different source
library(EnsDb.Hsapiens.v108)
edbx <- EnsDb.Hsapiens.v108

# Read data from a CSV file with columns: start, width, names
input_data <- read.csv("input.csv", header = TRUE)

# Create an IRanges object from the input data
rng_tx <- IRanges(start = input_data$start, width = input_data$width, names = input_data$names)

# Map transcript to genome coordinates
rng_gnm <- transcriptToGenome(rng_tx, edbx)

# Write results to CSV
write.csv(rng_gnm, "output.csv", row.names = FALSE)

