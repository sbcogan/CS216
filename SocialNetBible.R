library(igraph)
linkso <- read.csv("kjb_cleanedpairs.csv", header=T, as.is=T)
linkso$Book..Chapter..Verse.Number <- NULL
colnames(linkso)[1] <- "from"
colnames(linkso)[2] <- "to"
linkso$from[linkso$from == "Christ"] = "Jesus"
linkso$to[linkso$to == "Christ"] = "Jesus"
linkso$to[linkso$to == "GOD"] = "God"
linkso$from[linkso$from == "GOD"] = "God"
links <- aggregate(linkso[,3], linkso[,-3], sum)
colnames(links)[3] <- "weight"
links <- links[order(-links$weight),]
links1<- links[-5,] #Remove GOD god
links2 <- links1[-7,]
links <- links2
links10 <- subset(links, links$weight > 9)
links20 <- subset(links, links$weight >19)
links30 <- subset(links, links$weight>29)
link2node10 <- links10
link2node10$weight <- NULL
link2node20 <- links20 
link2node20$weight <- NULL
link2node30 <- links30
link2node30$weight <- NULL
node10 <- unique(stack(link2node10))
node20 <- unique(stack(link2node20))
node30 <- unique(stack(link2node30))
colnames(node10)[1] <- "name"
colnames(node20)[1] <- "name"
colnames(node30)[1]<- "name"
node10$ind <- NULL
node20$ind <- NULL
node30$ind <- NULL
nodes10<- unique(node10)
nodes20 <- unique(node20)
nodes30 <- unique(node30)
net10 <- graph.data.frame(links10, nodes10, directed=F)
net20 <- graph.data.frame(links20, nodes20, directed=F)
net30 <- graph.data.frame(links30, nodes30, directed=F)
#lets just work on the simplifed (20+ connections show up) one first
net20 <- simplify(net20, remove.multiple = F, remove.loops = T) 
deg <- degree(net20, mode="all")
V(net20)$size <- deg*.25
E(net20)$width <- E(net20)$weight/50
E(net20)$edge.color <- "gray80"
ecol <- rep("gray80", ecount(net20))
ecol[unlist(links20$from == "God")] <- "orange"
ecol[unlist(links20$to == "God")] <- "orange"
ecol[unlist(links20$to =="Jesus")] <- "yellow"
ecol[unlist(links20$fom =="Jesus")] <- "yellow"
plot(net20, edge.curved=.1, edge.color = ecol, vertex.frame.color= "white", layout = layout.random(net20), vertex.color=adjustcolor("gray50", alpha.f = .8), asp = 0, vertex.label.cex=.7, vertex.label.color=adjustcolor("black", alpha.f = .8))
plot(net20, edge.curved=.1, edge.color = ecol, vertex.frame.color= "white", layout = layout.sphere(net20), vertex.color=adjustcolor("gray50", alpha.f = .8), asp = 0, vertex.label.cex=.7, vertex.label.color=adjustcolor("black", alpha.f = .8))
plot(net20, edge.curved=.1, edge.color = ecol, vertex.shape = "none", vertex.size = .1, layout = layout.circle(net20), asp = 0, vertex.label.cex=.7, vertex.label.color=adjustcolor("black", alpha.f = .8))

#now
net10 <- simplify(net10, remove.multiple = F, remove.loops = T) 
deg <- degree(net10, mode="all")
V(net10)$size <- deg*.1
E(net10)$width <- E(net10)$weight/50
E(net10)$edge.color <- "gray80"
ecol <- rep("gray80", ecount(net10))
ecol[unlist(links10$from == "God")] <- "orange"
ecol[unlist(links10$to == "God")] <- "orange"
ecol[unlist(links10$to =="Jesus")] <- "yellow"
ecol[unlist(links10$from =="Jesus")] <- "yellow"
tcol <- rep(adjustcolor("black", alpha.f = .8), ecount(net10))
tcol[unlist(deg <10)] <- adjustcolor("black", alpha.f = .5)
tsize <- rep(.6, ecount(net10))
tsize[unlist(deg <10)] <-.5

#a random graph, then a sphere, then a circle
plot(net10, edge.curved=.1, edge.color = ecol, vertex.frame.color= "white", layout = layout.random(net10), vertex.color=adjustcolor("gray50", alpha.f = .8), asp = 0, vertex.label.cex=.7, vertex.label.color=adjustcolor("black", alpha.f = .8))
plot(net10, edge.curved=.1, edge.color = ecol, vertex.frame.color= "white", layout = layout.sphere(net10), vertex.color=adjustcolor("gray50", alpha.f = .8), asp = 0, vertex.label.cex=.7, vertex.label.color=adjustcolor("black", alpha.f = .8))
plot(net10, edge.curved=.1, edge.color = ecol, vertex.shape = "none", layout = layout.circle(net10), asp = 0, vertex.label.cex=.7, vertex.label.color=adjustcolor("black", alpha.f = .8))
plot(net10, edge.curved=.1, edge.color = ecol, vertex.shape = "none", layout = layout_on_grid(net10), asp = 0, vertex.label.cex=.7, vertex.label.color=adjustcolor("black", alpha.f = .8))
tkid <- tkplot(net10)
l <- tkplot.getcoords(tkid)
plot(net10, edge.curved=.1, edge.color = ecol, vertex.frame.color= "white", layout = l, vertex.color=adjustcolor("gray50", alpha.f = .8), asp = 0, vertex.label.cex=.7, vertex.label.color=adjustcolor("black", alpha.f = .8))


net30 <- simplify(net30, remove.multiple = F, remove.loops = T) 
deg <- degree(net30, mode="all")
V(net30)$size <- deg*.25
E(net30)$width <- E(net30)$weight/50
E(net30)$edge.color <- "gray80"
ecol <- rep("gray80", ecount(net30))
ecol[unlist(links30$from == "God")] <- "orange"
ecol[unlist(links30$to == "God")] <- "orange"
ecol[unlist(links30$to =="Jesus")] <- "yellow"
ecol[unlist(links30$from =="Jesus")] <- "yellow"
plot(net30, edge.curved=.1, edge.color = ecol, vertex.frame.color= "white", layout = layout.random(net30), vertex.color=adjustcolor("gray50", alpha.f = .8), asp = 0, vertex.label.cex=.7, vertex.label.color=adjustcolor("black", alpha.f = .8))
plot(net30, edge.curved=.1, edge.color = ecol, vertex.frame.color= "white", layout = layout.sphere(net30), vertex.color=adjustcolor("gray50", alpha.f = .8), asp = 0, vertex.label.cex=.7, vertex.label.color=adjustcolor("black", alpha.f = .8))
plot(net30, edge.curved=.1, edge.color = ecol, vertex.shape = "none", vertex.size = .1, layout = layout.circle(net30), asp = 0, vertex.label.cex=.7, vertex.label.color=adjustcolor("black", alpha.f = .8))

#now