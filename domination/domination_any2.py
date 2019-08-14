from domination_board import Board
from time import time
from domination_computer import Computer10, Computer9, Computer11
import os
b=Board()
player=3
ordering=-1
depth=0
maxtime=0
version=0
while version<9 or int(version)!=version:
    version=input("Version:")
if version==9:
    Computer=Computer9
if version==10:
    Computer=Computer10
if version==11:
    Computer=Computer11
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
print
b.display()
while len(b.moves[b.side])>0:
    print
    start_time=time()
    if player==b.side:
        move=raw_input(b.side+"'s move:")
        os.system('''cd '/Users/jtae/Desktop/Don'"'"'t empty the trash. Check first/' && '/usr/bin/python'  '/Users/jtae/Desktop/Don'"'"'t empty the trash. Check first/CGR.py'  && echo Exit status: $? && exit 1''')
    
        while move not in b.moves[b.side]:
            move=raw_input("Try Again:")
        b.move(move)
        print
        b.display()
    else:
        l=Computer(b,depth,maxtime,ordering)
        move=l[0]
        temp_side=b.side
        b.move(move)
        print
        b.display()
        print temp_side+"'s move:"+move
        print "Projected Score:",l[1]
        print "Depth of Search :",l[2]
        os.system('say "Your move."')
##        for m in b.moves[b.side]:
##            t=b.copy()
##            t.move(m)
##            print(m,t.score2("r"))
##    b.move(move)
##    print
    print "Current Computer Score:",b.score2(b.opponent(player))
    print "This move took", time()-start_time, "seconds"
##    print
##    b.display()
##print
##b.display()
print
print b.opponent(b.side)+" has won!"
