import random

def setUp(lists,reps):
    for i in range(reps):
        lists.append(random.randint(1,13))
    print(lists)

def moveable(hand,mid):
    for i in range(5):
        for j in range(2):
            if hand[i] == mid[j]+1 or hand[i] == mid[j]-1:
                return True
    return False

def move(j,inp, playahHand):
    mid[j] = inp
    playahHand.remove(inp)
    playahHand.append(random.randint(1,13))
    print[mid]



compHand = []
playahHand = []
mid = []
setUp(compHand,5)
setUp(playahHand,5)
setUp(mid,2)

gameOn = True
while(gameOn):
    #change the mid
    if moveable(compHand,mid) == False and moveable(compHand,mid) == False :
        mid[0] = random.randint(1,13)
        mid[1] = random.randint(1,13)
        print("yodelayeehu")

    #Computer Move
    if(moveable(compHand,mid)):
        for i in range(5):#runs through the hand
            for j in range(2):#runs through mid
                if compHand[i] == mid[j]+1 or compHand[i] == mid[j]-1:#checks if the current card in the hand can be played in the current position of mid
                    move(j,compHand[i],compHand)

    #Player Move
    while(moveable(playahHand,mid)):
        print("Your Hand:")
        print(playahHand)
        print("The Middle Section:")
        print(mid)

        print("What card do you want to play?")
        ining = int(input(">"))
        print("Left pile(input 1) or right pile(input 2)")
        to = int(input(">"))
        to-=1

        if mid[to] == 13:
            if ining == 12 or ining == 1:
                move(to,ining,playahHand)
        elif mid[to] == 1:
            if ining == 2 or ining == 13:
                move(to,ining,playahHand)
        elif mid[to]+1 == ining or mid[to]-1 == ining:
            move(to,ining,playahHand)
        else:
            print("invalid move :(")
