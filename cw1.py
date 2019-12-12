import statistics

f = open("diabetes.txt", "r")
f2 = open("diabetes-type.txt", "r")

tab = {}
tab2 = {}

for x in f2:
    line = x
    line = line.strip()
    line = line.split(" ")
    tab2[line[0]] = line[1]

indexes = []
i = 0

for key in tab2:
    if tab2[key] == "n":
        indexes.append(i)
    i += 1

for x in f:
    line = x
    line = line.strip()
    line = line.split(" ")

    lineCopy = []
    n = 0
    for item in line:
        if n in indexes:
            lineCopy.append(float(item))
        else:
            lineCopy.append(item)
        n += 1
    line = lineCopy

    if line[-1] in tab:
        tab[line[-1]] = tab.get(line[-1]) + [line]
    else:
        tab[line[-1]] = [line]

for key in tab:
    print("{} - liczba obiektów w klasach: {}".format(key, len(tab[key])))

for index in indexes:
    listAttributes = []
    listAttributesByKey = {}

    for key in tab:
        listPom = []
        for value in tab[key]:
            listAttributes.append(value[index])
            listPom.append(value[index])
        listAttributesByKey[key] = listPom
        print("{} Max atrybutu - {}, Min atrybutu - {}".format("a{}".format(str(index + 1)), max(listAttributes),
                                          min(listAttributes)))

