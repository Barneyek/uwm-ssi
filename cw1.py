import statistics

f = open("diabetes.txt", "r")
f2 = open("diabetes-type.txt", "r")

dictionary = {}
dictionary2 = {}

for x in f2:
    line = x
    line = line.strip()
    line = line.split(" ")
    dictionary2[line[0]] = line[1]

indexes = []
i = 0

for key in dictionary2:
    if dictionary2[key] == "n":
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

    if line[-1] in dictionary:
        dictionary[line[-1]] = dictionary.get(line[-1]) + [line]
    else:
        dictionary[line[-1]] = [line]

for key in dictionary:
    print("{} - liczba obiektów w klasach: {}".format(key, len(dictionary[key])))

def unique(attribute, list):
    uniqueList = []
    for i in list:
        if i not in uniqueList:
            uniqueList.append(i)

    print("Liczba unikalnych wartości atrubutu {}: {}".format(attribute, len(uniqueList)))
    print("Lista unikalnych wartości atrybutu {}".format(attribute))
    # for element in uniqueList:
    print(uniqueList)
    
for index in indexes:
    listAttributes = []
    listAttributesByKey = {}

    for key in dictionary:
        listPom = []
        for value in dictionary[key]:
            listAttributes.append(value[index])
            listPom.append(value[index])
        listAttributesByKey[key] = listPom
        print("{} Max atrybutu - {}, Min atrybutu - {}".format("a{}".format(str(index + 1)), max(listAttributes),
                                          min(listAttributes)))
        unique("a{}".format(index + 1), listAttributes)
        print("Odchylenie standardowe atrybutu {}, wynosi: {}".format(index + 1, statistics.stdev(listAttributes)))
        for key in listAttributesByKey:
            print("Odchylenie standardowe atrybutu {} w klasie decyzyjnej {}, wynosi: {}".format(index + 1, key,                                                                                             statistics.stdev(
                                                                                                   listAttributesByKey[                                                                                                       key])))


