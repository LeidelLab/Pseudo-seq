# Read WTplus data
WTplus <- read.table("WTpluscombined.coverage", header = FALSE, sep = "\t")

# Calculate mean values for WTplus data
mean_values <- rowMeans(WTplus[, c("V3", "V4", "V5", "V6", "V7", "V8")])
WTplus$MeanCoverage <- mean_values

# Read WTminus data
WTminus <- read.table("WTminuscombined.coverage", header = FALSE, sep = "\t")

# Calculate mean values for WTminus data
mean_values_minus <- rowMeans(WTminus[, c("V3", "V4", "V5", "V6", "V7", "V8")])
WTminus$MeanCoverage <- mean_values_minus

# Calculate divided data for WTplus
divided_data_plus <- data.frame(
  V9_divided_by_V3 = (WTplus$V9 + 1) / (WTplus$V3 + 1),
  V10_divided_by_V4 = (WTplus$V10 + 1) / (WTplus$V4 + 1),
  V11_divided_by_V5 = (WTplus$V11 + 1) / (WTplus$V5 + 1),
  V12_divided_by_V6 = (WTplus$V12 + 1) / (WTplus$V6 + 1),
  V13_divided_by_V7 = (WTplus$V13 + 1) / (WTplus$V7 + 1),
  V14_divided_by_V9 = (WTplus$V14 + 1) / (WTplus$V8 + 1)
)
WTplusdivided <- cbind(WTplus, divided_data_plus)

# Calculate divided data for WTminus
divided_data_minus <- data.frame(
  V9_divided_by_V3 = (WTminus$V9 + 1) / (WTminus$V3 + 1),
  V10_divided_by_V4 = (WTminus$V10 + 1) / (WTminus$V4 + 1),
  V11_divided_by_V5 = (WTminus$V11 + 1) / (WTminus$V5 + 1),
  V12_divided_by_V6 = (WTminus$V12 + 1) / (WTminus$V6 + 1),
  V13_divided_by_V7 = (WTminus$V13 + 1) / (WTminus$V7 + 1),
  V14_divided_by_V9 = (WTminus$V14 + 1) / (WTminus$V8 + 1)
)
WTminusdivided <- cbind(WTminus, divided_data_minus)


# Calculate mean divides for WTplus and WTminus
meandividesplus <- rowMeans(WTplusdivided[, c("V9_divided_by_V3", "V10_divided_by_V4", "V11_divided_by_V5", "V12_divided_by_V6", "V13_divided_by_V7", "V14_divided_by_V9")])
WTplusdivided$MeanValuedividedplus <- meandividesplus

meandividedminus <- rowMeans(WTminusdivided[, c("V9_divided_by_V3", "V10_divided_by_V4", "V11_divided_by_V5", "V12_divided_by_V6", "V13_divided_by_V7", "V14_divided_by_V9")])
WTminusdivided$MeanValuedividedminus <- meandividedminus

# Combine WTplus and WTminus data
WTplusandminus <- cbind(WTplusdivided, WTminusdivided)

# Calculate normalized values
divided_data <- meandividesplus / meandividedminus

# Add normalized column to the data frame
WTplusandminus$normalized <- divided_data

# Write the final data frame to a tab-separated text file
write.table(WTplusandminus, "WTplusandminus.txt", sep = "\t", quote = FALSE, row.names = FALSE)
