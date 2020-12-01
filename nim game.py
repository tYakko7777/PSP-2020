import random,math

def playNovice(b):
    take = random.randint(1,int(b/2))
    return take
def playExpert(b):
    m = int(math.log(b,2))
    if b == 2**(m+1)-1:
        take = playNovice(b)
    else:
        take = b-(2**m-1)
    return take

def playmodel(a,b):
    if a == 1:
        t = playNovice(b)
    elif a == 2:
        t = playExpert(b)
    return t

def gamerun():
    k = int(input("please decide the computer's level,1 is easy,2 is hard"))
    sum = 100
    playerturn = False
    comturn = False
    m = int(input('please decide who to begin,1 for computer,2 for you'))
    if m == 2 :
        playerturn = True
    elif m == 1:
        comturn = True
    while sum != 1 and (playerturn or comturn) :
        print('there reamian',sum)
        if playerturn == True:
            x = int(input('please decide how many you will take.'))
            while not(0<x<=int(sum/2)):
                print("you should never take more than",int(sum/2))
                x = int(input("Be honest!Don't cheat"))
            sum = sum - x
        elif comturn == True:
            y = playmodel(k,sum)
            sum = sum - y
            print('the computer take off',y)
        playerturn,comturn = comturn,playerturn
    else:
        print('there remian 1')
    return playerturn,comturn
def winner(a,b):
    if a:
        print('this is your turn.winner is computer')
    elif b:
        print("this is computer's turn.winner is you")
        
x,y = gamerun()
winner(x,y)
