import re

allWords = list()
verses = list()

def clean():
    #ensures each verse begins on its one line, separates each verse with newline if not already done in text
    with open("asv.txt", 'r') as bible, open('cleanedASV.txt', 'w') as cleaned:
        for line in bible:
                lineBreaks = False
                if re.match("^[0-9]*$",line[0]):
                    cleaned.write("\n")
                line = line.strip("\n")

                if not lineBreaks and len(line) > 1:
                    cleaned.write(line + " ")

def parseASV():
    with open("cleanedASV.txt", 'r') as bible, open('parsed_asv.txt', 'w') as parsed:
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

def uniqueWords():
    print(len(set(allWords)))

def numWords():
    print(len(allWords))

def toTSV():
    with open("parsed_asv.txt", 'r') as bible, open('ASV.tsv', 'w') as tsv:
        #tsv.write("Book \t Chapter \t Verse Number \t Verse Text\n") #header for tsv
        book = ""
        chap = ""
        # chap_count = 0
        # verse_num = ""
        count = 0
        count_book = 0
        chap_prev = ""
        chap = ""
        for line in bible:
            line = line.lstrip()
            line = line.replace("__________________________________________________________________", "")
            line = line.replace("    ", " ")
            thing = 0
            thing2 = 0
            verse = ""
            #chap = ""
            text = ""
            line2 = []
            #print line[0:2]

            chap = chap_prev

            if line[0] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                for char in line:
                    if char =="^":
                        thing = 1
                    if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                        thing2 = 1
                    if char in "0123456789":
                        if thing == 0:
                            chap += char
                        if thing2 == 0:
                            if thing == 1:
                                verse += char
                    if thing == 1:
                        if thing2 == 1:
                            text += char

            chap_prev = chap

            if verse == "":
                for x in line:
                    if x in "123456789":
                        count_book += 1
                        if count_book == 1:
                            line2 = line.split()
                            if line2[0] in "1234567890":
                                book = " ".join(line2[0:2])
                                chap_prev = ""
                            else:
                                book = line2[0]
                                chap_prev = ""
            count_book = 0
            if text != "":
                if verse != "":
                    tsv.write(book + "\t" + chap + "\t" + verse + "\t" + text)

def toTSV2():
    with open("ASV.tsv", 'r') as bible, open('ASV2.tsv', 'w') as tsv:
        count = 0
        new_line = []
        prev_chap = "1"
        prev_book = "Genesis"
        for line in bible:
            count += 1
            line2 = line.split("\t")

            book = line2[0]
            chap = line2[1]
            verse = line2[2]
            text = line2[3]
            text = text.replace('\n','')

            if prev_chap == chap:
                new_line.append(text)
                prev_chap = chap
                prev_book = book
            else:
                new_line = " ".join(new_line)
                tsv.write(prev_book + "\t" + prev_chap + "\t" + new_line + "\n")
                new_line = []
                new_line.append(text)
                prev_chap = chap
                prev_book = book

            if book == "Revelation":
                if chap == "22":
                    if verse == "21":
                        new_line.append(text)
                        new_line = " ".join(new_line)
                        tsv.write(prev_book + "\t" + chap + "\t" + new_line + "\n")

clean()
parseASV()
toTSV()
toTSV2()
