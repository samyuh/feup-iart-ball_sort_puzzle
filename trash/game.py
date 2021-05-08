NUM_BOTTLES = 3
MAX_BALLS = 4

bottle_list = [["blue","blue"], [ "yellow","yellow"]]
move_list = []

def ansiEncodeGame():
    for idx, i in enumerate(bottle_list):
        print("Bottle" + str(idx))
        start = MAX_BALLS - len(i)
        for value in range(MAX_BALLS):
            if value >= start:
                print("|" + i[value-start] + "|")
            else:
                print("|    |")
        print("\n")

def isGoal():
    for i in bottle_list:
        if len(i) == 0:
            continue
        if not (all(element == i[0] for element in i) and (len(i) == 4)):
            return False
    return True

def isNotFull(bottle):
    if len(bottle) < MAX_BALLS:
        return True
    return False

def moves():
    for idxA, a in enumerate(bottle_list): # Pick from this bottle
        for idxB, b in enumerate(bottle_list): # To this bottle
            if not a:
                continue
            elif not b:
                move_list.append([a[0], idxA, idxB])
            elif (a[0] == b[0]) and isNotFull(b) and a != b:
                move_list.append([a[0], idxA, idxB])

def play():
    print("Game")
    ansiEncodeGame()
    moves()
    print(move_list)
    print(isGoal())
    pass

if __name__ == "__main__":
    play()