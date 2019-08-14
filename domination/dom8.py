#Begin file
#Dom8
from Dom_board import Board
from time import time
from Dom_computer import Computer8
b=Board()
player=3
depth=0
maxtime=0
ordering=-1
while depth<1 or int(depth)!=depth:
    depth=input("Maximum Depth:")
print
while maxtime<1:
    maxtime=input("Maximum Time:")
print
while ordering<0 or int(ordering)!=ordering or ordering>= depth:
    ordering=input("Maximum Ordering (can be zero):")
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
        l=Computer8(b,depth,maxtime,ordering)
        move=l[0]
        print b.side+"’s move:"+move
        print "Projected Score:"+str(l[1])
    b.move(move)
    print "Current Computer Score:"+str(b.score2(b.opponent(player)))
    print "This move took", time()-start_time, "seconds"
print
b.display()
print
print b.opponent(b.side)+" has won!"

