import csv, collections

bookCount = dict()
with open('sermonDatasetCSV.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        bookStuff = row[0]
        realSplit = bookStuff.split(',')
        for bookThingy in realSplit:
            new = bookThingy.strip()
            contents = new.split(' ')
            if contents[0]!='1' and contents[0]!='2':
                bookName = contents[0]
                if bookName not in bookCount.keys():
                    bookCount[bookName] = 1
                else:
                    oldValue = bookCount[bookName]
                    bookCount[bookName] = oldValue + 1
            else:
                bookName = contents[0] + ' ' +contents[1]
                if bookName not in bookCount.keys():
                    bookCount[bookName] = 1
                else:
                    oldValue = bookCount[bookName]
                    bookCount[bookName] = oldValue + 1

consistencyCheck = 0
del bookCount['Song']
for book in bookCount.keys():
    consistencyCheck = consistencyCheck + bookCount[book]
print consistencyCheck

valdic = collections.OrderedDict(sorted(bookCount.items()))
print valdic

with open('bookCount.csv','wb') as myfile:
    current = csv.writer(myfile)
    current.writerows(valdic.items())
    myfile.close()




