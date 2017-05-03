
data<- read.csv("sentiment_data_6_groups.csv", header = T)
data<- data[-c(1,5,6),]
data$conscientiousness <- NULL
data$openness <- NULL
data$extraversion<-NULL
data$agreeableness <- NULL
data$emotional_range<-NULL
data$group <-NULL
#tones<- c(0.191024247,0.377882463,0.206939711,	0.30037463,	0.391631228)#torah 
#data<- data.frame()
#data<- c(0.199262049,	0.386728159, 0.190559302,	0.273776209, 0.41537271) #oldtest
#tones<- c(0.160715999,	0.372718463,	0.207049297,	0.374605607,	0.456329388) #new
#tones<- c(0.256390019, 0.191328189,	0.283999168,	0.456699812,	0.513324886)#koran
#x<- matrix(data, 3, 5)
colnames(data)=c("Anger", "Disgust", "Fear", "Joy", "Sadness")
library(fmsb)
data=rbind(rep(.5,5) , rep(0,5) , data)
#color = c(rgb(0.2,0.5,0.5,0.8)) #turquoise
#color = c(rgb(.8,0,0,0.8)) #red
#color = c(rgb(.8, .8, 0, .8)) #yellow
#color = c(rgb(.5,0,.5,0.8),
color = c(rgb(.8,0,0,.5),rgb(.8, .8,0,.5), rgb(0.2,0.5,0.5,.5))
border = c(rgb(.8,0,0),rgb(.8, .8,0), rgb(0.2,0.5,0.5))
radarchart(data, seg = 5, pcol = color, pfcol =color, calcex = .2, cglty=1, cglcol="grey", title = "Comparative Sentiment (0-.5 Scale)", centerzero = TRUE, caxislabels=seq(0,1,.1),plty = 1,  axislabcol="black", plwd = 2, cglwd=0.8)
legend(x=2, y=1, legend = c("Old Testament", "New Testament", "Quran"), bty = "n", pch=20 , col=color , text.col = "black", cex=1, pt.cex=2)


