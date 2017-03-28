import re

allWords = list()
verses = list()

def clean():
    #ensures each verse begins on its one line, separates each verse with newline if not already done in text
    with open("kingjames.txt", 'r') as bible, open('cleanedBible.txt', 'w') as cleaned:
        for line in bible:
                lineBreaks = False
                if re.match("^[0-9]*$",line[0]):
                    cleaned.write("\n")
                line = line.strip("\n")
                for i in range(6, len(line) - 1):
                    if (line[i].isnumeric() or re.match("^[0-9]*$",line[i]) or line[i] == "6") and(line[i+1] == ":" or re.match("^[0-9]*$",line[i+1])): #sorry this is hardcoded, randomly one 6 wasnt making this conditional true idek     
                        cleaned.write(line[:i] + "\n" + "\n" + line[i:] + " ")
                        lineBreaks = True
                        break
                if not lineBreaks and len(line) > 1:
                    cleaned.write(line + " ")


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
            if line[:4] == "The ":
                book = line[:len(line) -1].strip()
                continue
            if line.find(":") > -1:
                line = line.replace(",", "")
                words = line.split()
                nums = words[0].split(":")
                print(line)
                csv.write(book + "," + nums[0] + "," + nums[1] + "," + line[len(words[0]) + 1:])
                
#updates: yay!! csv file looks damn good


clean()
parseJames()
toCSV()
#print(sorted(set(allWords)))

#fixed the newline problem!
#fixing this I think will help with the bible csv column issue too

'''
def test():
    line ="6:51 Bukki his son Uzzi his son Zerahiah his son 6:52 Meraioth h"
    for i in range(6, len(line) - 1):
        if line[i].isnumeric() or re.match("^[0-9]*$",line[i]) or line[i] == "6" or line[i+1] == ":": 
            print(line[i])
test()
'''
