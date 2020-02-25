import os
from time import time
from domination_board import Board
from domination_computer import Computer12, Computer13, Computer14
all_moves = []
b = Board()
tie_list = ['four', 'totally', 'different', 'words']
version_r = -1
while (version_r < 12 and version_r != 0) or int(version_r) != version_r:
    version_r = int(input("Version of r (0 means human): "))
# if version_r == 11:
#    thinker_r = Computer11
# player_r=3
if version_r != 0:
    scoring = 0
    while scoring < 1 or int(scoring) != scoring:
        scoring = int(input("Scoring of r: "))
    if version_r == 12:
        thinker_r = Computer12(scoring)
    if version_r == 13:
        thinker_r = Computer13(scoring)
    if version_r == 14:
        thinker_r = Computer14(scoring)
    ordering_r = -1
    depth_r = -1
    maxtime_r = 0
    while maxtime_r < 1:
        maxtime_r = int(input("Maximum Time of r: "))
    print()
    if version_r == 12:
        while depth_r < 0 or int(depth_r) != depth_r:
            depth_r = int(input("Maximum Depth of r: "))
        print()
        while ordering_r < 0 or int(
                ordering_r) != ordering_r or (ordering_r >= depth_r and depth_r):
            ordering_r = int(input("Ordering (can be zero) of r: "))
        print()
    else:
        curiosity_r = float(input("Curiosity of r: "))
        print()
version_g = -1
while (version_g < 12 and version_g != 0) or int(version_g) != version_g:
    version_g = int(input("Version of g (0 means human): "))
if version_g != 0:
    scoring = 0
    while scoring < 1 or int(scoring) != scoring:
        scoring = int(input("Scoring of g: "))
    if version_g == 12:
        thinker_g = Computer12(scoring)
    if version_g == 13:
        thinker_g = Computer13(scoring)
    if version_g == 14:
        thinker_g = Computer14(scoring)
    ordering_g = -1
    depth_g = -1
    maxtime_g = 0
    while maxtime_g < 1:
        maxtime_g = int(input("Maximum Time of g: "))
        print()
    if version_g == 12:
        while depth_g < 0 or int(depth_g) != depth_g:
            depth_g = int(input("Maximum Depth of g: "))
        print()
        while ordering_g < 0 or int(
                ordering_g) != ordering_g or (ordering_g >= depth_g and depth_g):
            ordering_g = int(input("Ordering (can be zero) of g: "))
        print()
    else:
        curiosity_g = float(input("Curiosity of g: "))
        print()
# while player!="g" and player!="r":
# player=raw_input("Do you want to be r or g? R moves first.")
# player="r"
moves_so_far = 0
is_tie = False
while len(b.moves[b.side]) > 0 and is_tie == False:
    print()
    b.display()
    print()
    start_time = time()
    if "r" == b.side:
        if version_r == 0:
            move = input("r's move: ")
            while move not in b.moves['r']:
                move = input("Try Again: ")
        elif version_r == 12:
            l = thinker_r.go(b, depth_r, maxtime_r, ordering_r)
        else:
            l = thinker_r.go(b, maxtime_r, curiosity_r)
        if version_r != 0:
            move = l[0]
        all_moves.append(move)
        moves_so_far += 1
        print("Move:", moves_so_far)
        print(b.side + "'s move:" + move)
        if version_r != 0:
            print("Projected Score by r for r:", l[1])
            print("Depth of Search :", l[2])
    else:
        if version_g == 0:
            move = input("g's move: ")
            while move not in b.moves['g']:
                move = input("Try Again: ")
        elif version_g == 12:
            l = thinker_g.go(b, depth_g, maxtime_g, ordering_g)
        else:
            l = thinker_g.go(b, maxtime_g, curiosity_g)
        if version_g != 0:
            move = l[0]
        all_moves.append(move)
        moves_so_far += 1
        print("Move:", moves_so_far)
        print(b.side + "'s move:" + move)
        if version_g != 0:
            print("Projected Score by g for r:", 1 - l[1])
            print("Depth of Search :", l[2])
    b.move(move)
    print("Current score3 (classic) of r:", b.score3("r"))
    print("Current score6 (5-towers) of r:", b.score6("r"))
    print("Current score8 (2x reserves) of r:", b.score8("r"))
    print("Current score6 (half reserves) of r:", b.score9("r"))
    print("This move took", time() - start_time, "seconds")
    print('All moves so far', all_moves)
    tie_list[moves_so_far % 4] = move
    if tie_list[0][:2] == tie_list[2][2:] and tie_list[2][:2] == tie_list[0][2:
                                                                             ] and tie_list[1][:2] == tie_list[3][2:] and tie_list[3][:2] == tie_list[1][2:]:
        is_tie = True
print()
b.display()
print()
if is_tie:
    print("There has been a tie after", moves_so_far, "moves!")
else:
    print(b.opponent(b.side) + " has won after", moves_so_far, "moves!")
# os.system("say 'The game has finished.'")
print('All moves so far', all_moves)
