#Begin file
#Dom_computer.py
def Computer1(c): #First computer player, can only play depth 2
        moveplan={}
        for possmove in c.clean(c.moves[c.side]):
            temp=c.copy()
            temp.move(possmove)
            templist=[]
            for nextmove in temp.clean(temp.moves[temp.side]):
                copy=temp.copy()
                copy.move(nextmove)
                templist.append(copy)
            numlist=[]
            for entry in templist:
                numlist.append(entry.score(entry.side))
            moveplan[possmove]=min(numlist)
        k=max(moveplan.values())
        for goodmove in moveplan.keys():
            if moveplan[goodmove]==k:
                return [goodmove, k]
def Computer2(c,totaldepth=2): #can play to any depth, long text
    tempmove="placeholder"
    tempscore=-1
    for possmove in c.clean(c.moves[c.side]):
            temp=c.copy()
            temp.move(possmove)
            r=rank(temp,c.side,1,totaldepth)
            #print tempscore
            #print tempmove 
            if tempscore==-1:
                tempscore=r
                tempmove=possmove
            #print r
            if r>=tempscore:
                tempscore=r
                tempmove=possmove
            #print [possmove,r]
    return [tempmove,tempscore]
def rank(board,sidetowin,depth,totaldepth):
    if depth==totaldepth or board.score(sidetowin) in (0,10l**10):
        return board.score(sidetowin)
    if board.side==sidetowin: 
        tempscore=-1
        for possmove in board.clean(board.moves[board.side]):
            temp=board.copy()
            temp.move(possmove)
            r=rank(temp,sidetowin,depth+1,totaldepth)
            if r>=tempscore:
                tempscore=r
        return tempscore
    else:
        tempscore=10l**100
        for possmove in board.clean(board.moves[board.side]):
            temp=board.copy()
            temp.move(possmove)
            r=rank(temp,sidetowin,depth+1,totaldepth)
            if r<=tempscore:
                tempscore=r
        return tempscore
def Computer3(c,depth=2): #can play to any depth, short text, uses -1000 to 1000
    tempmove="placeholder"
    tempscore=-1000
    for possmove in c.clean(c.moves[c.side]):
            temp=c.copy()
            temp.move(possmove)
            r=-rank2(temp,depth-1) 
            if r>=tempscore:
                tempscore=r
                tempmove=possmove
            #print [possmove,r]
    return [tempmove,tempscore]
def rank2(board,depth):
    if depth==0 or board.score2(board.side) in (-1000,1000):
        return board.score2(board.side)
    tempscore=-1000
    for possmove in board.clean(board.moves[board.side]):
        temp=board.copy()
        temp.move(possmove)
        r=-rank2(temp,depth-1)
        if r>=tempscore:
            tempscore=r
    return tempscore
def Computer5(c,depth=2):#first to use alpha beta
    alpha=-1000
    beta=1000
    bestmove="placeholder"
    bestscore=-1000
    for possmove in c.clean(c.moves[c.side]):
            temp=c.copy()
            temp.move(possmove)
            r=-rank5(temp,depth-1,-beta,-alpha)
            if r>=bestscore:
                bestscore=r
                bestmove=possmove
            if bestscore>alpha:
                alpha=bestscore
            if alpha>=beta:
                return [bestmove,alpha]
            #print [possmove,r]
    return [bestmove,bestscore]
def rank5(board,depth,alpha=-1000,beta=1000):
    if depth==0 or board.score2(board.side) in (-1000,1000):
        return board.score2(board.side)
    bestscore=-1000
    for possmove in board.clean(board.moves[board.side]):
        temp=board.copy()
        temp.move(possmove)
        r=-rank5(temp,depth-1,-beta,-alpha)
        if r>bestscore:
            bestscore=r
        if bestscore>alpha:
            alpha=bestscore
        if alpha>=beta:
            return alpha
    return bestscore
def Computer6(c,depth=2,time_limit=60):#first to use time limits and iterative deepening, not the direct ancestor of 7 and 8 but an older sibling
    from time import time
    end_time=time()+time_limit
    best_list=[]
    for a_depth in range(1,depth+1):
        alpha=-1000
        beta=1000
        bestmove="placeholder"
        bestscore=-1000
        for possmove in c.clean(c.moves[c.side]):
            temp=c.copy()
            temp.move(possmove)
            r=-rank6(temp,a_depth-1,-beta,-alpha,end_time)
            if time()>end_time:
                break
            if r>=bestscore:
                bestscore=r
                bestmove=possmove
            if bestscore>alpha:
                alpha=bestscore
            if alpha>=beta:
                best_list=[bestmove,alpha,a_depth]
                break
            #print [possmove,r]
        if time()<end_time:
            best_list=[bestmove,bestscore,a_depth]
        else:
            break
    return best_list
def rank6(board,depth,alpha=-1000,beta=1000,end_time=2000000000):
    from time import time
    if depth==0 or board.score2(board.side) in (-1000,1000):
        return board.score2(board.side)
    bestscore=-1000
    for possmove in board.clean(board.moves[board.side]):
        temp=board.copy()
        temp.move(possmove)
        r=-rank6(temp,depth-1,-beta,-alpha,end_time)
        if time()>end_time:
            return 3
        if r>bestscore:
            bestscore=r
        if bestscore>alpha:
            alpha=bestscore
        if alpha>=beta:
            return alpha
    return bestscore
def Computer7(c,depth=2,time_limit=60):#first to order moves using previous iterations, orders with n-1 at every level
    from time import time
    end_time=time()+time_limit
    best_list=[]
    move_order=[]
    #deeper_move_order=[]
    for a_depth in range(1,depth+1):
        num_move_order=[]
        new_move_order=[]
        new_deeper_move_order=[]
        alpha=-1000
        beta=1000
        bestmove="placeholder"
        bestscore=-1000
        if len(move_order)==0:
            moves=c.clean(c.moves[c.side])
            deeper_move_order=[]
        else:
            moves=move_order[:-1]
            deeper_move_order=move_order[-1]
        for i in range(0,len(moves)):
            possmove=moves[i]
            temp=c.copy()
            temp.move(possmove)
            if len(deeper_move_order)==0:
                k=[]
            else:
                k=deeper_move_order[i]
            #print a_depth, k,move_order
            rank=rank7(temp,a_depth-1,-beta,-alpha,end_time,k)
            r=-rank[0]
            if time()>end_time:
                break
            if len(num_move_order)==0:
                num_move_order+=[r]
                new_move_order+=[possmove] 
                new_deeper_move_order+=[rank[1]]
            else:
                for x in range(0,len(num_move_order)):
                    if r>num_move_order[x]:
                        num_move_order=num_move_order[:x]+[r]+num_move_order[x:]
                        new_move_order=new_move_order[:x]+[possmove]+new_move_order[x:] 
                        new_deeper_move_order=new_deeper_move_order[:x]+[rank[1]]+new_deeper_move_order[x:] 
            if r>=bestscore:
                bestscore=r
                bestmove=possmove
            if bestscore>alpha:
                alpha=bestscore
            if alpha>=beta:
                best_list=[bestmove,alpha]
                move_order=new_move_order+[new_deeper_move_order]
                break
            #print [possmove,r]
        if time()<end_time:
            best_list=[bestmove,bestscore]
            move_order=new_move_order+[new_deeper_move_order]
        else:
            break
    return best_list
def rank7(board,depth,alpha=-1000,beta=1000,end_time=2000000000,move_order=[]):
    from time import time
    if depth==0 or board.score2(board.side) in (-1000,1000):
        return [board.score2(board.side),[]]
    num_move_order=[]
    new_move_order=[]
    new_deeper_move_order=[]
    bestscore=-1000
    if len(move_order)==0:
            moves=board.clean(board.moves[board.side])
            deeper_move_order=[]
    else:
            moves=move_order[:-1]
            deeper_move_order=move_order[-1]
    for i in range(0,len(moves)):
        possmove=moves[i]
        temp=board.copy()
        temp.move(possmove)
        if len(deeper_move_order)==0:
            k=[]
        else:
            k=deeper_move_order[i]
        #print depth,k,move_order
        rank=rank7(temp,depth-1,-beta,-alpha,end_time,k)
        r=-rank[0]
        if time()>end_time:
            return [3,[3]]
        if len(num_move_order)==0:
                num_move_order+=[r]
                new_move_order+=[possmove]
                new_deeper_move_order+=[rank[1]]
        else:
            for x in range(0,len(num_move_order)):
                if r>num_move_order[x]:
                    num_move_order=num_move_order[:x]+[r]+num_move_order[x:]
                    new_move_order=new_move_order[:x]+[possmove]+new_move_order[x:] 
                    new_deeper_move_order=new_deeper_move_order[:x]+[rank[1]]+new_deeper_move_order[x:] 
        if r>bestscore:
            bestscore=r
        if bestscore>alpha:
            alpha=bestscore
        if alpha>=beta:
            return [alpha,new_move_order+[new_deeper_move_order]]
    return [bestscore,new_move_order+[new_deeper_move_order]]
def Computer8(c,depth=2,time_limit=60,ordering=0):#uses user defined ordering at every level
    from time import time
    end_time=time()+time_limit
    best_list=[]
    for a_depth in range(1,depth+1):
        alpha=-1000
        beta=1000
        bestmove="placeholder"
        bestscore=-1000
        new_ordering=ordering
        moves=c.clean(c.moves[c.side])
        while new_ordering>=depth:
            new_ordering+=-1
        if new_ordering!=0:
            moves.sort(key=lambda move_in_list: -rank8(c.copy().move(move_in_list,True),new_ordering-1,-beta,-alpha,end_time), reverse=True) 
        for possmove in moves: #WARNING: There is a high chance that moves is reversed, which would explain why optimization slows down Dom9. This may be the case also in Dom7 or Dom8.
            temp=c.copy()
            temp.move(possmove)
            r=-rank8(temp,a_depth-1,-beta,-alpha,end_time,ordering)
            if time()>end_time:
                break
            if r>=bestscore:
                bestscore=r
                bestmove=possmove
            if bestscore>alpha:
                alpha=bestscore
            if alpha>=beta:
                best_list=[bestmove,alpha]
                break
            #print [possmove,r]
        if time()<end_time:
            best_list=[bestmove,bestscore]
        else:
            break
    return best_list
def rank8(board,depth,alpha=-1000,beta=1000,end_time=2000000000,ordering=0):
    from time import time
    if depth==0 or board.score2(board.side) in (-1000,1000):
        return board.score2(board.side)
    bestscore=-1000
    new_ordering=ordering
    moves=board.clean(board.moves[board.side])
    while new_ordering>=depth:
        new_ordering+=-1
    if new_ordering!=0:
        moves.sort(key=lambda move_in_list: -rank8(board.copy().move(move_in_list,True),new_ordering-1,-beta,-alpha,end_time), reverse=True) 
    for possmove in moves:
        temp=board.copy()
        temp.move(possmove)
        r=-rank8(temp,depth-1,-beta,-alpha,end_time,ordering)
        if time()>end_time:
            return 3
        if r>bestscore:
            bestscore=r
        if bestscore>alpha:
            alpha=bestscore
        if alpha>=beta:
            return alpha
    return bestscore
def Computer9(c,depth=2,time_limit=60,ordering=0):#uses user defined ordering at the first level only, direct descendant of 6 and shares some features with 8
    from time import time
    end_time=time()+time_limit
    best_list=[]
    for a_depth in range(1,depth+1):
        alpha=-1000
        beta=1000
        bestmove="placeholder"
        bestscore=-1000
        moves=c.clean(c.moves[c.side])
        if ordering>0:
            moves.sort(key=lambda move_in_list: -rank9(c.copy().move(move_in_list,True),ordering-1,-beta,-alpha,end_time), reverse=True) 
        for possmove in moves:
            temp=c.copy()
            temp.move(possmove)
            r=-rank9(temp,a_depth-1,-beta,-alpha,end_time)
            if time()>end_time:
                break
            if r>=bestscore:
                bestscore=r
                bestmove=possmove
            if bestscore>alpha:
                alpha=bestscore
            if alpha>=beta:
                best_list=[bestmove,alpha,a_depth]
                break
            #print [possmove,r]
        if time()<end_time:
            best_list=[bestmove,bestscore,a_depth]
        else:
            break
    return best_list
def rank9(board,depth,alpha=-1000,beta=1000,end_time=2000000000):
    from time import time
    if depth==0 or board.score2(board.side) in (-1000,1000):
        return board.score2(board.side)
    bestscore=-1000
    for possmove in board.clean(board.moves[board.side]):
        temp=board.copy()
        temp.move(possmove)
        r=-rank9(temp,depth-1,-beta,-alpha,end_time)
        if time()>end_time:
            return 3
        if r>bestscore:
            bestscore=r
        if bestscore>alpha:
            alpha=bestscore
        if alpha>=beta:
            return alpha
    return bestscore
#Computer10 will use iterative deepening. It will use ordering only at the first level. It will get the ordering from the last iteration
#Computer11 might use ordering at the first two levels from previous iterations. It may be possible to use all levels of previous iterations, maybe with a hash table.
#Can processing become faster if r and g are replaced by something more binary?
#Make the computer able to play versus itself, repeatedly. That is, a Dom program should ask the user who the players should be, and their time limits and characteristics.
#Is it a waste to use e to the power?
#Change the static evaluator such that it considers not only relative moves, but also centrality, height of towers, etc. To do this, have Dom strategies evolve against each other.
# If the game becomes repetitive or there are no more captures, maybe the computer should adjust its strategy. Maybe try to combine towers to get reserves.




        
        
            



