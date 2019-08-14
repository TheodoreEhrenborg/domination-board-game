#Begin file
#Dom_board.py
class Board:
    def __init__(self,currentboard=["","x","x","","","","","x","x","x","r","r","g","g","r","r","x","","g","g","r","r","g","g","","","r","r","g","g","r","r","","","g","g","r","r","g","g","","","r","r","g","g","r","r","","x","g","g","r","r","g","g","x","x","x","","","","","x","x"],side="r",):
        self.reserve=currentboard[0]
       self.mainboard=currentboard[1:]
        self.moves={"g":self.findmoves("g"),"r":self.findmoves("r")}
        self.side=side
    def create_skeleton(self):
        open="| "
        for x in range(0,3):
            open+=open
        open+="|\n"
        closed="+-"
        for x in range(0,3):
            closed+=closed
        closed+="+\n"
        five=""
        for x in range(0,5):
            five+=open
        skeleton=closed+five
        for x in range(0,3):
            skeleton+=skeleton
        skeleton+=closed
        skeleton=" a b c d e f g h \n"+skeleton
        new=""
        for x in range(0,len(skeleton)):
            a=x%18
            b=(x-a)/18
            if a==0:
                if b%6==2:
                    new+=str((b-2)/6+1)
                else:
                    new+=" "
            new+=skeleton[x]
        skeleton=new
        for i in range(0,len(skeleton)):
        #for i in range(0,25):
            list=self.num_to_coord(i)
           ## if list[1]>45:
           ##     print list, i 
            x=list[0]
            y=list[1]
            #print i, skeleton[i],x,y,((x<3 and y>37) or (x<5 and y>43) or (x<3 and y<13) or (x<5 and y<7) or  (x>15 and y>37) or (x>13 and y>43) or (x>15 and y<13) or (x>13 and y<7)) and x<18
            if ((x<4 and y>37) or (x<6 and y>43) or (x<4 and y<13) or (x<6 and y<7) or  (x>16 and y>37) or (x>14 and y>43) or (x>16 and y<13) or (x>14 and y<7)) and x<19 and skeleton[i] not in "abcdefgh12345678":
               skeleton=self.switch(skeleton,i," ")
        skeleton=self.switch(skeleton,931,"g:",2)
        skeleton=self.switch(skeleton,912,"r:",2)
        self.skeleton=skeleton
        ##return skeleton
    def display(self):
        try:
            image=self.skeleton
        except AttributeError:
            self.create_skeleton()
            image=self.skeleton
        r_num=self.reserve.count("r")
        g_num=self.reserve.count("g")
        r_str=str(r_num)
        g_str=str(g_num)
        while len(r_str)<2:
            r_str+=" "
        while len(g_str)<2:
            g_str+=" "
        image=self.switch(image,933,g_str,2)
        image=self.switch(image,914,r_str,2)
        main_board=self.mainboard[:]
        for i in range(0,64):
            if main_board[i]!="x":
                while len(main_board[i])<5:
                    main_board[i]+=" "
                a=i%8
                b=(i-a)/8
                place=19*6*(b+1)+2*a+1+1
                for j in range(0,5):
                    image=self.switch(image,place-19*j,main_board[i][j])
        print image           
    def switch(self,string,place,char,length=1):
        return string[:place]+char+string[place+length:]
    def num_to_coord(self,num): #Lower left is [1,1]
        a=num%19
        b=(num-a)/19
        y=50-b
        x=a+1
        return [x,y]
    def coord_to_num(self,x,y):
        a=x-1
        b=50-y
        return a+19*b
    def findmoves(self,side):
        movelist=[]
        if side in self.reserve:
            for j in range(0,self.reserve.count(side)):
                for i in range(0,64):
                    if self.mainboard[i]!="x":
                        movelist.append("rr"+self.numtostr(i))
        for i in range(0,64):
            if self.mainboard[i]!="x" and self.mainboard[i]!="" and self.mainboard[i][-1:]==side:
                length=0
                while length<len(self.mainboard[i]):
                    length+=1
                    if i+length in range(0,64) and (i%8)+length<=7:
                        if self.mainboard[i+length]!="x":
                            movelist.append(self.numtostr(i)+self.numtostr(i+length))
                    if i-length in range(0,64) and (i%8)-length>=0:
                        if self.mainboard[i-length]!="x":
                            movelist.append(self.numtostr(i)+self.numtostr(i-length))
                    if i+8*length in range(0,64):
                        if self.mainboard[i+8*length]!="x":
                            movelist.append(self.numtostr(i)+self.numtostr(i+8*length))
                    if i-8*length in range(0,64):
                        if self.mainboard[i-8*length]!="x":
                            movelist.append(self.numtostr(i)+self.numtostr(i-8*length))
        return movelist
    def numtostr(self,num):
        a=num%8
        b=(num-a)/8
        stra="abcdefgh"
        strb="12345678"
        return stra[a:a+1]+strb[b:b+1]
    def opponent(self,side):
        if side=="r":
            return "g"
        else:
            return "r"
    def strtonum(self,str):
        if str=="rr":
            return str
        stra="abcdefgh"
        strb="12345678"
        return stra.find(str[0])+8*strb.find(str[1])
    def move(self,move, send=False):
        if move in self.moves[self.side]:
            start=move[0:2]
            end=move[2:4]
            start=self.strtonum(start)
            end=self.strtonum(end)
            if start=="rr":
                k=self.reserve.find(self.side)
                self.reserve=self.reserve[:k]+self.reserve[k+1:]
                pieces=self.side
            else:
                k=start-end
                if k<0:
                    k=-k
                if k>=8:
                    k=k/8
                pieces=self.mainboard[start][-k:]
                self.mainboard[start]=self.mainboard[start][:-k]
            self.mainboard[end]+=pieces
            while len(self.mainboard[end])>5:
                piece=self.mainboard[end][0:1]
                self.mainboard[end]=self.mainboard[end][1:]
                if piece==self.side:
                    self.reserve+=piece
            self.side=self.opponent(self.side)
            self.moves={"g":self.findmoves("g"),"r":self.findmoves("r")}
        if send==True:
            return self 
    def clean(self,firstlist):
        list=firstlist[:]
        newlist=[]
        for entry in list:
            if entry not in newlist:
                newlist.append(entry)
        return newlist
    def copy(self):
        return Board([self.reserve]+self.mainboard,self.side)
    def score(self,side):
        if len(self.moves[side])==0:
            return 0
        if len(self.moves[self.opponent(side)])==0:
            return 10l**10
        return float(len(self.moves[side]))/float(len(self.moves[self.opponent(side)]))
    def score2(self,side):
        import math
        if len(self.moves[side])==0:
            return -1000
        if len(self.moves[self.opponent(side)])==0:
            return 1000
        return math.log(float(len(self.moves[side]))/float(len(self.moves[self.opponent(side)])))













