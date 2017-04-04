import re

allWords = list()
verses = list()

def clean():
    #ensures each verse begins on its one line, separates each verse with newline if not already done in text
    with open("vedas.txt", 'r') as vedas, open('cleanedvedas.txt', 'w') as cleaned:
        for line in vedas:
                lineBreaks = False
                if re.match("^[0-9]*$",line[0]):
                    cleaned.write("\n")
                line = line.strip("\n")
                for i in range(6, len(line) - 1):
                    if (line[i].isdigit() or re.match("^[0-9]*$",line[i]) or line[i] == "6") and(line[i+1] == ":" or re.match("^[0-9]*$",line[i+1])): #sorry this is hardcoded, randomly one 6 wasnt making this conditional true idek
                        cleaned.write(line[:i] + "\n" + "\n" + line[i:] + " ")
                        lineBreaks = True
                        break
                if not lineBreaks and len(line) > 1:
                    cleaned.write(line + " ")

def parseVedas():
    with open("cleanedvedas.txt", 'r') as vedas, open('parsed_vedas.txt', 'w') as parsed:
        for line in vedas:
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

#format: 7|3|textofverse

def toTSV():
    with open("parsed_vedas.txt", 'r') as vedas, open('vedas.tsv', 'w') as tsv:
        line2 = " "
        tsv.write("Verse Number, Verse Text\n") #header for tsv
        for line in vedas:
            if line[0].isdigit():
                line = line.replace(",", "")
                line = line.replace("  ", " ")
                words = line.split()
                loc = line.find(" ")
                nums = line[:loc]
                tsv.write(nums + "\t" + line[loc+1:])
#            else:
#                if line2[0].isdigit():
#                    line = line.replace(",", "")
#                    words = line.split()
#                    nums = line[0]
#                    tsv.write(nums + "," + line)
#            line2 = line

clean()
parseVedas()
toTSV()
#print(sorted(set(allWords)))

#fixed the newline problem!
#fixing this I think will help with the vedas tsv column issue too
