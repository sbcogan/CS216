

import json
import csv
from watson_developer_cloud import ToneAnalyzerV3

##craft a matrix of values with different chapters as rows and book, chapter, anger, disgust, fear, joy, sadness, openness, 
## conscientiousness, extraversion, agreeableness, and emotional range (in that order) as the columns

############################################################################################################################################################################################
############################################################################################################################################################################################
#change this section to match the username, password and version of the tone analyzer you are using
tone_analyzer = ToneAnalyzerV3(
   username="46ad7679-dfc6-4412-9b7e-f49e6e193ee4",
   password="ChqPL3LDbmf1",
   version='2016-05-19 ',
   )

big_ass_array_of_values = list(list())
############################################################################################################################################################################################
############################################################################################################################################################################################


with open("SermonDatasetCSV.csv") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")

	counter = 1
	for line in csvreader:

#disable here to run full program
############################################################################################################################################################################################
############################################################################################################################################################################################
		# if counter == 0:
		# 	continue
		# if counter >= 3:
		# 	break
############################################################################################################################################################################################
############################################################################################################################################################################################
#and enable here
		if counter%100 == 0:
			print counter

		row = [0,"","","",0,0,0,0,0,0,0,0,0,0]
		row[0] = counter
		# print line[0]
		# print len(line)
		different_references = line[0].split(",")
		for j in range(len(different_references)):
			split=different_references[j].split(" ")
			items = len(split)
			for i in range(items-1):
				row[1] = row[1] + str(split[i]) + " "
			row[1]=row[1].strip()
			row[2] = row[2] + split[items-1][:split[items-1].find(":")]
			row[2]=row[2].strip()
			if j != len(different_references)-1:
				row[1]+= ", "
				row[2]+=", "
		row[3] = line[2]
		chapter_text = line[3]
		asjson = json.dumps(tone_analyzer.tone(chapter_text,sentences='false'), indent=2)
		parsed_json = json.loads(asjson)

		row[4] = parsed_json["document_tone"]['tone_categories'][0][u'tones'][0][u'score']
		row[5] = parsed_json["document_tone"]['tone_categories'][0][u'tones'][1][u'score']
		row[6] = parsed_json["document_tone"]['tone_categories'][0][u'tones'][2][u'score']
		row[7] = parsed_json["document_tone"]['tone_categories'][0][u'tones'][3][u'score']
		row[8] = parsed_json["document_tone"]['tone_categories'][0][u'tones'][4][u'score']
		row[9] = parsed_json["document_tone"]["tone_categories"][2][u'tones'][0][u'score']
		row[10] = parsed_json["document_tone"]["tone_categories"][2][u'tones'][1][u'score']
		row[11] = parsed_json["document_tone"]["tone_categories"][2][u'tones'][2][u'score']
		row[12] = parsed_json["document_tone"]["tone_categories"][2][u'tones'][3][u'score']
		row[13] = parsed_json["document_tone"]["tone_categories"][2][u'tones'][4][u'score']

		big_ass_array_of_values.append(row)
		counter += 1

with open('sentiment_data_sermons.tsv','w') as data:
	header = ['id','book','chapter','denomination','anger','disgust','fear','joy','sadness','openness','conscientiousness','extraversion','agreeableness',\
			'emotional_range']
	data.write('\t'.join(header) + '\n')
	for row in big_ass_array_of_values:
		for num in range(len(row)):
			value = row[num]
			row[num] = str(value)
		data.write('\t'.join(row) + '\n')

print big_ass_array_of_values
