def Computer9(c, depth=2, time_limit=60, ordering=0):
    '''uses user defined ordering at the first level only, direct
descendant of 6 and shares some features with 8'''
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
# print [possmove,r]
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
# import domination_board
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
# print(possmove, r, bestscore, alpha, beta)
# if possmove=="g7f7" and z.moves==board.moves:
# print("r:",r,depth,beta,alpha)
# v=2
# else:
# v=v-1
# if v==1:
# print(possmove)
        if time() > end_time:
            # if testing:
            # print("Look here")
            return 3
        if r > bestscore:
            bestscore = r
        if bestscore > alpha:
            alpha = bestscore
        if alpha >= beta:
            # if testing:
            # print("Over here")
            return alpha
    return bestscore


def Computer10(c, depth=2, time_limit=60, ordering=0):
    '''Only uses searches of even depth, although that idea was a mistake'''
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
# print [possmove,r]
        if time() < end_time and not(stopped):
            best_list = [bestmove, bestscore, a_depth]
        else:
            break
    return best_list


def Computer11(c, depth=2, time_limit=60, ordering=0):
    '''Descendent of 9, will not consider playing a reserve piece
 anywhere but on an opponent's tower'''
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
# print [possmove,r]
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
# import domination_board
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
# print(possmove, r, bestscore, alpha, beta)
# if possmove=="g7f7" and z.moves==board.moves:
# print("r:",r,depth,beta,alpha)
# v=2
# else:
# v=v-1
# if v==1:
# print(possmove)
        if time() > end_time:
            # if testing:
            # print("Look here")
            return 3
        if r > bestscore:
            bestscore = r
        if bestscore > alpha:
            alpha = bestscore
        if alpha >= beta:
            # if testing:
            # print("Over here")
            return alpha
    return bestscore


class Computer12:
    '''Descendent of 11, hashtable (just kidding), an object.
    Thus it does not play reserve pieces on empty squares'''

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
        if depth == 0:
            import random
            c.find_good_moves_for_the_side_to_play()
            return [random.choice(c.good_moves), .5, 0]
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


class Computer13:
    '''Uses MCTS to choose a move. Does not ban
    playing reserve pieces on empty squares'''

    def __init__(self, scoring=3):
        self.scoring = scoring

    def go(self, c, time_limit=60):
        t = Tree(c, time_limit, self.scoring)
        # Expect make_choice to return (bestmove, eval_average of that move,
        # eval_count of that move)
        return t.make_choice_visits()


class Tree:
    '''The tree of moves, which explands using MCTS'''

    def __init__(self, start_board, time_limit, scoring, curiosity=0):
        # Why are time_limit and self.scoring defined at different times?
        from time import time
        end_time = time() + time_limit
        self.scoring = scoring
        self.curiosity = curiosity
        start_board = start_board.copy()
        start_board.optimize = True
        self.ur_node = Node(start_board, None)
        self.ur_side = start_board.side
        while time() < end_time:
            #            print('a', time(), end_time)
            current_node = self.ur_node
            while not current_node.is_leaf():
                # Choose a child node using the magic formula
                #                print('b', time())
                best_child = current_node.children[0]
                for child in current_node.children:
                    if child.magic_formula(
                            self.ur_side, self.curiosity) > best_child.magic_formula(self.ur_side, self.curiosity):
                        best_child = child
                current_node = best_child
            # Now add children to the leaf node
            current_node.add_children()
            # Now run the static evaluator on the leaf,
            # and go up the tree updating the nodes
            static_score = current_node.board.score3(self.ur_side)
            if static_score not in (0, 1):
                static_score = current_node.board.score(
                    self.ur_side, self.scoring)
#            print('c', time())
            while current_node is not None:
                current_node.eval_count += 1
                current_node.eval_sum += static_score
                current_node.eval_average = current_node.eval_sum / current_node.eval_count
                current_node = current_node.parent
            # And we should end up at the None node above the ur_node

    def make_choice_score(self):
        '''Choose a child node using the eval_average'''
        best_child = self.ur_node.children[0]
        for child in self.ur_node.children:
            if child.eval_average > best_child.eval_average:
                # Since the ur_node uses the ur_side to maximize, we
                # can compare the eval_averages, which were calculated
                # based on the ur_side
                best_child = child
        return (best_child.last_move, best_child.eval_average,
                best_child.eval_count)

    def make_choice_visits(self):
        '''Choose a child node depending on which one was visited the most'''
        best_child = self.ur_node.children[0]
        for child in self.ur_node.children:
            if child.eval_count > best_child.eval_count:
                best_child = child
            print(child.last_move, child.eval_average,
                  child.eval_count)
        return (best_child.last_move, best_child.eval_average,
                best_child.eval_count)


class Node:
    '''A node in this tree'''

    def __init__(self, board, parent, last_move=None):
        self.board = board
        self.parent = parent
        self.eval_sum = 0
        self.eval_count = 0
        self.eval_average = 0
        self.children = []
        self.last_move = last_move

    def is_leaf(self):
        return not self.children

    def magic_formula(self, ur_side, curiosity):
        '''Returns the sum of this node's exploration and exploitation
        values. It takes into account which side we are currently
        on. I got this from the MCTS Wikipedia page.'''
        import math
        #CURIOSITY = 0.1
        # Wikipedia suggested 2, but I think that's too high. 1 also seems too
        # high. 0 is maybe too low, in that the computer doesn't seem to manage to think
        # about the direct consequence of its move. 0.5 is too high, for the same
        # reason as the previous sentence, but with more confidence. 0.1 is too
        # high.
        if self.eval_count == 0:
            exploration = 100  # That is, infinity
        else:
            exploration = math.sqrt(
                curiosity *
                math.log(
                    self.parent.eval_count) /
                self.eval_count)
        if self.board.side != ur_side:
            # Then we're OK because the parent, i.e. the place from
            # which we're choosing, agrees with the ur_side and
            # thus agrees with the scores we've averaged
            exploitation = self.eval_average
        else:
            exploitation = 1 - self.eval_average
        return exploration + exploitation

    def add_children(self):
        '''Adds children to the node. Has to calculate moves'''
        # Do nothing if we're in an end game position
        self.board.calculate_moves()
        if self.board.score3('r') in (0, 1):
            # The 'r' is completely arbitrary
            return
        moves = self.board.clean(self.board.moves[self.board.side])
        for m in moves:
            next_board = self.board.copy()
            next_board.move(m)
            self.children.append(Node(next_board, self, m))
