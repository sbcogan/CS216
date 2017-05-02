# imports
library(readr)
library(dplyr)
library(calibrate)
library(ggplot2)
library(gridExtra)
library(reshape2)
library(Metrics)

# read in bible, quran, sermon data
# there are two sermon datasets, denom_sermons with one row per sermon, and cite_sermons with
# one row per cited verse (so sermons with multiple citations appear more than once)
bible <- read_csv("C:/Users/Peter/Downloads/CS216_28/CS216-master/sentiment_data_bible.csv")
bible <- as.data.frame(bible)
summary(bible)
colnames(bible)
quran <- read_csv("C:/Users/Peter/Downloads/CS216_28/CS216-master/sentiment_data_quran.csv")
quran <- as.data.frame(quran)
summary(quran)
colnames(quran)
denom_sermons <- read_delim("C:/Users/Peter/Downloads/CS216_28/CS216-master/sentiment_data_sermons.tsv",
                         "\t", escape_double = FALSE, trim_ws = TRUE)
summary(denom_sermons)
colnames(denom_sermons)
cite_sermons <- read_delim("C:/Users/Peter/Downloads/CS216_28/CS216-master/ungrouped_sentiment_data_sermons.tsv",
           "\t", escape_double = FALSE, trim_ws = TRUE)
summary(cite_sermons)
colnames(cite_sermons)

# creates dataframe with weighed sentiment averages for each book of bible
# writes to csv "sentiment_data_bible_by_book_FINAL.csv"
# weights are word count lengths of chapters
bible_books <- bible %>%
  group_by(book) %>%
  summarise(weighted.anger = weighted.mean(anger, weight),
            weighted.disgust = weighted.mean(disgust, weight),
            weighted.fear = weighted.mean(fear, weight),
            weighted.joy = weighted.mean(joy, weight),
            weighted.sadness = weighted.mean(sadness, weight),
            weighted.openness = weighted.mean(openness, weight),
            weighted.conscientiousness = weighted.mean(conscientiousness, weight),
            weighted.extraversion = weighted.mean(extraversion, weight),
            weighted.agreeableness = weighted.mean(agreeableness, weight),
            weighted.emotional_range = weighted.mean(emotional_range, weight),
            book.weight = sum(weight),
            min.index = min(index)
  )
bible_books <- bible_books[order(bible_books$min.index,decreasing = FALSE),]
bible_books
write.csv(bible_books, "sentiment_data_bible_by_book_FINAL.csv")

# creates dataframe with weighted average of sentiments for torah,
# old testmant, new testament, koran, and sermons
# writes results to sentiment_data_5_groups.csv
# weights are word count lengths of text sections
torah <- bible_books[1:5,]
torah_data <- bible[1,2:12]
torah_data[1,] <- c(
    "Torah",
    weighted.mean(torah$weighted.anger,torah$book.weight),
    weighted.mean(torah$weighted.disgust,torah$book.weight),
    weighted.mean(torah$weighted.fear,torah$book.weight),
    weighted.mean(torah$weighted.joy,torah$book.weight),
    weighted.mean(torah$weighted.sadness,torah$book.weight),
    weighted.mean(torah$weighted.openness,torah$book.weight),
    weighted.mean(torah$weighted.conscientiousness,torah$book.weight),
    weighted.mean(torah$weighted.extraversion,torah$book.weight),
    weighted.mean(torah$weighted.agreeableness,torah$book.weight),
    weighted.mean(torah$weighted.emotional_range,torah$book.weight)
)
torah_data

old_testament <- bible_books[1:39,]
old_testament_data <- bible[1,2:12]
old_testament_data[1,] <- c(
  "Old Testament",
  weighted.mean(old_testament$weighted.anger,old_testament$book.weight),
  weighted.mean(old_testament$weighted.disgust,old_testament$book.weight),
  weighted.mean(old_testament$weighted.fear,old_testament$book.weight),
  weighted.mean(old_testament$weighted.joy,old_testament$book.weight),
  weighted.mean(old_testament$weighted.sadness,old_testament$book.weight),
  weighted.mean(old_testament$weighted.openness,old_testament$book.weight),
  weighted.mean(old_testament$weighted.conscientiousness,old_testament$book.weight),
  weighted.mean(old_testament$weighted.extraversion,old_testament$book.weight),
  weighted.mean(old_testament$weighted.agreeableness,old_testament$book.weight),
  weighted.mean(old_testament$weighted.emotional_range,old_testament$book.weight)
)
old_testament_data

new_testament <- bible_books[40:66,]
new_testament_data <- bible[1,2:12]
new_testament_data[1,] <- c(
  "New Testament",
  weighted.mean(new_testament$weighted.anger,new_testament$book.weight),
  weighted.mean(new_testament$weighted.disgust,new_testament$book.weight),
  weighted.mean(new_testament$weighted.fear,new_testament$book.weight),
  weighted.mean(new_testament$weighted.joy,new_testament$book.weight),
  weighted.mean(new_testament$weighted.sadness,new_testament$book.weight),
  weighted.mean(new_testament$weighted.openness,new_testament$book.weight),
  weighted.mean(new_testament$weighted.conscientiousness,new_testament$book.weight),
  weighted.mean(new_testament$weighted.extraversion,new_testament$book.weight),
  weighted.mean(new_testament$weighted.agreeableness,new_testament$book.weight),
  weighted.mean(new_testament$weighted.emotional_range,new_testament$book.weight)
)
new_testament_data

quran_data <- bible[1,2:12]
quran_data[1,] <- c(
  "Quran",
  weighted.mean(quran$anger,quran$weight),
  weighted.mean(quran$disgust,quran$weight),
  weighted.mean(quran$fear,quran$weight),
  weighted.mean(quran$joy,quran$weight),
  weighted.mean(quran$sadness,quran$weight),
  weighted.mean(quran$openness,quran$weight),
  weighted.mean(quran$conscientiousness,quran$weight),
  weighted.mean(quran$extraversion,quran$weight),
  weighted.mean(quran$agreeableness,quran$weight),
  weighted.mean(quran$emotional_range,quran$weight)
)
quran_data

whole_bible_data <- bible[1,2:12]
whole_bible_data[1,] <- c(
  "Whole Bible",
  weighted.mean(bible_books$weighted.anger,bible_books$book.weight),
  weighted.mean(bible_books$weighted.disgust,bible_books$book.weight),
  weighted.mean(bible_books$weighted.fear,bible_books$book.weight),
  weighted.mean(bible_books$weighted.joy,bible_books$book.weight),
  weighted.mean(bible_books$weighted.sadness,bible_books$book.weight),
  weighted.mean(bible_books$weighted.openness,bible_books$book.weight),
  weighted.mean(bible_books$weighted.conscientiousness,bible_books$book.weight),
  weighted.mean(bible_books$weighted.extraversion,bible_books$book.weight),
  weighted.mean(bible_books$weighted.agreeableness,bible_books$book.weight),
  weighted.mean(bible_books$weighted.emotional_range,bible_books$book.weight)
)
whole_bible_data

denom_sermon_data <- bible[1,2:12]
denom_sermon_data[1,] <- c(
  "denom_sermons",
  mean(denom_sermons$anger),
  mean(denom_sermons$disgust),
  mean(denom_sermons$fear),
  mean(denom_sermons$joy),
  mean(denom_sermons$sadness),
  mean(denom_sermons$openness),
  mean(denom_sermons$conscientiousness),
  mean(denom_sermons$extraversion),
  mean(denom_sermons$agreeableness),
  mean(denom_sermons$emotional_range)
)
denom_sermon_data

sentiment_data_6_groups <- as.data.frame(rbind(
    torah_data,old_testament_data,new_testament_data,
    quran_data,denom_sermon_data,whole_bible_data))

write.csv(sentiment_data_6_groups, "sentiment_data_6_groups.csv")


# creates labeled plots for sentiment scores of each book of the bible and
# chapter of quran, in order
# prints top 6 books for each score
plot(bible_books$weighted.anger)
textxy(seq(1,66),bible_books$weighted.anger,labs = bible_books$book)
bible_books$book[order(bible_books$weighted.anger, decreasing = TRUE)][1:6]

plot(bible_books$weighted.disgust)
textxy(seq(1,66),bible_books$weighted.disgust,labs = bible_books$book)
bible_books$book[order(bible_books$weighted.disgust, decreasing = TRUE)][1:6]

plot(bible_books$weighted.fear)
textxy(seq(1,66),bible_books$weighted.fear,labs = bible_books$book)
bible_books$book[order(bible_books$weighted.fear, decreasing = TRUE)][1:6]

plot(bible_books$weighted.joy, xlab = "Book Number",ylab = "",
     main = "Joy Score by Book")
textxy(seq(1,66),bible_books$weighted.joy,labs = bible_books$book)
bible_books$book[order(bible_books$weighted.joy, decreasing = TRUE)][1:6]

plot(bible_books$weighted.sadness)
textxy(seq(1,66),bible_books$weighted.sadness,labs = bible_books$book)
bible_books$book[order(bible_books$weighted.sadness, decreasing = TRUE)][1:6]

plot(bible_books$weighted.openness)
textxy(seq(1,66),bible_books$weighted.openness,labs = bible_books$book)
bible_books$book[order(bible_books$weighted.openness, decreasing = TRUE)][1:6]

plot(bible_books$weighted.conscientiousness)
textxy(seq(1,66),bible_books$weighted.conscientiousness,labs = bible_books$book)
bible_books$book[order(bible_books$weighted.conscientiousness, decreasing = TRUE)][1:6]

plot(bible_books$weighted.extraversion)
textxy(seq(1,66),bible_books$weighted.extraversion,labs = bible_books$book)
bible_books$book[order(bible_books$weighted.extraversion, decreasing = TRUE)][1:6]

plot(bible_books$weighted.agreeableness)
textxy(seq(1,66),bible_books$weighted.agreeableness,labs = bible_books$book)
bible_books$book[order(bible_books$weighted.agreeableness, decreasing = TRUE)][1:6]

plot(bible_books$weighted.emotional_range)
textxy(seq(1,66),bible_books$weighted.emotional_range,labs = bible_books$book)
bible_books$book[order(bible_books$weighted.emotional_range, decreasing = TRUE)][1:6]


plot(quran$anger)
textxy(seq(1,114),quran$anger,labs = quran$book)
quran$book[order(quran$anger, decreasing = TRUE)][1:6]

plot(quran$disgust)
textxy(seq(1,114),quran$disgust,labs = quran$book)
quran$book[order(quran$disgust, decreasing = TRUE)][1:6]

plot(quran$fear)
textxy(seq(1,114),quran$fear,labs = quran$book)
quran$book[order(quran$fear, decreasing = TRUE)][1:6]

plot(quran$joy)
textxy(seq(1,114),quran$joy,labs = quran$chapter)
quran$book[order(quran$joy, decreasing = TRUE)][1:6]

plot(quran$sadness)
textxy(seq(1,114),quran$sadness,labs = quran$book)
quran$book[order(quran$sadness, decreasing = TRUE)][1:6]

plot(quran$openness)
textxy(seq(1,114),quran$openness,labs = quran$book)
quran$book[order(quran$openness, decreasing = TRUE)][1:6]

plot(quran$conscientiousness)
textxy(seq(1,114),quran$conscientiousness,labs = quran$book)
quran$book[order(quran$conscientiousness, decreasing = TRUE)][1:6]

plot(quran$extraversion)
textxy(seq(1,114),quran$extraversion,labs = quran$book)
quran$book[order(quran$extraversion, decreasing = TRUE)][1:6]

plot(quran$agreeableness)
textxy(seq(1,114),quran$agreeableness,labs = quran$book)
quran$book[order(quran$agreeableness, decreasing = TRUE)][1:6]

plot(quran$emotional_range)
textxy(seq(1,114),quran$emotional_range,labs = quran$book)
quran$book[order(quran$emotional_range, decreasing = TRUE)][1:6]


# creates histograms of sentiment scores for bible and sermons
breaks = seq(0,1,.05)
hist(bible_books$weighted.anger,breaks = breaks)
hist(bible_books$weighted.disgust,breaks = breaks)
hist(bible_books$weighted.fear,breaks = breaks)
hist(bible_books$weighted.joy,breaks = breaks)
hist(bible_books$weighted.sadness,breaks = breaks)
hist(bible_books$weighted.openness,breaks = breaks)
hist(bible_books$weighted.conscientiousness,breaks = breaks)
hist(bible_books$weighted.extraversion,breaks = breaks)
hist(bible_books$weighted.agreeableness,breaks = breaks)
hist(bible_books$weighted.emotional_range,breaks = breaks)

hist(denom_sermons$anger,breaks = breaks)
hist(denom_sermons$disgust,breaks = breaks)
hist(denom_sermons$fear,breaks = breaks)
hist(denom_sermons$joy,breaks = breaks)
hist(denom_sermons$sadness,breaks = breaks)
hist(denom_sermons$openness,breaks = breaks)
hist(denom_sermons$conscientiousness,breaks = breaks)
hist(denom_sermons$extraversion,breaks = breaks)
hist(denom_sermons$agreeableness,breaks = breaks)
hist(denom_sermons$emotional_range,breaks = breaks)

## analysis of sermons by denomination

# denomination counts
table(denom_sermons$denomination)[order(table(denom_sermons$denomination),decreasing = TRUE)][1:10]

# creates data frame of avg sentiment scores by denomination
sermon_denominations <- denom_sermons %>%
  group_by(denomination) %>%
  summarise(mean.anger = mean(anger),
            mean.disgust = mean(disgust),
            mean.fear = mean(fear),
            mean.joy = mean(joy),
            mean.sadness = mean(sadness),
            n = length(denomination)

  )
sermon_denominations
sermon_denominations <- sermon_denominations[order(sermon_denominations$n,decreasing = TRUE),]
sermon_denominations
write.csv(sermon_denominations, "sentiment_data_sermons_by_denom.csv")


# creates graph showing variation among all sermons
# variation := MAE between sermons and avg sermon
sermon_diff <- as.data.frame(c(mae(mean(denom_sermons$anger),denom_sermons$anger),
                               mae(mean(denom_sermons$disgust),denom_sermons$disgust),
                               mae(mean(denom_sermons$fear),denom_sermons$fear),
                               mae(mean(denom_sermons$joy),denom_sermons$joy),
                               mae(mean(denom_sermons$sadness),denom_sermons$sadness)))
sermon_diff <- cbind(c('Anger','Disgust','Fear','Joy','Sadness'),sermon_diff)
names(sermon_diff) <- c('Emotion','Score')
ggplot(sermon_diff,aes(x=Emotion,y=Score,fill=Emotion)) +
  geom_bar(stat = "identity") +
  xlab("") +
  ylab("MAE from Overall Mean") +
  ggtitle("Average Absolute Difference Between Sermons and Overall Mean") +
  coord_cartesian(ylim=c(0,.25)) +
  scale_fill_manual("Legend", values = c("Anger" = "red",
                                         "Disgust" = "green",
                                         "Fear" = "purple",
                                         "Joy" = "yellow",
                                         "Sadness" = "blue"))


# limit analysis to denominations with at least 10 sermons
sermon_denominations <- sermon_denominations[sermon_denominations$n > 10,]

# creates graph showing variation within denominations
# variation := MAE between denominations and avg denomination
sermon_diff <- as.data.frame(c(mae(mean(sermon_denominations$mean.anger),sermon_denominations$mean.anger),
  mae(mean(sermon_denominations$mean.disgust),sermon_denominations$mean.disgust),
  mae(mean(sermon_denominations$mean.fear),sermon_denominations$mean.fear),
  mae(mean(sermon_denominations$mean.joy),sermon_denominations$mean.joy),
  mae(mean(sermon_denominations$mean.sadness),sermon_denominations$mean.sadness)))
sermon_diff <- cbind(c('Anger','Disgust','Fear','Joy','Sadness'),sermon_diff)
names(sermon_diff) <- c('Emotion','Score')
ggplot(sermon_diff,aes(x=Emotion,y=Score,fill=Emotion)) +
  geom_bar(stat = "identity") +
  xlab("") +
  ylab("MAE from Overall Mean") +
  ggtitle("Average Absolute Difference Between Denominations and Overall Mean") +
  coord_cartesian(ylim=c(0,.25)) +
  scale_fill_manual("Legend", values = c("Anger" = "red",
                                         "Disgust" = "green",
                                         "Fear" = "purple",
                                         "Joy" = "yellow",
                                         "Sadness" = "blue"))


## analysis of sermons by citation

# book citation counts
table(cite_sermons$book)[order(table(cite_sermons$book), decreasing = TRUE)][1:10]#citation freq

# creates dataframe of books of the bible and the avg sermon which cites them
sermon_books <- cite_sermons %>%
  group_by(book) %>%
  summarise(mean.anger = mean(anger),
            mean.disgust = mean(disgust),
            mean.fear = mean(fear),
            mean.joy = mean(joy),
            mean.sadness = mean(sadness),
            mean.openness = mean(openness),
            mean.conscientiousness = mean(conscientiousness),
            mean.extraversion = mean(extraversion),
            mean.agreeableness = mean(agreeableness),
            mean.emotional_range = mean(emotional_range),
            n = length(book)
  )
sermon_books
sermon_books <- sermon_books[order(sermon_books$n,decreasing = TRUE),]
sermon_books
write.csv(sermon_books, "sentiment_data_sermons_by_book.csv")


# creates data frame with the differences between a book's avg sermon and the
# book itself
bible_books$book[19] <- "Psalms"
bible_books$book[22] <- "Song of Songs"

diff_bible_sermons <- sermon_books
for (i in seq(1,nrow(sermon_books))){
  diff_bible_sermons[i,2:11] <- as.numeric(sermon_books[i,2:11]) -
  as.numeric(bible_books[bible_books$book == as.character(sermon_books[i,1]),2:11])
}
write.csv(diff_bible_sermons,"sentiment_data_bible_vs_sermons.csv")


# limit analysis to books with at least 10 citations
diff_bible_sermons <- diff_bible_sermons[diff_bible_sermons$n >= 10,]

# creates graph of avg absolute deviation between books and their avg sermon
# avg absolute deviation := MAE between books and their avg sermons
# illustrates the magnitude of deviation between sermons and the bible
sermon_diff <- as.data.frame(c(mean(abs(diff_bible_sermons$mean.anger)),
                             mean(abs(diff_bible_sermons$mean.disgust)),
                             mean(abs(diff_bible_sermons$mean.fear)),
                             mean(abs(diff_bible_sermons$mean.joy)),
                             mean(abs(diff_bible_sermons$mean.sadness))))

sermon_diff <- cbind(c('Anger','Disgust','Fear','Joy','Sadness'),sermon_diff)
names(sermon_diff) <- c('Emotion','Score')
ggplot(sermon_diff,aes(x=Emotion,y=Score,fill=Emotion)) +
  geom_bar(stat = "identity") +
  xlab("") +
  ylab("MAE from Overall Mean") +
  ggtitle("Average Absolute Difference Between Sermons and Bible Book They Draw From") +
  coord_cartesian(ylim=c(0,.25)) +
  scale_fill_manual("Legend", values = c("Anger" = "red",
                                         "Disgust" = "green",
                                         "Fear" = "purple",
                                         "Joy" = "yellow",
                                         "Sadness" = "blue"))

# creates a graph of avg deviation between books and their avg sermon
# avg deviation := average error between books and their avg sermons
# illustrates the direction of deviation between sermons and the bible
sermon_diff <- as.data.frame(c(mean((diff_bible_sermons$mean.anger)),
                               mean((diff_bible_sermons$mean.disgust)),
                               mean((diff_bible_sermons$mean.fear)),
                               mean((diff_bible_sermons$mean.joy)),
                               mean((diff_bible_sermons$mean.sadness))))

sermon_diff <- cbind(c('Anger','Disgust','Fear','Joy','Sadness'),sermon_diff)
names(sermon_diff) <- c('Emotion','Score')
ggplot(sermon_diff,aes(x=Emotion,y=Score,fill=Emotion)) +
  geom_bar(stat = "identity") +
  xlab("") +
  ylab("Average Difference from Overall Mean") +
  ggtitle("Average Difference Between Sermons and Bible Book They Draw From") +
  coord_cartesian(ylim=c(-.25,.25)) +
  scale_fill_manual("Legend", values = c("Anger" = "red",
                                         "Disgust" = "green",
                                         "Fear" = "purple",
                                         "Joy" = "yellow",
                                         "Sadness" = "blue"))

# creates graphs of the avg sentiment scores for the whole bible
# and all of the sermons

whole_bible_vec <- as.data.frame(as.numeric(whole_bible_data[2:6]))
whole_bible_vec <- cbind(c('Anger','Disgust','Fear','Joy','Sadness'),whole_bible_vec)
names(whole_bible_vec) <- c('Emotion','Score')
ggplot(whole_bible_vec,aes(x=Emotion,y=Score,fill=Emotion)) +
  geom_bar(stat = "identity") +
  xlab("") +
  ylab("Score") +
  ggtitle("Sentiment Scores for the Bible") +
  coord_cartesian(ylim=c(0,1)) +
  scale_fill_manual("Legend", values = c("Anger" = "red",
                                         "Disgust" = "green",
                                         "Fear" = "purple",
                                         "Joy" = "yellow",
                                         "Sadness" = "blue"))

sermons_vec <- as.data.frame(as.numeric(denom_sermon_data[2:6]))
sermons_vec <- cbind(c('Anger','Disgust','Fear','Joy','Sadness'),sermons_vec)
names(sermons_vec) <- c('Emotion','Score')
ggplot(sermons_vec,aes(x=Emotion,y=Score,fill=Emotion)) +
  geom_bar(stat = "identity") +
  xlab("") +
  ylab("Score") +
  ggtitle("Average Sentiment Scores for Sermons") +
  coord_cartesian(ylim=c(0,1)) +
  scale_fill_manual("Legend", values = c("Anger" = "red",
                                         "Disgust" = "green",
                                         "Fear" = "purple",
                                         "Joy" = "yellow",
                                         "Sadness" = "blue"))
