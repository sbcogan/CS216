import csv, collections

bookCount = dict()
with open('sermonDatasetCSV.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        bookStuff = row[0]
        new = bookStuff.split(',')
        for thing in new:
            new2 = thing.strip()
            contents = new2.split(' ')
            if contents[0]!='1' and contents[0]!='2':
                bookName = contents[0]
                chapterVerse = contents[1].split(':')
                bookChap = contents[0] + ' ' + chapterVerse[0]
                if bookChap not in bookCount.keys():
                    bookCount[bookChap] = 1
                else:
                    oldValue = bookCount[bookChap]
                    bookCount[bookChap] = oldValue + 1
            else:
                chapterVerse = contents[2].split(':')
                bookChap = contents[0] + ' ' +contents[1] + ' ' + chapterVerse[0]
                if bookChap not in bookCount.keys():
                    bookCount[bookChap] = 1
                else:
                    oldValue = bookCount[bookChap]
                    bookCount[bookChap] = oldValue + 1

consistencyCheck = 0
del bookCount['Song of']
for book in bookCount.keys():
    consistencyCheck = consistencyCheck + bookCount[book]
print consistencyCheck

valdic = collections.OrderedDict(sorted(bookCount.items()))
print valdic

with open('bookAndChapterCount.csv','wb') as myfile:
    current = csv.writer(myfile)
    current.writerows(valdic.items())
    myfile.close()




