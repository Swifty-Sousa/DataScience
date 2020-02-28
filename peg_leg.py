import numpy as np
winnings_list= []
#list of 10000 trials winnings/losings
# negative values denote losing money
my_turn= 0
peg_leg_turn=0
#these two dennote weather on a roll i had to give money or not 
my_prev= 99
peg_leg_prev= 99
# they start at 99 so the frist roll cannot match any previous for those coditions
D20= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
D19= D20= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]


def start_my_turn():
    global my_turn
    global peg_leg_prev
    roll= np.random.choice(D20, size=1)
    if(roll== peg_leg_prev):
        turn= -5
    elif(roll==8):
        turn=2
    elif(roll==7):
        turn=4
    elif(roll==15):
        turn=-1



def start_peg_leg_turn():
    global peg_leg_turn
    global my_prev

def win_solver():

def mains():
