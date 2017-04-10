#Scrape web data from sermoncentral.com
#Associate proper tags to data
#Put data into usable TSV file
########################################
from bs4 import BeautifulSoup
import csv
import urllib2

global sermonDataset
sermonDataset = dict()

def openURL(url):
    response = None
    request = urllib2.Request(url=url)
    try:
        response = urllib2.urlopen(request)
    except IOError:
        repsonse = 'BAD'
    return response

def formingTheDataSet(currentURLIndex):
    pageNumber = 1
    seenLines = set()
    text = ''
    scriptureLabel = 'Scripture:'
    tagLabel = 'Tags:'
    denominationLabel = 'Denomination:'
    strip1 = 'Nobody has commented yet. Be the first!'
    strip2 = 'Enter your email address and we will send you a link to reset your password.'
    strip3 = 'View More Preaching Articles'
    suggestScripture = '(suggest scripture)'
    suggestTag = '(suggest tag)'
    if (currentURLIndex not in sermonDataset):
        sermonDataset[currentURLIndex] = []
    while (pageNumber < 6):
        yoWeMadeTheLoopCount = 0
        currentPage = 'https://www.sermoncentral.com/sermons/what-most-christians-dont-know-barry-o-johnson-sermon-on-ephesus-'+str(currentURLIndex)+'?page='+str(pageNumber)
        response = openURL(currentPage)
        while (response == None):
            print 'YO WE MADE THE LOOP'
            if (yoWeMadeTheLoopCount == 4):
                return 'PAGE PROBABLY DOESNT EXIST, BUT IF IT DOES THERE ARE STILL 207000 OTHERS'
            currentPage = 'https://www.sermoncentral.com/sermons/what-most-christians-dont-know-barry-o-johnson-sermon-on-ephesus-'+str(currentURLIndex)+'?page='+str(pageNumber)
            yoWeMadeTheLoopCount = yoWeMadeTheLoopCount + 1
            response = openURL(currentPage)
        soup = BeautifulSoup(response.read(),'lxml')
        for i in range(len(soup.find_all('p'))):
            currentLine = soup.find_all('p')[i].get_text()
            if (scriptureLabel in currentLine):
                startIndex = currentLine.find(scriptureLabel)
                scriptureOut = startIndex + len(scriptureLabel)
                tempString = currentLine[scriptureOut:]
                stopIndexPlusOne = tempString.find(suggestScripture)
                stopIndex = stopIndexPlusOne-1
                actualBookandChapter = (tempString[2: stopIndex]).encode('utf-8')
                if (actualBookandChapter not in sermonDataset[currentURLIndex]):
                    sermonDataset[currentURLIndex].append(actualBookandChapter)
            if (tagLabel in currentLine):
                startTagIndex = currentLine.find(tagLabel)
                tagOut = startIndex + len(tagLabel)
                tempTagString = currentLine[tagOut:]
                stopIndexTagPlusOne = tempTagString.find(suggestTag)
                stopIndexTag = stopIndexTagPlusOne - 1
                actualTags = tempTagString[2:stopIndexTag]
                stringToConvert = (actualTags).encode('utf-8')
                actualTagsTuple = tuple(stringToConvert.split(", "))
                if (actualTagsTuple not in sermonDataset[currentURLIndex]):
                    sermonDataset[currentURLIndex].append(actualTagsTuple)
            if (denominationLabel in currentLine):
                startIndex = currentLine.find(denominationLabel)
                denominationOut = startIndex + len(denominationLabel)
                denominationCurrent= currentLine[denominationOut:]
                denomationTemp = (denominationCurrent[:-1])
                denomationTemp = denomationTemp[2:]
                denomation = (denomationTemp).encode('utf-8')
                if (denomation not in sermonDataset[currentURLIndex]):
                    sermonDataset[currentURLIndex].append(denomation)
            if (currentLine in seenLines):
                pass
            else:
                if (len(currentLine) == 0):
                    pass
                else:
                    if (strip1 in currentLine or strip2 in currentLine or strip3 in currentLine or scriptureLabel in currentLine or tagLabel in currentLine or denominationLabel in currentLine):
                        pass
                    else:
                        text = text + " " + currentLine.encode('utf-8')
                        seenLines.add(currentLine)
        pageNumber = pageNumber + 1
    text = text.replace('\xe2\x80\x99',"'")
    text = text.replace('\xe2\x80\x9d','"')
    text = text.replace('\xe2\x80\x9c','"')
    text = text.replace('\xe2\x80\x93', '-')
    text = text.replace('\xe2\x80\x94', '--')
    text = text.replace('\xe2\x80\x98', "'")
    text = text.replace('\xe2\x80\xa6', "...")
    text = text.replace("\'","'")
    text = text.replace('\xe2\x80\xa2', '"')
    sermonDataset[currentURLIndex].append(text)
    
    if (len(sermonDataset[currentURLIndex])!=4):
        sermonDataset.pop(currentURLIndex)
        return sermonDataset
    elif ("\xe2" in text or "\xc2" in text):
        sermonDataset.pop(currentURLIndex)
        return sermonDataset
    elif (sermonDataset[currentURLIndex][0] == 'None'):
        sermonDataset.pop(currentURLIndex)
        return sermonDataset
    elif (sermonDataset[currentURLIndex][1] == ('None',)):
        sermonDataset.pop(currentURLIndex)
        return sermonDataset
    elif (sermonDataset[currentURLIndex][0] == ''):
        sermonDataset.pop(currentURLIndex)
        return sermonDataset
    elif (len(sermonDataset[currentURLIndex][3]) < 100):
        sermonDataset.pop(currentURLIndex)
        return sermonDataset
    elif (sermonDataset[currentURLIndex][2] == '*other'):
        sermonDataset.pop(currentURLIndex)
        return sermonDataset
    else:
        return sermonDataset

def startHere():
    currentURLIndex = 205000
    while (len(sermonDataset)<1000):
        formingTheDataSet(currentURLIndex)
        print currentURLIndex
        currentURLIndex = currentURLIndex + 1
    
    createCSVArray = []
    for entry in sermonDataset.keys():
        if (len(sermonDataset[entry])!=0):
            createCSVArray.append(sermonDataset[entry])
    with open('sermonDatasetCSV','wb') as myfile:
        current = csv.writer(myfile)
        current.writerows(createCSVArray)
    myfile.close()

if __name__ == "__main__":
    startHere()

