with open("kingjames.tsv") as tsvfile, open("kingjames_bychapter.tsv",'w') as wfile:
    biblebychapter = list()
    newrow = [""]*3
    counter = 0
    for line in tsvfile:
        if counter == 0:
            counter += 1
            continue
        line = line.strip('\n')
        line = line.split('\t')
        if line[2] == '1' and counter > 1: #when new chapter, dump the row into biblebychapter (exception: first row)
            biblebychapter.append(newrow)
            newrow = [""]*3
        if line[2] == '1': #when new chapter, grab book title and chapter number
            newrow[0] = line[0]
            newrow[1] = line[1]
        newrow[2] = newrow[2] + line[3] #accumulate verses
        if counter == 31009: #edge case: append Revelations 22
            biblebychapter.append(newrow)
        counter += 1
    wfile.write('\t'.join(['Book','Chapter','Text']) + '\n')
    for row in biblebychapter: #write to new tsv
        wfile.write('\t'.join(row) + '\n')


with open("kingjames_bychapter.tsv") as tsvfile, open("kingjames_bybook.tsv",'w') as wfile:
    biblebybook = list()
    newrow = [""]*2
    counter = 0
    for line in tsvfile:
        if counter == 0:
            counter += 1
            continue
        line = line.strip('\n')
        line = line.split('\t')
        if line[1] == '1' and counter > 1: #when new book, dump the row into biblebychapter (exception: first row)
            biblebybook.append(newrow)
            newrow = [""]*2
        if line[1] == '1': #when new book, grab book title
            newrow[0] = line[0]
            print line[0],line[1]
        newrow[1] = newrow[1] + line[2] #accumulate chapters
        if counter == 1188: #edge case: append Revelations
            biblebybook.append(newrow)
        counter += 1
    wfile.write('\t'.join(['Book','Text']) + '\n')
    counter = 0
    for row in biblebybook: #write to new tsv
        counter += 1
        wfile.write('\t'.join(row) + '\n')
