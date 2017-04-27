
ch1<- c(0.029573, 0.289592, 0.058911, 0.402043, 0.101180)
x <- matrix(ch1,nrow = 1,ncol = 5)
data <- data.frame(x)
colnames(data)=c("Anger", "Disgust", "Fear", "Joy", "Sadness")
library(fmsb)
data=rbind(rep(.5,5) , rep(0,5) , data)
polycolors = c(rgb(0.2,0.5,0.5,0.8))
#polycolors = c(rgb(0.2,0.5,0.5,0.9))

radarchart(data, pcol = rgb(0.2,0.5,0.5,0.9), pfcol = polycolors,  cglty=1, cglcol="grey", title = "Quran", centerzero = TRUE)

