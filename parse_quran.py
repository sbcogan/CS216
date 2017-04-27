import re

allWords = list()
verses = list()

def clean():
    #ensures each verse begins on its one line, separates each verse with newline if not already done in text
    with open("quran.txt", 'r') as quran, open('cleanedQuran.txt', 'w') as cleaned:
        for line in quran:
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

def parseQuran():
    with open("cleanedQuran.txt", 'r') as quran, open('parsed_quran.txt', 'w') as parsed:
        for line in quran:
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

#format: chap|verse_num|textofverse
def toTSV():
    #next_line = ""
    next_line = []
    chap_int = 0
    former_num = 1
    length = 0
    count = 0
    with open("parsed_quran.txt", 'r') as quran, open('quran.tsv', 'w') as tsv:
        #tsv.write("Chapter, Verse Number, Verse Text\n") #header for csv
        tsv.write("Chapter, Verse Text, Length\n") #header for csv
        for line in quran:
            if line.find("|") > -1:
                #line = line.replace(",", "")
                words = line.split("|")
                #print words
                chap_int = int(words[0])
                chap = words[0]
                verse = words[1]
                text = words[2]
                text = text.replace('\n','')
                if chap_int == former_num:
                    #next_line = next_line + text
                    next_line.append(text)
                if chap_int != former_num:
                    #tsv.write(str(former_num) + "\t" + next_line
                    for item in next_line:
                        item = item[:-1]
                    for i in next_line:
                        for x in  i.split():
                            length += 1
                    next_line = " ".join(next_line)
                    tsv.write(str(former_num) + "\t" + next_line + "\t" + str(length) + "\n")
                    #print next_line
                    #next_line = ""
                    #next_line = text
                    #print next_line
                    next_line = []
                    next_line.append(text)
                    length = 0

                former_num = chap_int

                if chap_int == 114:
                    if verse == "6":
                        #tsv.write(str(former_num) + "\t" + next_line)
                        for i in next_line:
                            for x in i.split():
                                length += 1
                        tsv.write(str(former_num) + "\t" + " ".join(next_line) + "\t" + str(length))
                        next_line = []

                #nums = words[0].split("|")
                #print(line)
                #if len(nums) >= 2 and len(words) > 2:
                    #csv.write(nums[0] + "\t" + nums[1] + "\t" + line[len(words[0]) + 1:])
                #tsv.write(chap + "\t" + verse + "\t" + text)

clean()
parseQuran()
toTSV()
#print(sorted(set(allWords)))

#fixed the newline problem!
#fixing this I think will help with the quran tsv column issue too
