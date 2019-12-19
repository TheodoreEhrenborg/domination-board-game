# uses user defined ordering at the first level only, direct descendant of
# 6 and shares some features with 8


def Computer9(c, depth=2, time_limit=60, ordering=0):
    from time import time
    end_time = time() + time_limit
    best_list = []
    for a_depth in range(1, depth + 1):
        alpha = -1000
        beta = 1000
        bestscore = -1000
        moves = c.clean(c.moves[c.side])
        # A placeholder for the case when every move loses at once.
        bestmove = moves[0]
# print(moves)
        if ordering > 0:
            moves.sort(key=lambda move_in_list: -
                       rank9(c.copy().move(move_in_list, True), ordering -
                             1, -
                             beta, -
                             alpha, end_time), reverse=True)
        for possmove in moves:
            temp = c.copy()
            temp.move(possmove)
# print(possmove,alpha,beta,end_time,a_depth)
            r = -rank9(temp, a_depth - 1, -beta, -alpha, end_time)
# print(r)
# r=-r
            if time() > end_time:
                break
            if r > bestscore:  # If this were >=, the computer might make a move that it has not fully explored, especially if all moves are similar.
                bestscore = r
                bestmove = possmove
            if bestscore > alpha:
                alpha = bestscore
            if alpha >= beta:
                best_list = [bestmove, alpha, a_depth]
                break
##            print [possmove,r]
        if time() < end_time:
            best_list = [bestmove, bestscore, a_depth]
        else:
            break
    return best_list


def rank9(board, depth, alpha=-1000, beta=1000, end_time=2000000000):
    from time import time
    if depth == 0 or board.score2(board.side) in (-1000, 1000):
        return board.score2(board.side)
    bestscore = -1000
# v=0
##    import domination_board
# z=domination_board.Board()
# z.move("b2b3")
    moves_to_do = board.clean(board.moves[board.side])
# testing=False
# if z.moves==board.moves:
# print(moves_to_do)
# testing=True
    for possmove in moves_to_do:
        temp = board.copy()
# if testing:
# print(possmove) #Oh no. It only printed the first 3 from a list of about
# 20! It's not looking at all possible re-plies!
        temp.move(possmove)
# if possmove=="g7f7":
        r = -rank9(temp, depth - 1, -beta, -alpha, end_time)
# if testing:
##            print(possmove, r, bestscore, alpha, beta)
# if possmove=="g7f7" and z.moves==board.moves:
# print("r:",r,depth,beta,alpha)
# v=2
# else:
# v=v-1
# if v==1:
# print(possmove)
        if time() > end_time:
            # if testing:
            ##                print("Look here")
            return 3
        if r > bestscore:
            bestscore = r
        if bestscore > alpha:
            alpha = bestscore
        if alpha >= beta:
            # if testing:
            ##                print("Over here")
            return alpha
    return bestscore


# Only uses searches of even depth, although that idea was a mistake
def Computer10(c, depth=2, time_limit=60, ordering=0):
    from time import time
    end_time = time() + time_limit
    best_list = []
    for a_depth in [1] + range(2, depth + 1, 2):
        alpha = -1000
        beta = 1000
        bestscore = -1000
        moves = c.clean(c.moves[c.side])
        # A placeholder for the case when every move loses at once.
        bestmove = moves[0]
        num_moves = len(moves)
# print(moves)
        if ordering > 0:
            moves.sort(key=lambda move_in_list: -
                       rank9(c.copy().move(move_in_list, True), ordering -
                             1, -
                             beta, -
                             alpha, end_time), reverse=True)
        moves_done_so_far = 0
        stopped = False
        start_time = time()
        for possmove in moves:
            temp = c.copy()
            temp.move(possmove)
# print(possmove,alpha,beta,end_time,a_depth)
            r = -rank9(temp, a_depth - 1, -beta, -alpha, end_time)
# print(r)
# r=-r
            if time() > end_time:
                stopped = True
                break
            if r > bestscore:  # If this were >=, the computer might make a move that it has not fully explored, especially if all moves are similar.
                bestscore = r
                bestmove = possmove
            if bestscore > alpha:
                alpha = bestscore
            if alpha >= beta:
                best_list = [bestmove, alpha, a_depth]
                break
            moves_done_so_far += 1
# if (end_time-time())*1.5<(num_moves-moves_done_so_far)*(time()-start_time)/moves_done_so_far: #This line tried to estimate how long the program would take, but it overestimated the necessary time. Remember, alpha-beta pruning makes later thinking faster.
# stopped=True
# print(best_list)
# break
##            print [possmove,r]
        if time() < end_time and not(stopped):
            best_list = [bestmove, bestscore, a_depth]
        else:
            break
    return best_list


# Descendent of 9, will not consider playing a reserve piece anywhere but
# on an opponent's tower
def Computer11(c, depth=2, time_limit=60, ordering=0):
    from time import time
    end_time = time() + time_limit
    best_list = []
    for a_depth in range(1, depth + 1):
        alpha = -1000
        beta = 1000
        bestscore = -1000
        c.find_good_moves_for_the_side_to_play()
        moves = c.good_moves
        # A placeholder for the case when every move loses at once.
        bestmove = moves[0]
# print(moves)
        if ordering > 0:
            moves.sort(key=lambda move_in_list: -
                       rank11(c.copy().move(move_in_list, True), ordering -
                              1, -
                              beta, -
                              alpha, end_time), reverse=True)
        for possmove in moves:
            temp = c.copy()
            temp.move(possmove)
# print(possmove,alpha,beta,end_time,a_depth)
            r = -rank11(temp, a_depth - 1, -beta, -alpha, end_time)
# print(r)
# r=-r
            if time() > end_time:
                break
            if r > bestscore:  # If this were >=, the computer might make a move that it has not fully explored, especially if all moves are similar.
                bestscore = r
                bestmove = possmove
            if bestscore > alpha:
                alpha = bestscore
            if alpha >= beta:
                best_list = [bestmove, alpha, a_depth]
                break
##            print [possmove,r]
        if time() < end_time:
            best_list = [bestmove, bestscore, a_depth]
        else:
            break
    return best_list


def rank11(board, depth, alpha=-1000, beta=1000, end_time=2000000000):
    from time import time
    if depth == 0 or board.score2(board.side) in (-1000, 1000):
        return board.score2(board.side)
    bestscore = -1000
# v=0
##    import domination_board
# z=domination_board.Board()
# z.move("b2b3")
    board.find_good_moves_for_the_side_to_play()
    moves_to_do = board.good_moves
# testing=False
# if z.moves==board.moves:
# print(moves_to_do)
# testing=True
    for possmove in moves_to_do:
        temp = board.copy()
# if testing:
# print(possmove) #Oh no. It only printed the first 3 from a list of about
# 20! It's not looking at all possible re-plies!
        temp.move(possmove)
# if possmove=="g7f7":
        r = -rank11(temp, depth - 1, -beta, -alpha, end_time)
# if testing:
##            print(possmove, r, bestscore, alpha, beta)
# if possmove=="g7f7" and z.moves==board.moves:
# print("r:",r,depth,beta,alpha)
# v=2
# else:
# v=v-1
# if v==1:
# print(possmove)
        if time() > end_time:
            # if testing:
            ##                print("Look here")
            return 3
        if r > bestscore:
            bestscore = r
        if bestscore > alpha:
            alpha = bestscore
        if alpha >= beta:
            # if testing:
            ##                print("Over here")
            return alpha
    return bestscore


class Computer12:  # Descendent of 11, hashtable (just kidding), an object
    def __init__(self, scoring=3):
        self.scoring = scoring

    def go(self, c, depth=2, time_limit=60, ordering=0):
        self.c = c
        self.depth = depth
        self.time_limit = time_limit
        self.ordering = ordering
        from time import time
        end_time = time() + time_limit
        best_list = []
        for a_depth in range(1, depth + 1):
            alpha = 0
            beta = 1
            bestscore = 0
            c.find_good_moves_for_the_side_to_play()
            moves = c.good_moves
            # A placeholder for the case when every move loses at once.
            bestmove = moves[0]
            if ordering > 0:
                moves.sort(key=lambda move_in_list: 1 -
                           self.rank(c.copy().move(move_in_list, True), ordering -
                                     1, 1 -
                                     beta, 1 -
                                     alpha, end_time), reverse=True)
            for possmove in moves:
                temp = c.copy()
                temp.move(possmove)
                r = 1 - self.rank(temp, a_depth - 1, 1 -
                                  beta, 1 - alpha, end_time)
                if time() > end_time:
                    break
                if r > bestscore:  # If this were >=, the computer might make a move that it has not fully explored, especially if all moves are similar.
                    bestscore = r
                    bestmove = possmove
                if bestscore > alpha:
                    alpha = bestscore
                if alpha >= beta:
                    best_list = [bestmove, alpha, a_depth]
                    break
            if time() < end_time:
                best_list = [bestmove, bestscore, a_depth]
            else:
                break
        return best_list

    def rank(self, board, depth, alpha=0,
             beta=1, end_time=2000000000):
        from time import time
        if board.score3(board.side) in (0, 1):
            return board.score3(board.side)
        if depth == 0:
            return board.score(board.side, self.scoring)
        bestscore = 0
        board.find_good_moves_for_the_side_to_play()
        moves_to_do = board.good_moves
        for possmove in moves_to_do:
            temp = board.copy()
            temp.move(possmove)
            r = 1 - self.rank(temp, depth - 1, 1 - beta, 1 - alpha, end_time)
            if time() > end_time:
                return 3
            if r > bestscore:
                bestscore = r
            if bestscore > alpha:
                alpha = bestscore
            if alpha >= beta:
                return alpha
        return bestscore
