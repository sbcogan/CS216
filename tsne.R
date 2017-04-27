#this is the tsne package version (not Rtsne).that leaves me with less flexibility
mydata <- read.table("sentiment_data_quran.csv", header=TRUE, sep=",")

# load the tsne package
library(tsne)

# initialize counter to 0
x <- 0
epc <- function(x) {
  x <<- x + 1
  filename <- paste("d:\\plot", x, "jpg", sep=".")
  cat("> Plotting TSNE to ", filename, " ")
  
  # plot to d:\\plot.x.jpg file of 2400x1800 dimension
  jpeg(filename, width=2400, height=1800)
  
  plot(x, t='n', main="T-SNE")
  text(x, labels=rownames(mydata))
  dev.off()
}

# run tsne (maximum iterations:500, callback every 100 epochs, target dimension k=5)
tsne_data <- tsne(mydata, k=5, epoch_callback=epc, max_iter=500, epoch=100)
