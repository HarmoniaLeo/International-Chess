class chess:
    __x=0
    __y=0
    __isBlack=0
    
    def getX(self):
        return self._chess__x
    
    def getY(self):
        return self._chess__y
    
    def moveTo(self,x,y):
        if not plate[y][x]=="0":
            del plate[y][x]
        plate[y][x]=plate[self._chess__y][self._chess__x]
        del plate[self._chess__y][self._chess__x]
        self._chess__x=x
        self._chess__y=y
    
    def isBlack(self):
        return self._chess__isBlack
    
    def __init__(self,x,y,isBlack):
        self._chess__y=y
        self._chess__x=x
        self._chess__isBlack=isBlack
    
class Pawn(chess):
    __moved=0
    __movedTwo=0


    def __init__(self,x,y,isBlack):
        self._chess__y=y
        self._chess__x=x
        self._chess__isBlack=isBlack
        self._Pawn__moved=0
        self._Pawn__movedTwo=0
    
    def movedTwo(self):
        return self._Pawn__moveTwo
    
    def move(self,x,y):
        if self._Pawn__moved:
            if not abs(y-self._chess__y)==1:
                return 0
        else:
            if not(abs(y-self._chess__y)==1 or abs(y-self._chess__y)==2):
                return 0
        if abs(y-self._chess__y)==2:
            if not abs(x-self._chess__x)==0:
                return 0
            if not plate[y][x]=="0":
                    if plate[y][x].isBlack==self._chess__isBlack:
                        return 0
            if self._Pawn__moved==0:
                self._Pawn__moveTwo=1
        else:
            if abs(x-self._chess__x)>1:
                return 0
            if abs(x-self._chess__x)==1:
                if plate[y][x]=="0":
                    if str(type(plate[self._chess__y][x]))=="<class 'Pawn'>":
                        if plate[self._chess__y][x].movedTwo:
                            del plate[self._chess__y][x]
                            plate[self._chess__y][x]="0"
                        else:
                            return 0
                    else:
                        return 0
                if plate[y][x].isBlack==self._chess__isBlack:
                    return 0
            else:
                if not plate[y][x]=="0":
                    if plate[y][x].isBlack==self._chess__isBlack:
                        return 0
            self._Pawn__moveTwo=0
        self._Pawn__moved=1
        self.moveTo(x,y)
        if(self._chess__isBlack):
            if(y==7):
                return 2
        else:
            if(y==0):
                return 2
        return 1
                
            
    def crt(self):
        if self._chess__isBlack:
            return "P"
        else:
            return "p"

class Knight(chess):
    def move(self,x,y):
        if (not (abs(x-self._chess__x)==2 and abs(y-self._chess__x)==1)) or (not (abs(x-self._chess__x)==1 and abs(y-self._chess__x)==2)):
            return 0
        if not plate[y][x]=="0":
            if plate[y][x].isBlack==self._chess__isBlack:
                return 0
        self.moveTo(x,y)
        return 1
    
    def crt(self):
        if self._chess__isBlack:
            return "N"
        else:
            return "n"

class Bishop(chess):  
    def move(self,x,y):
        if not abs(x-self._chess__x)==abs(y-self._chess__y):
            return 0
        for x1 in range(min(x,self._chess__x)+1,max(x,self._chess__x)):
            for y1 in range(min(y,self._chess__y)+1,max(y,self._chess__y)):
                if(not plate[y1][x1]=="0"):
                    return 0
        if not plate[y][x]=="0":
            if plate[y][x].isBlack==self._chess__isBlack:
                return 0
        self.moveTo(x,y)
        return 1
    
    def crt(self):
        if self._chess__isBlack:
            return "B"
        else:
            return "b"

class Castle(chess):
    __moved=0
    
    def __init__(self,x,y,isBlack):
        self._chess__y=y
        self._chess__x=x
        self._chess__isBlack=isBlack
        self._Castle__moved=0

    def ifMoved(self):
        return self._Castle__moved
    
    def move(self,x,y):
        if not (x==self._chess__x or y==self._chess__y):
            return 0
        if y==self._chess__y:
            for x1 in range(min(x,self._chess__x)+1,max(x,self._chess__x)):
                if(not plate[y][x1]=="0"):
                    return 0
        else:
            for y1 in range(min(y,self._chess__y)+1,max(y,self._chess__y)):
                if(not plate[y1][x]=="0"):
                    return 0
        if not plate[y][x]=="0":
            if plate[y][x].isBlack==self._chess__isBlack:
                return 0
        __moved=1
        self.moveTo(x,y)
        return 1
    
    def crt(self):
        if self._chess__isBlack:
            return "R"
        else:
            return "r"
    
class Queen(chess):
    def move(self,x,y):
        if not (x==self._chess__x or y==self._chess__y or (abs(x-self._chess__x)==abs(y-self._chess__y))):
            return 0
        if y==self._chess__y:
            for x1 in range(min(x,self._chess__x)+1,max(x,self._chess__x)):
                if(not plate[y][x1]=="0"):
                    return 0
        elif x==self._chess__x:
            for y1 in range(min(y,self._chess__y)+1,max(y,self._chess__y)):
                if(not plate[y1][x]=="0"):
                    return 0
        else:
            for x1 in range(min(x,self._chess__x)+1,max(x,self._chess__x)):
                for y1 in range(min(y,self._chess__y)+1,max(y,self._chess__y)):
                    if(not plate[y1][x1]=="0"):
                        return 0
        if not plate[y][x]=="0":
            if plate[y][x].isBlack==self._chess__isBlack:
                return 0
        self.moveTo(x,y)
        return 1

    
    def crt(self):
        if self._chess__isBlack:
            return "Q"
        else:
            return "q"

class King(chess):
    __moved=0
    
    def __init__(self,x,y,isBlack):
        self._chess__y=y
        self._chess__x=x
        self._chess__isBlack=isBlack
        self._King__moved=0

    def move(self,x,y):
        if(not(abs(chess.__x-x)<=1 and abs(chess.__y-y)<=1)):
            return 0
        if not plate[y][x]=="0":
            if plate[y][x].isBlack==self._chess__isBlack:
                if self._King__moved==0 and str(type(plate[y][x]))=="<class 'Castle'>" and plate[y][x].ifMoved()==0:
                    for x1 in range(self._chess__x+1,x):
                        if not plate[y][x1]=="0":
                            if not plate[y][x1].isBlack==self._chess__isBlack:
                                return 0
                    tmp=plate[y][x]
                    del plate[y][x]
                    plate[y][x]=self
                    plate[self._chess__y][self._chess__x]="0"
                    tmp.moveTo(self._chess__x,self._chess__y)
                    return 1
                else:
                    return 0
        self.moveTo(x,y)
        return 1
    
    def crt(self):
        if self._chess__isBlack:
            return "K"
        else:
            return "k"
        
def printPlate():
    print("  A B C D E F G H")
    for i in range(0,8):
        string=str(i+1)+" "
        for j in range(0,8):
            if plate[i][j]=="0":
                string+=plate[i][j]+" "
            else:
                string+=plate[i][j].crt()+" "
        print(string)

def evo(x,y):
    tmp=plate[y][x]
    print("升变为:")
    ch=input()
    if ch=="q":
        plate[y][x]=Queen(x,y,tmp.isBlack)
    elif ch=="r":
        plate[y][x]=Castle(x,y,tmp.isBlack)
    elif ch=="n":
        plate[y][x]=Knight(x,y,tmp.isBlack)
    elif ch=="b":
        plate[y][x]=Bishop(x,y,tmp.isBlack)
    del tmp
        
global plate
plate=[["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0"]]
for i in range(0,8):
    plate[1][i]=Pawn(i,1,1)
for j in range(0,8):
    plate[6][j]=Pawn(j,1,0)
plate[0][0]=Castle(0,0,1)
plate[0][7]=Castle(7,0,1)
plate[7][0]=Castle(0,7,0)
plate[7][7]=Castle(7,7,0)
plate[0][1]=Knight(1,0,1)
plate[0][6]=Knight(6,0,1)
plate[7][1]=Knight(1,7,0)
plate[7][6]=Knight(6,7,0)
plate[0][2]=Bishop(2,0,1)
plate[0][5]=Bishop(5,0,1)
plate[7][2]=Bishop(2,7,0)
plate[7][5]=Bishop(5,7,0)
plate[0][3]=King(3,0,1)
plate[0][4]=Queen(4,0,1)
plate[7][3]=King(3,7,0)
plate[7][4]=Queen(4,7,0)

symbol=["白","黑"]
diction={"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7}
while True:
    for i in range(0,2):
        printPlate()
        while True:
            print(symbol[i]+"方行动:\n从")
            print("x:")
            x1=input()
            print("y:")
            y1=int(input())
            if (y1>=1 and y1<=8) and (x1 in diction):
                if plate[y1-1][diction[x1]].isBlack()==i:
                    break
            print("此处没有棋子")
        while True:
            print("到")
            print("x:")
            x2=input()
            print("y:")
            y2=int(input())
            if (y2>=1 and y2<=8) and (x2 in diction):
                if(plate[y1-1][diction[x1]].move(diction[x2],y2-1)==1):
                    break
                if(plate[y1-1][diction[x1]].move(diction[x2],y2-1)==2):
                    evo(diction[x1],y1-1)
                    break
            print("不能移动到此")