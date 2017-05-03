#this is the tsne package version (not Rtsne).that leaves me with less flexibility
mydata <- read.table("combined_sentiment.csv", header=TRUE, sep=",", row.names = 1)

# load the tsne package
library(tsne)
#names <- rownames()
# initialize counter to 0
x <- 0
epc <- function(x) {
  x <<- x + 1
  filename <- paste("d:\\plot", x, "jpg", sep=".")
  cat("> Plotting TSNE to ", filename, " ")
  color = "black"
  color[is.numeric(rownames(mydata))] = 'green'
  # plot to d:\\plot.x.jpg file of 2400x1800 dimension
  jpeg(filename, width=2400, height=1800)
  plot(x, t='n', main="T-SNE")
  text(x, labels=rownames(mydata), col = color)
  dev.off()
}

# run tsne (maximum iterations:500, callback every 100 epochs, target dimension k=2)
tsne_data <- tsne(mydata, k=2,  initial_dims = 5,epoch_callback=epc, perplexity = 8, max_iter=500, epoch=100, whiten = TRUE)
