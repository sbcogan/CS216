#mostly playing around with the gensim library, idk how much of this will be useful

import logging
from gensim import corpora, models, similarities
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def tutorial():
    documents = ["human human human human machine interface", \
    "A survey of user opinion of machine system"]

    stoplist = set('for a of the and to in'.split())
    texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

    ''' 
    #i dont care to remove the words that only occur once
    from collections import defaultdict
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1
    '''

    dictionary = corpora.Dictionary(texts)
    print(dictionary)
    #print(dictionary.token2id)

    corpus = [dictionary.doc2bow(text) for text in texts]
    #print(corpus)

    tfidf = models.TfidfModel(corpus)
    for text in corpus:
        print(tfidf[text])


    corpus_tfidf = tfidf[corpus]
    for doc in corpus_tfidf:
        print(doc)


#everything before this was playing with the tutorial
#everything after this is hopefully applicable to our data set!


def parseGenesis():
    docs2 = list()
    with open('kingjames.csv', 'r') as csv:
        for line in csv:
            if line.startswith("The First Book of Moses"):
                verse = line.split(",")[3]
                print(verse)
                docs2.append(verse)
    dictionary2 = corpora.Dictionary(docs2)
    print(dictionary2)
    corpus2 = [dictionary2.doc2bow(text) for text in docs2]
   # print(corpus2)
    print(len(corpus2))
    tfidf2 = models.TfidfModel(corpus2)
    #for each in corpus2:
        #print(tfidf2[each])

#parseGenesis();


def calcByBook():
    books = list()
    curBook = "x"
    with open('kingjames.csv', 'r') as csv:
        counter = -1 #lol there's probably a better way to do this but this should work!
        for line in csv:
            verse = line.split(",")[3]
            if  verse.strip().startswith("Verse Text"): #hard coded, ignoring header line
                print("first line")
                continue
            if  not line.startswith(curBook):
                counter += 1
                books.append("")
                curBook = line.split(",")[0]
            books[counter] += " " + verse
    #for book in books:
        #print(book)
    print(len(books)) #this says there are 53 books which I thought seemed high but the titles all seem reasonable(?) 
    calcScores(books)


def calcScores(books):
    texts = [[word for word in document.lower().split()] for document in books]
    dictionary = corpora.Dictionary(texts)
    print(dictionary)
    corpus = [dictionary.doc2bow(text) for text in texts]
    tfidf = models.TfidfModel(corpus)
    for each in corpus:
        print(tfidf[each])

    #action items: sort by SECOND element in tuple (highest TFIDF score listed first)
    #then convert back from id to token
    #remember to go back and strip of extraneous chars like :
calcByBook();