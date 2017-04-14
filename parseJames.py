import logging
import re
from operator import itemgetter
from gensim import corpora, models, similarities
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

corpus_lsi = []
books = list() #each element in list is full text of a book
bookNames = list()
testamentText = ["", ""] # each element in list is full text of a testament

def calcByBook():
    curBook = "x"
    with open('kingjames.csv', 'r') as csv:
        counter = -1
        for line in csv:
            verse = line.split(",")[3]
            if  verse.strip().startswith("Verse Text"): #hard coded, ignoring header line
                continue
            if  not line.startswith(curBook):
                counter += 1
                books.append("")
                curBook = line.split(",")[0]
                bookNames.append(curBook)
            books[counter] += " " + verse
    calcBookScores(books)
    calcTestamentScoresSort()

def bookToTestament():
    oldT = True
    for i in range(len(books)):
        if bookNames[i].startswith("The Gospel"):
            oldT = False
        if oldT:
            testamentText[0] += books[i] + " "
        else:
            testamentText[1] += books[i] + " "

def calcTestamentScoresSort():
    bookToTestament()
    texts = [[word.strip(",:;.?!") for word in document.lower().split()] for document in testamentText]
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    tfidf = models.TfidfModel(corpus)
    tfidfTest= list()
    testNames = ["Old Testament", "New Testament"]
    for each in corpus:
        tfidfTest.append(tfidf[each])
    with open ("salientByTestament.txt", 'w') as out:
        out.write("The top 15 salient words in each testament of the bible\n")
        for i in range(len(tfidfTest)):
            top15 = sorted(tfidfTest[i], key=itemgetter(1), reverse=True)[:15]
            out.write(testNames[i] + " - ")
            for word in top15:
                out.write(dictionary[word[0]] + " ")
            out.write("\n")


def calcBookScores(books):
    texts = [[word.strip(",:;.?!") for word in document.lower().split()] for document in books]
    dictionary = corpora.Dictionary(texts)
    print(dictionary)
    corpus = [dictionary.doc2bow(text) for text in texts]
    tfidf = models.TfidfModel(corpus)
    tfidfList = list()
    for each in corpus:
        tfidfList.append(tfidf[each])
    salientByBook(tfidfList, dictionary)
    #calcLSI(tfidfList, dictionary)
    #calcLSA(corpus, dictionary)


def sortScore(tfidfList, dict):
    for i in range(len(tfidfList)):
        local10 = list()
        top10 = sorted(tfidfList[i], key=itemgetter(1), reverse=True)[:10]
        #print(*top10)
        print(bookNames[i])
        for word in top10:
            local10.append(dict[word[0]])
            print(dict[word[0]])

def salientByBook(tfidfList, dict): #basically the same as sortScore() but outputs to a file instead of printing
    with open ("salientByBook.txt", 'w') as out:
        out.write("The top 10 salient words in each book of the bible\n")
        for i in range(len(tfidfList)):
            local10 = list()
            top10 = sorted(tfidfList[i], key=itemgetter(1), reverse=True)[:10]
            #print(*top10)
            out.write(bookNames[i] + " - ")
            for word in top10:
                local10.append(dict[word[0]] )
                out.write(dict[word[0]] + " ")
            out.write("\n")


def calcLSI(tfidfList, dictionary):
    global corpus_lsi
    topics = 4 #this is arbitrary we should play around with this
    lsi = models.LsiModel(tfidfList, id2word=dictionary, num_topics = topics)
    corpus_lsi = lsi[tfidfList]
    lsi.print_topics(topics)
    #after this is new stuff to evaluate topics

def calcLSA(corpus, dictionary):
    model = models.LdaModel(corpus, id2word = dictionary, num_topics = 10)



if __name__ == "__main__":
    calcByBook()
    bookToTestament()
