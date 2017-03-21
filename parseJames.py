import re

allWords = list()
verses = list()

def parseJames():
    with open("kingjames.txt", 'r') as bible, open('parsed.txt', 'w') as parsed:
        for line in bible:
            getWords(line)
            parsed.write(line)

def getWords(line):
    words = line.split()
    if len(words) > 0:
        if re.match("^[0-9:]*$",words[0]):
            verse = words[0]
            verses.append(verse)
    for i in range(len(words)):
        if words[i].isalpha():
            allWords.append(words[i])

            #check for chars like dashes, apostraphes, etc. (wouldn't otherwise evaluate to true with isalpha)

def uniqueWords():
    print(len(set(allWords)))

def numWords():
    print(len(allWords))

parseJames()
for verse in verses:
    print(verse)

