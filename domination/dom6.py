#Begin file
#Dom6
from Dom_board import Board
from time import time
from Dom_computer import Computer6
b=Board()
player=3
depth=0
maxtime=0
while depth<1 or int(depth)!=depth:
    depth=input("Maximum Depth:")
print
while maxtime<1:
    maxtime=input("Maximum Time:")
print
while player!="g" and player!="r":
    player=raw_input("Do you want to be r or g? R moves first.")
while len(b.moves[b.side])>0:
    print
    b.display()
    print
    start_time=time()
    if player==b.side:
        move=raw_input(b.side+"’s move:")    
        while move not in b.moves[b.side]:
            move=raw_input("Try Again:")
    else:
        l=Computer6(b,depth,maxtime)
        move=l[0]
        print b.side+"’s move:"+move
        print "Projected Score:",l[1]
        print "Depth of Search :",l[2]
    b.move(move)
    print "Current Computer Score:",b.score2(b.opponent(player))
    print "This move took", time()-start_time, "seconds"
print
b.display()
print
print b.opponent(b.side)+" has won!"

