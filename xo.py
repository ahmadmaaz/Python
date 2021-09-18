import time
import random
letter='O'
inbox= [' ',' ',' ',' ',' ',' ',' ',' ',' ']



def botdecide(nmb):
    
    inbox[nmb]='O'
    boardinit()


def boardinit():
    print("         "+inbox[0]+"|"+inbox[1]+'|'+inbox[2])
    print("         "+"_____")
    print("         "+inbox[3]+"|"+inbox[4]+'|'+inbox[5])
    print("         "+"_____")
    print("         "+inbox[6]+"|"+inbox[7]+'|'+inbox[8])
    print("---------Ahmad----------")
    print("---------Maaaz----------")

def checkwinner(whichsign, whichwinner):
    if (inbox[0]==whichsign and inbox[1]== whichsign and inbox[2]== whichsign) or (inbox[3]==whichsign and inbox[4]== whichsign and inbox[5]== whichsign)or (inbox[6]==whichsign and inbox[7]== whichsign and inbox[8]== whichsign) or (inbox[0]==whichsign and inbox[4]== whichsign and inbox[8]==whichsign) or (inbox[2]==whichsign and inbox[4]== whichsign and inbox[6]== whichsign) or (inbox[0]==whichsign and inbox[3]== whichsign and inbox[6]== whichsign) or (inbox[1]==whichsign and inbox[4]== whichsign and inbox[7]== whichsign) or (inbox[2]==whichsign and inbox[5]== whichsign and inbox[8]== whichsign):
        print( " The winner is "+ whichwinner)
        time.sleep(4)
        exit()
        
    if (inbox[0]!=' ' and inbox[1]!=' ' and inbox[2]!=' ' and inbox[3]!=' ' and inbox[4]!=' ' and inbox[5]!=' ' and inbox[6]!=' ' and inbox[7]!=' ' and inbox[8]!=' ' ):
        print(' DRAW!')
        time.sleep(4)
        exit()
        
        
        


botor2players= input('You want to play with bot or 2 players?Answer with B for bot and P for 2 players!')
while botor2players.lower()!='b' and botor2players.lower()!='p':
    botor2players= input('You want to play with bot or 2 players?Answer with B for bot and P for 2 players!')
if botor2players.lower()=='b':
    print('Your game files are loading please wait.....')
    time.sleep(2)
    boardinit()

    while True:
        time.sleep(1)
        p1turn=input('please select an empty slot from 1-9!')
        while (int(p1turn)<0 or int(p1turn)>10)  or inbox[int(p1turn)-1]!= ' ' or int(p1turn)==0 :
            p1turn=input('please select an empty slot from 1-9!')
        if inbox[int(p1turn)-1]==' ':
            inbox[int(p1turn)-1]= 'X'
            boardinit()
        checkwinner('X','You')
        checkwinner('O','Bot')
        time.sleep(1)
        
        
        
        if inbox[1]==letter and inbox[2]==letter and inbox[0]==' ': botdecide(0)
        elif inbox[0]==letter and inbox[1]==letter and inbox[2]==' ':botdecide(2)
        elif inbox[0]==letter and inbox[2]==letter and inbox[1]==' ': botdecide(1)
        elif inbox[3]==letter and inbox[4]==letter and inbox[5]==' ': botdecide(5)
        elif inbox[3]==letter and inbox[5]==letter and inbox[4]==' ':botdecide(4)
        elif inbox[4]==letter and inbox[5]==letter and inbox[3]==' ':botdecide(3)
        elif inbox[6]==letter and inbox[7]==letter and inbox[8]==' ':botdecide(8)
        elif inbox[6]==letter and inbox[8]==letter and inbox[7]==' ':botdecide(7)
        elif inbox[7]==letter and inbox[8]==letter and inbox[6]==' ':botdecide(6)
        elif inbox[0]==letter and inbox[3]==letter and inbox[6]==' ':botdecide(6)
        elif inbox[0]==letter and inbox[6]==letter and inbox[3]==' ':botdecide(3)
        elif inbox[3]==letter and inbox[6]==letter and inbox[0]==' ':botdecide(0)
        elif inbox[1]==letter and inbox[4]==letter and inbox[7]==' ':botdecide(7)
        elif inbox[1]==letter and inbox[7]==letter and inbox[4]==' ':botdecide(4)
        elif inbox[4]==letter and inbox[7]==letter  and inbox[1]==' ':botdecide(1)
        elif inbox[2]==letter and inbox[5]==letter and inbox[8]==' ':botdecide(8)
        elif inbox[2]==letter and inbox[8]==letter and inbox[5]==' ':botdecide(5)
        elif inbox[5]==letter and inbox[8]==letter and inbox[2]==' ':botdecide(2)
        elif inbox[0]==letter and inbox[4]==letter  and inbox[8]==' ':botdecide(8)
        elif inbox[0]==letter and inbox[8]==letter and inbox[4]==' ':botdecide(4)
        elif inbox[4]==letter and inbox[8]==letter and inbox[0]==' ':botdecide(0)
        elif inbox[2]==letter and inbox[4]==letter and inbox[6]==' ':botdecide(6)
        elif inbox[2]==letter and inbox[6]==letter and inbox[4]==' ':botdecide(4)
        elif inbox[4]==letter and inbox[6]==letter and inbox[2]==' ':botdecide(2)
        elif inbox[1]=='X'and inbox[2]=='X' and inbox[0]==' ': botdecide(0)
        elif inbox[0]=='X'and inbox[1]=='X' and inbox[2]==' ':botdecide(2)
        elif inbox[0]=='X'and inbox[2]=='X' and inbox[1]==' ': botdecide(1)
        elif inbox[3]=='X'and inbox[4]=='X' and inbox[5]==' ': botdecide(5)
        elif inbox[3]=='X'and inbox[5]=='X' and inbox[4]==' ':botdecide(4)
        elif inbox[4]=='X'and inbox[5]=='X' and inbox[3]==' ':botdecide(3)
        elif inbox[6]=='X'and inbox[7]=='X' and inbox[8]==' ':botdecide(8)
        elif inbox[6]=='X'and inbox[8]=='X' and inbox[7]==' ':botdecide(7)
        elif inbox[7]=='X'and inbox[8]=='X'and inbox[6]==' ':botdecide(6)
        elif inbox[0]=='X'and inbox[3]=='X' and inbox[6]==' ':botdecide(6)
        elif inbox[0]=='X'and inbox[6]=='X'and inbox[3]==' ':botdecide(3)
        elif inbox[3]=='X'and inbox[6]=='X'and inbox[0]==' ':botdecide(0)
        elif inbox[1]=='X'and inbox[4]=='X'and inbox[7]==' ':botdecide(7)
        elif inbox[1]=='X'and inbox[7]=='X'and inbox[4]==' ':botdecide(4)
        elif inbox[4]=='X'and inbox[7]=='X' and inbox[1]==' ':botdecide(1)
        elif inbox[2]=='X'and inbox[5]=='X'and inbox[8]==' ':botdecide(8)
        elif inbox[2]=='X'and inbox[8]=='X'and inbox[5]==' ':botdecide(5)
        elif inbox[5]=='X'and inbox[8]=='X'and inbox[2]==' ':botdecide(2)
        elif inbox[0]=='X'and inbox[4]=='X' and inbox[8]==' ':botdecide(8)
        elif inbox[0]=='X'and inbox[8]=='X' and inbox[4]==' ':botdecide(4)
        elif inbox[4]=='X'and inbox[8]=='X' and inbox[0]==' ':botdecide(0)
        elif inbox[2]=='X'and inbox[4]=='X' and inbox[6]==' ':botdecide(6)
        elif inbox[2]=='X'and inbox[6]=='X' and inbox[4]==' ':botdecide(4)
        elif inbox[4]=='X'and inbox[6]=='X' and inbox[2]==' ':botdecide(2)
        else:
            try:
                    ok=random.randint(0,8)
                    while inbox[ok]=='X' or inbox[ok]=='O':
                        ok=random.randint(0,8)
                    inbox[ok]='O'
                    boardinit()
            except:
                    inbox[5]='O'
        
        
        
        
        
        checkwinner('X','You')
        checkwinner('O','Bot')

if botor2players.lower()=='p':
    print('Your game files are loading please wait.....')
    time.sleep(2)
    boardinit()


    while True:
        time.sleep(1)
        p1turn=input('player 1  please select an empty slot from 1-9!')
        while (p1turn != '1' and p1turn != '2' and p1turn != '3' and p1turn != '4' and p1turn != '5' and p1turn != '6' and p1turn != '7' and p1turn != '8' and p1turn != '9') or inbox[int(p1turn)-1]!= ' ':
            p1turn=input('player 1  please select an empty slot from 1-9!')
        if inbox[int(p1turn)-1]==' ':
            inbox[int(p1turn)-1]= 'X'
            boardinit()
        checkwinner('X','Player 1')
        checkwinner('O','Player 2')
        time.sleep(1)
        p2turn=input('player 2  please select an empty slot from 1-9!')
        while (p2turn != '1' and p2turn != '2' and p2turn != '3' and p2turn != '4' and p2turn != '5' and p2turn !='6' and p2turn != '7' and p2turn != '8' and p2turn != '9') or inbox[int(p2turn)-1]!= ' ' :
            p2turn=input('player 2  please select an empty slot from 1-9!')
        

        if inbox[int(p2turn)-1]==' ':
            inbox[int(p2turn)-1]= 'O'
            boardinit()
        checkwinner('X','Player 1')
        checkwinner('O','Player 2')
        
        
        
    





