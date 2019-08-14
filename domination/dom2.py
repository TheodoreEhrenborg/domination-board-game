#Begin file
#Dom2
from Dom_board import Board
from Dom_computer import Computer1
b=Board()
player=3
while player!="g" and player!="r":
    player=raw_input("Do you want to be r or g? R moves first.")
while len(b.moves[b.side])>0:
    print
    b.display()
    print
    if player==b.side:
        move=raw_input(b.side+"’s move:")    
        while move not in b.moves[b.side]:
            move=raw_input("Try Again:")
    else:
        l=Computer1(b)
        move=l[0]
        print b.side+"’s move:"+move
        print "Projected Score:"+str(l[1])
    b.move(move)
    print "Current Computer Score:"+str(b.score(b.opponent(player)))
print
b.display()
print
print b.opponent(b.side)+" has won!"

