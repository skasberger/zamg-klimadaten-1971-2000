# Settings
library("climatol")
require(lattice)

# Variables
period <- "1971-2000"

# main
setwd("./data/r/")

#csvlist <- list.files(pattern = "*csv$")
file_list <- read.table("metadata.csv", dec=".", sep=",", header=FALSE)
file_list <- file_list[, c(3,4,5,8)]

# add image filenames to data.frame
temp<-file_list[,4]
for (i in seq_along(temp)) {
  png<-gsub("csv", "png", temp)
  svg<-gsub("csv", "svg", temp)
}
file_list<-cbind(file_list, png, svg)

for (i in seq_along(file_list[, 4])) {
  csv_filename<-as.character(file_list[i, 4])
  climate_data <- read.table(csv_filename, dec=".", sep=",", header=TRUE, row.names = 1)
  # the png is created from the svg while post processing
  svg(as.character(file_list[i, 6]))
  diagwl(climate_data, est=file_list[i,1], alt=file_list[i,2], per=period, mlab="en")
  dev.off()
}

