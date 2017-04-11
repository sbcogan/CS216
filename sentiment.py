

import json
import csv
from watson_developer_cloud import ToneAnalyzerV3

##craft a matrix of values with different chapters as rows and book, chapter, anger, disgust, fear, joy, sadness, openness, 
## conscientiousness, extraversion, agreeableness, and emotional range (in that order) as the columns
tone_analyzer = ToneAnalyzerV3(
   username="46ad7679-dfc6-4412-9b7e-f49e6e193ee4",
   password="ChqPL3LDbmf1",
   version='2016-05-19 ',
   )

big_ass_array_of_values = list(list())



with open("kingjames.tsv") as tsvfile:
	tsvreader = csv.reader(tsvfile, delimiter="\t")

	counter = 0
	for line in tsvreader:
		if counter == 0:
			counter +=1
			continue
		if counter >= 5:
			break

		row = ["",0,0,0,0,0,0,0,0,0,0,0]

	    	#assigns first two items in each row to the name and chapter of the books
		row[0] = line[0]
		row[1] = line[1]

	    	#analyze text of chapter
		chapter_text = line[2]
		asjson = json.dumps(tone_analyzer.tone(chapter_text,sentences='false'), indent=2)
		parsed_json = json.loads(asjson)

	#assign scores to remaining ten values in row
		row[2] = parsed_json["document_tone"]['tone_categories'][0][u'tones'][0][u'score']
		row[3] = parsed_json["document_tone"]['tone_categories'][0][u'tones'][1][u'score']
		row[4] = parsed_json["document_tone"]['tone_categories'][0][u'tones'][2][u'score']
		row[5] = parsed_json["document_tone"]['tone_categories'][0][u'tones'][3][u'score']
		row[6] = parsed_json["document_tone"]['tone_categories'][0][u'tones'][4][u'score']
		row[7] = parsed_json["document_tone"]["tone_categories"][2][u'tones'][0][u'score']
		row[8] = parsed_json["document_tone"]["tone_categories"][2][u'tones'][1][u'score']
		row[9] = parsed_json["document_tone"]["tone_categories"][2][u'tones'][2][u'score']
		row[10] = parsed_json["document_tone"]["tone_categories"][2][u'tones'][3][u'score']
		row[11] = parsed_json["document_tone"]["tone_categories"][2][u'tones'][4][u'score']

		big_ass_array_of_values.append(row)
		counter += 1
	
with open('sentiment_data.csv','w') as data:
	header = ['book','chapter','anger','disgust','fear','joy','sadness','openness','conscientiousness','extraversion','agreeableness',\
			'emotional_range']
	data.write(','.join(header) + '\n')
	for row in big_ass_array_of_values:
		for num in range(len(row)):
			value = row[num]
			row[num] = str(value)
		data.write(','.join(row) + '\n')

print big_ass_array_of_values