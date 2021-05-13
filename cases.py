
import itertools


"""
NUM_BALL = 3
NUM_BOTTLES = 3
start = [[1, 2, 0], [1, 1, 0], [2, 2, 0]]

#listA = [[1, 1, 1], [0, 0, 0]]
#listB = [[1, 1, 0], [1, 0, 0]]

###
allLista = [
            [[2, 2, 2], [1, 1, 1], [0, 0, 0]],
            [[2, 2, 0], [1, 1, 1], [2, 0, 0]],
            [[2, 2, 2], [1, 1, 0], [1, 0, 0]],
            [[2, 2, 0], [1, 1, 0], [2, 1, 0]],
            [[2, 0, 0], [1, 1, 0], [2, 2, 1]],
            [[2, 2, 0], [1, 0, 0], [1, 1, 2]],
            [[2, 2, 0], [1, 0, 2], [1, 1, 0]]
            ]


test = set()

for i in itertools.combinations(list(itertools.combinations([2, 2, 2, 1, 1, 1, 0, 0, 0], 3)), 3):
    test.add(i)

print(test)

toRemove = []
for subList in test:
    count2 = 0
    count1 = 0
    count0 = 0
    for i in subList:
        for elem in i:
            if elem == 2:
                count2 += 1
            if elem == 1:
                count1 += 1
            if elem == 0:
                count0 += 1

    if count2 == 3 and count1 == 3 and count0 == 3:
        pass
    else:
        toRemove.append(subList)

for i in toRemove:
    test.remove(i)


setElem = {}
stateIdx = 0
allLista = []
for elem in list(test):
    subListaB = []
    for subElem in elem:
        subListaB.append(list(subElem))
    allLista.append(subListaB)

#print(allLista)

for lista in allLista:
    for idx, values in enumerate(lista):
        for x in itertools.permutations(values):
            newElem = lista.copy()
            newElem[idx] = x

            tup = tuple(tuple(sub) for sub in newElem)
            setElem[tup] = stateIdx
            stateIdx += 1
print(setElem)


setElem = {}
def testFun(allLista):
    stateIdx = 0
    for lista in allLista:
        copy = lista.copy()

        lista = copy
        ways = [i for i in range(len(lista))]
        for i in itertools.permutations(ways):
            # Permutações entre as N Listas
            lista = []
            for copyIdx in i:
                lista.append(copy[copyIdx].copy())

            # Permutações entre as N Listas
            for idx, values in enumerate(lista):
                print(list(itertools.permutations(values)))
                for x in itertools.permutations(values):
                    newElem = lista.copy()
                    newElem[idx] = x

                    tup = tuple(tuple(sub) for sub in newElem)
                    setElem[tup] = 1
                    stateIdx += 1

testFun(allLista)
print(len(setElem))
"""
