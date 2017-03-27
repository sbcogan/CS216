mapping = list()
def hw9():
    with open("states_counts.txt", 'r') as file, open("output9.txt", 'w') as out:
        gender = False
        counter = 0
        for line in file:
            if line[0].islower():
                gender = True
                continue
            line = line.split("|")
            state = line[0] .strip()
            if line[0] == '\n':
                break
            count = float(line[1].strip())
            if not gender:
                print(line)
                mapping.append([state, count])
                counter += 1
            else:
                for i in range(len(mapping)):
                    if mapping[i][0] == state:
                        mapping[i][1]  =  count/mapping[i][1]
    for line in mapping:
        if line[1] >= 1:
            line[1] = 0

hw9()
for line in mapping:
    print(str(line[0]) + ' ' + str(line[1]))
