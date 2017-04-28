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
    with open("ASV.tsv", 'r') as bible, open('ASV_by_chapter.tsv', 'w') as tsv:
        #tsv.write(prev_book + "\t" + chap + "\t" + new_line + "\t" + str(length) + "\n")
        hardCode = ['Genesis','Exodus','Leviticus','Numbers','Deuteronomy','Joshua','Judges','Ruth','1 Samuel','2 Samuel','1 Kings','2 Kings','1 Chronicles','2 Chronicles','Ezra','Nehemiah','Esther','Job','Psalm','Proverbs','Ecclesiastes','Song','Isaiah','Jeremiah','Lamentations','Ezekiel','Daniel','Hosea','Joel','Amos','Obadiah','Jonah','Micah','Nahum','Habakkuk','Zephaniah','Haggai','Zechariah','Malachi','Matthew','Mark','Luke','John','Acts','Romans','1 Corinthians', '2 Corinthians','Galatians','Ephesians','Philippians','Colossians','1 Thessalonians','2 Thessalonians','1 Timothy','2 Timothy','Titus','Philemon','Hebrews','James','1 Peter','2 Peter','1 John','2 John','3 John','Jude','Revelation']
        makeShiftDict = dict()
        for row in bible:
            currentEntry = row.split('\t')
            currentBook = currentEntry[0]
            currentChap = currentEntry[1]
            currentText = currentEntry[3]
            dictEntry = currentBook + ' ' + currentChap
            currentText = currentText.strip('\n')
            if dictEntry not in makeShiftDict.keys():
                makeShiftDict[dictEntry] = currentText
            else:
                oldText = makeShiftDict[dictEntry]
                makeShiftDict[dictEntry] = oldText + ' ' + currentText

        for book in hardCode:
            loopNum = 1
            lookUp = book + ' ' + str(loopNum)
            count = 0
            while lookUp in makeShiftDict.keys():
                for word in makeShiftDict[lookUp].split(' '):
                    #print word
                    if len(word)>0:
                        count = count + 1
                tsv.write(book + "\t" + str(loopNum) + "\t" + makeShiftDict[lookUp] + "\t" + str(count) + "\n")
                del makeShiftDict[lookUp]
                loopNum = loopNum + 1
                lookUp = book + ' ' + str(loopNum)
                count = 0

        if len(makeShiftDict.keys())!=0:
            print 'Uh oh spaghetti o'

clean()
parseASV()
toTSV()
toTSV2()
