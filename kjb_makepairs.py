import csv
from nltk.tag import pos_tag
#creates word pairs csv by cooccurence by verse
with open("kingjames.tsv") as tsvfile, open("kjb_cleanedpairs.csv",'wb') as f:
    biblebyverse = list()
    extraneous = ['wherefore','verily','where','the','thus','ye','therefore','and','yeah','said','lo','behold', 'whence','thy','king','and', 'come', 'let', 'be', 'for', 'go', 'say', 'speak', 'thou', 'you', 'shall', 'a', 'of','amen', 'o','kings','saying']
    extraneous.extend(['yea','my', 'ah','hearken','return','take','i', 'see','fear','son', 'nay','holy','ner','arise','spirit', 'wherefore','who'])
    extraneous.extend(['did', 'get', 'whosoever','remember', 'where', 'how', 'woe', 'hast', 'know', 'so', 'hear', 'praise', 'almighty', 'turn', 'surely', 'unto'])    
	
    for line in tsvfile:
        line = line.strip('\n')
        line = line.split('\t')
        propernouns = list()
        text =  pos_tag(line[3].split())
        for tup in text:
                if tup[1] == 'NNP' and tup[0].lower().replace("'s", '').strip(",;.:)?'") not in extraneous:
			if tup[0].lower().replace("'s", '').strip(",;.:)?'") == "lord":
				propernouns.append("God") 
                	#if tup[0].lower().strip(",;.:)?'") == "god":
			#	propernouns.append("God")
			#if tup[0].lower().replace("'s",'').strip(",;.:)?'") == "christ":
			#	propernouns.append("Jesus") 
			else: 
				propernouns.append(tup[0].replace("'s",'').strip(",;.:)?'"))
 
        unique = set(propernouns)
        if len(list(unique)) > 1:
                biblebyverse.append((line[0],line[1],line[2],list(unique)))
    wordpairs = list()
    for verse in biblebyverse:
        uniquepairs = set()
        for word1 in verse[3]:
                for word2 in verse[3]:
                        if word1 != word2:
                                plist =sorted([word1, word2])
                                pair = tuple(plist)
                                uniquepairs.add(pair)
        versenum = verse[0] + " " + verse[1] + ":" + verse[2]
        for pair in uniquepairs:
                wordpairs.append([pair[0],pair[1],1,versenum])

    writer = csv.writer(f, delimiter=',', lineterminator='\n')
    writer.writerows(wordpairs)

for line in wordpairs:
        print(line)
