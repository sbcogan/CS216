with open("ASV2.tsv") as tsvfile, open("ASV2_by_book.tsv",'w') as wfile:
    biblebybook = list()
    newrow = [""]*2
    counter = 0
    for line in tsvfile:
        line = line.strip('\n')
        line = line.split('\t')
        if line[1] == '1' and counter > 1: #when new book, dump the row into biblebychapter (exception: first row)
            biblebybook.append(newrow)
            newrow = [""]*2
        if line[1] == '1': #when new book, grab book title
            newrow[0] = line[0]
        newrow[1] = newrow[1] + line[2] #accumulate chapters
        if counter == 1183: #edge case: append Revelations
            biblebybook.append(newrow)
        counter += 1
    wfile.write('\t'.join(['Book','Text']) + '\n')
    counter = 0
    for row in biblebybook: #write to new tsv
        counter += 1
        wfile.write('\t'.join(row) + '\n')
