def readFile(filename):
    list_strings = []
    file = open(filename, 'r')
    for line in file:
        if (line[0] != '#'):
            list_strings.append(line.rstrip())
    file.close()
    return list_strings

def generateAdjacencyList(filename="train-graph-1.txt"):
    list_3tuple = []
    for string in readFile(filename):
        list_3tuple.append((string[0], string[1], float(string[2:])))
    return list_3tuple