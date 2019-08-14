#Begin file
#Dom1
from Dom_board import Board
b=Board()
b.display()
while len(b.moves[b.side])>0:
    move=raw_input(b.side+"’s move:")    
    while move not in b.moves[b.side]:
        move=raw_input("Try Again:")
    b.move(move)
    print
    b.display()
    print
print b.opponent()+" has won!"

