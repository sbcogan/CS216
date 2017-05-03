
tones<- c(0.191024247,0.377882463,0.206939711,	0.30037463,	0.391631228)#torah 
#tones<- c(0.199262049,	0.386728159, 0.190559302,	0.273776209, 0.41537271) #oldtest
#tones<- c(0.160715999,	0.372718463,	0.207049297,	0.374605607,	0.456329388) #new
#tones<- c(0.256390019, 0.191328189,	0.283999168,	0.456699812,	0.513324886)#koran
x<- matrix(tones, 1, 5)
data <- data.frame(x)
colnames(data)=c("Anger", "Disgust", "Fear", "Joy", "Sadness")
library(fmsb)
data=rbind(rep(.5,5) , rep(0,5) , data)
#color = c(rgb(0.2,0.5,0.5,0.8)) #turquoise
#color = c(rgb(.8,0,0,0.8)) #red
#color = c(rgb(.8, .8, 0, .8)) #yellow
color = c(rgb(.5,0,.5,0.8))
radarchart(data, pcol = color, pfcol = color,  cglty=1, cglcol="grey", title = "Torah (0-.5 Scale)", centerzero = TRUE, caxislabels=seq(0,1,.25), axislabcol="black", cglwd=0.8)

