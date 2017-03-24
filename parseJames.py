import re

allWords = list()
verses = list()

def clean():
    #ensures each verse begins on its one line, separates each verse with newline if not already done in text
    with open("kingjames.txt", 'r') as bible, open('cleanedBible.txt', 'w') as cleaned:
        for line in bible:
                lineBreaks = False
                for i in range(5, len(line)):
                    if line[i].isnumeric():
                        cleaned.write(line[:i] + "\n" + "\n" + line[i:])
                        lineBreaks = True
                        break
                if not lineBreaks:
                    cleaned.write(line)

def parseJames():
    with open("cleanedBible.txt", 'r') as bible, open('parsed.txt', 'w') as parsed:
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

            #need to check for chars like dashes, apostraphes, etc. (wouldn't otherwise evaluate to true with isalpha)

def uniqueWords():
    print(len(set(allWords)))

def numWords():
    print(len(allWords))

clean()
parseJames()



