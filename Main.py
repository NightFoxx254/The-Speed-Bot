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

    #Computer Move
    if(moveable(compHand,mid)):
        for i in range(5):#runs through the hand
            for j in range(2):#runs through mid
                if compHand[i] == mid[j]+1 or compHand[i] == mid[j]-1:#checks if the current card in the hand can be played in the current position of mid
                    print(mid[j])
                    mid[j] = compHand[i]#places the card down
                    print(mid[j])
                    compHand.pop(i)#removes the placed card from the hand
                    compHand.append(random.randint(1,13))#dhraws a new card into the hand
                    print("beep")

    streak = True
    while(streak):
        if moveable(playahHand,mid) == False:
            streak = False
            break
        else:
            print(mid[0],mid[1])
            print(playahHand[0],playahHand[1],playahHand[2],playahHand[3],playahHand[4])
            print("What card do you want to play?")
            inp = int(input(">"))
            if inp in playahHand:
                if mid[0] == 13:
                    if inp == 1 or inp == 12:
                        move(0,inp,playahHand)
                elif mid[1] == 13:
                    if inp == 1 or inp == 12:
                        move(1,inp,playahHand)
                if mid[0] == 1:
                    if inp == 2 or inp == 13:
                        move(0,inp,playahHand)
                elif mid[1] == 1:
                    if inp == 2 or inp == 13:
                        move(1,inp,playahHand)
                elif mid[0]+1 == inp or mid[0]-1 == inp:
                    move(0,inp,playahHand)
                elif mid[1]+1 == inp or mid[1]-1 == inp:
                    move(1,inp,playahHand)
                else:
                    print("sorry that is an invalid move")

