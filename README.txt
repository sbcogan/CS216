In order to recreate the results of our sentiment analysis, one would run the following programs:
UPATED_parse_asv.py
bible_sentiment.py
parse_quran.py
quran_sentiment.py
SermonCentraltoCSV.py
sermon_sentiment.py
ungrouped_sermon_sentiment.py
sermon_graphing.R
Multi_Radial.R
Radial Plot.R
tSNE.R

The programs for the social network graphs and salient word analysis are:
NounParse.py
Nodes.py
Bible_Cooccurences.py
Circle20Bible.R
SocialNetBible.R
newTFIDF.py

Each file takes data as input and either writes data as output or returns graphs, so it is only necessary to alter file-paths to run through the appropriate directories on your own computer. That is, running the program will generate the output files. Successful runs of these files assume a prior installation of the BeautifulSoup and gensim libraries. A number of libraries are also required for the R scripts, though these are easily obtained within RStudio. Our .zip includes all necessary data.