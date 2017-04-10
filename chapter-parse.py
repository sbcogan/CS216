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
                    if (line[i].isdigit() or re.match("^[0-9]*$",line[i]) or line[i] == "6") and(line[i+1] == ":" or re.match("^[0-9]*$",line[i+1])): #sorry this is hardcoded, randomly one 6 wasnt making this conditional true idek
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

def toTSV():
    with open("parsed.txt", 'r') as bible, open('kingjames.tsv', 'w') as tsv:
        tsv.write("Book\t Chapter\t Verse Number\t Verse Text\n") #header for csv
        book = ""
        someBookTitles = ["Hosea", "Ezra", "Joel", "Amos", "Obadiah", "Jonah", \
        "Micah", "Nahum", "Habakkuk", "Zephaniah", "Haggai", "Zechariah", "Malachi"]
        for lno, line in enumerate(bible):
            #if lno < 29:
                #continue
            if 'End of the Project Gutenberg EBook of The King James Bible' in line:
                break
            if line[:4] == "The " and not line[4].islower():
                book = line[:len(line) -1].strip()
                continue
            breakcondition = False
            for title in someBookTitles:
                if line.startswith(title):
                    book = line.strip("\n")
                    breakcondition = True
                    break
            if breakcondition:
                continue
            if line.find(":") > -1:
                words = line.split()
                nums = words[0].split(":")
                tsv.write(book + "\t" + nums[0] + "\t" + nums[1] + "\t" + line[len(words[0]) + 1:])



clean()
parseJames()
toTSV()
#print(sorted(set(allWords)))

#fixed the newline problem!
#fixing this I think will help with the bible csv column issue too
