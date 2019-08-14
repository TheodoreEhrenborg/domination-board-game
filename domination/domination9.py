from domination_board import Board
from time import time
from domination_computer import Computer9
b=Board()
player=3
ordering=-1
depth=0
maxtime=0
import os
while depth<1 or int(depth)!=depth:
    depth=input("Maximum Depth:")
print
while maxtime<1:
    maxtime=input("Maximum Time:")
print
while ordering<0 or int(ordering)!=ordering or ordering>= depth:
    ordering=input("Ordering (can be zero):")
print
while player!="g" and player!="r":
    player=raw_input("Do you want to be r or g? R moves first.")
while len(b.moves[b.side])>0:
    print
    b.display()
    print
    start_time=time()
    if player==b.side:
        move=raw_input(b.side+"'s move:")    
        while move not in b.moves[b.side]:
            move=raw_input("Try Again:")
    else:
        l=Computer9(b,depth,maxtime,ordering)
        move=l[0]
        print b.side+"'s move:"+move
        print "Projected Score:",l[1]
        print "Depth of Search :",l[2]
        os.system("say 'Your move.'")
    b.move(move)
    print "Current Computer Score:",b.score2(b.opponent(player))
    print "This move took", time()-start_time, "seconds"
print
b.display()
print
print b.opponent(b.side)+" has won!"
