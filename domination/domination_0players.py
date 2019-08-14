#Make all the ComputerX functions into objects, then adjust this accordingly.
import os
from domination_board import Board
from time import time
from domination_computer import Computer10, Computer9, Computer11
all_moves=[]
b=Board()
tie_list=['four', 'totally', 'different', 'words']
version=0
while version<9 or int(version)!=version:
    version=input("Version of r:")
if version==9:
    thinker_r=Computer9
if version==10:
    thinker_r=Computer10
if version==11:
    thinker_r=Computer11
##player_r=3
ordering_r=-1
depth_r=0
maxtime_r=0
while depth_r<1 or int(depth_r)!=depth_r:
    depth_r=input("Maximum Depth of r:")
print
while maxtime_r<1:
    maxtime_r=input("Maximum Time of r:")
print
while ordering_r<0 or int(ordering_r)!=ordering_r or ordering_r>= depth_r:
    ordering_r=input("Ordering (can be zero) of r:")
print
version=0
while version<9 or int(version)!=version:
    version=input("Version of g:")
if version==9:
    thinker_g=Computer9
if version==10:
    thinker_g=Computer10
if version==11:
    thinker_g=Computer11
##player_g=3
ordering_g=-1
depth_g=0
maxtime_g=0
while depth_g<1 or int(depth_g)!=depth_g:
    depth_g=input("Maximum Depth of g:")
print
while maxtime_g<1:
    maxtime_g=input("Maximum Time of g:")
print
while ordering_g<0 or int(ordering_g)!=ordering_g or ordering_g>= depth_g:
    ordering_g=input("Ordering (can be zero) of g:")
print
##while player!="g" and player!="r":
##    player=raw_input("Do you want to be r or g? R moves first.")
##player="r"
moves_so_far=0
is_tie=False
while len(b.moves[b.side])>0 and is_tie==False:
    print
    b.display()
    print
    start_time=time()
    if "r"==b.side:
        l=thinker_r(b,depth_r,maxtime_r,ordering_r)
        move=l[0]
        all_moves.append(move)
        moves_so_far+=1
        print "Move:",moves_so_far
        print b.side+"'s move:"+move
        print "Projected Score by r for r:",l[1]
        print "Depth of Search :",l[2]
    else:
        l=thinker_g(b,depth_g,maxtime_g,ordering_g)
        move=l[0]
        all_moves.append(move)
        moves_so_far+=1
        print "Move:",moves_so_far
        print b.side+"'s move:"+move
        print "Projected Score by g for r:",-l[1]
        print "Depth of Search :",l[2]
    b.move(move)
    print "Current Score of r:",b.score2("r")
    print "This move took", time()-start_time, "seconds"
    print 'All moves so far',all_moves
    tie_list[moves_so_far%4]=move
    if tie_list[0][:2]==tie_list[2][2:] and tie_list[2][:2]==tie_list[0][2:] and tie_list[1][:2]==tie_list[3][2:] and tie_list[3][:2]==tie_list[1][2:]:
        is_tie=True
print
b.display()
print
if is_tie:
    print "There has been a tie after",moves_so_far,"moves!"
else:
    print b.opponent(b.side)+" has won after",moves_so_far,"moves!"
os.system("say 'The game has finished.'")
print 'All moves so far',all_moves
