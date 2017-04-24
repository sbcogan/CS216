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

############################################################################################################################################################################################
############################################################################################################################################################################################


big_ass_array_of_values = list(list())

with open("quran.tsv") as tsvfile:
	tsvreader = csv.reader(tsvfile, delimiter="\t")

	counter = 0
	for line in tsvreader:

#disable here to run full program
############################################################################################################################################################################################
############################################################################################################################################################################################

		if counter == 0:
			counter +=1
			continue
		# if counter >= 3:
		# 	break

############################################################################################################################################################################################
############################################################################################################################################################################################

		if counter%100 == 0:
			print counter

		row = [0,0,0,0,0,0,0,0,0,0,0]

	    	#assigns id to chapter number
		row[0] = line[0]

	    	#analyze text of chapter
		chapter_text = line[1]
		asjson = json.dumps(tone_analyzer.tone(chapter_text,sentences='false'), indent=2)
		parsed_json = json.loads(asjson)

	#assign scores to remaining ten values in row
		row[1] = parsed_json["document_tone"]['tone_categories'][0][u'tones'][0][u'score']
		row[2] = parsed_json["document_tone"]['tone_categories'][0][u'tones'][1][u'score']
		row[3] = parsed_json["document_tone"]['tone_categories'][0][u'tones'][2][u'score']
		row[4] = parsed_json["document_tone"]['tone_categories'][0][u'tones'][3][u'score']
		row[5] = parsed_json["document_tone"]['tone_categories'][0][u'tones'][4][u'score']
		row[6] = parsed_json["document_tone"]["tone_categories"][2][u'tones'][0][u'score']
		row[7] = parsed_json["document_tone"]["tone_categories"][2][u'tones'][1][u'score']
		row[8] = parsed_json["document_tone"]["tone_categories"][2][u'tones'][2][u'score']
		row[9] = parsed_json["document_tone"]["tone_categories"][2][u'tones'][3][u'score']
		row[10] = parsed_json["document_tone"]["tone_categories"][2][u'tones'][4][u'score']

		big_ass_array_of_values.append(row)
		counter += 1
	
with open('sentiment_data_quran.csv','w') as data:
	header = ['chapter','anger','disgust','fear','joy','sadness','openness','conscientiousness','extraversion','agreeableness',\
			'emotional_range']
	data.write(','.join(header) + '\n')
	for row in big_ass_array_of_values:
		for num in range(len(row)):
			value = row[num]
			row[num] = str(value)
		data.write(','.join(row) + '\n')

print big_ass_array_of_values