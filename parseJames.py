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
            parsed.write(line + "\n")

def getWords(line):
    words = line.split()
    if len(words) > 0:
        if re.match("^[0-9:]*$",words[0]):
            verse = words[0]
            verses.append(verse)
        for i in range(1, len(words)):
            allWords.append(words[i].strip(",:;.?!"))

            #strips of some chars -- how to deal w apostrophes still not decided

def uniqueWords():
    print(len(set(allWords)))

def numWords():
    print(len(allWords))

def toCSV():
    with open("parsed.txt", 'r') as bible, open('kingjames.csv', 'w') as csv:
        csv.write("Book, Chapter, Verse Number, Verse Text\n") #header for csv
        book = ""
        for line in bible:
            if len(line) > 0 and not line[0].isnumeric():
                if line[0] != "" and line[0] != "\n" and line[0] != " ":
                    book = line
                    print(book)
                continue
            line = line.replace(",", "")
            words = line.split()
            nums = words[0].split(":")
            csv.write(book + "," + nums[0] + "," + nums[1] + "," + line[len(words[0]) + 1:])

clean()
parseJames()
toCSV()
#print(sorted(set(allWords)))

#need to ignore line breaks in the original and only add them in at end of verse
#fixing this I think will help with the bible csv column issue too

