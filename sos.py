#greetings
print("===================")
print("WELCOME TO SOS GAME")
print("\n")
print("======YOO==========")
print("\n")
print("===2 PLAYER GAME===")
print("\n")
#SOS table size
print("Enter you SOS TABLE SIZE")
s=int(input())
#initializing all blocks to empty
g=[[0 for i in range(s)] for j in range(s)]
k=1
for i in range(s):
    for j in range(s):
        g[i][j]=k
        k=k+1
#changing positions
pipe=[0,0]
pipe[0]=1
#counting filled blocks
k=0
#points of players
p1=0
p2=0
#initailizing all empty blocks as X
z=[['X' for i in range(s)] for j in range(s)]
while(k!=(s*s)):
    print("\n")
    print("        ===      ====                        ")
    print("        SOS      GAME                        ")
    print("        ===      ====                        ")
    print("\n")
    print("======================================")
    for i in range(s):
        for j in range(s):
            if(z[i][j]=='s'):
                print('s',end=" ")
            elif(z[i][j]=='o'):
                print('o',end=" ")
            else:
                print(g[i][j],end=" ")
        print("\n")
    print("======================================")
    k+=1
    if(pipe[0]):
        print("Player 1's Chance Now....")
    if(pipe[1]):
        print("Player 2's Chance Now....")
    print("ENTER POSITION :: ")
    p=int(input())
    p-=1
    print("ENTER S OR O :: ")
    q=input()
    print("======================================")
    #if input is S
    if(q=="s"):
        a=int(p/s)
        b=int(p%s)
        c=0
        d=0
        z[a][b]='s'
        #total 8 ways
        #1st way
        if((b+2)<s):
            if(z[a][b+1]=='o' and z[a][b+2]=='s'):
                if(pipe[0]):
                    c+=1
                    print("===Player 1 got a Point===")
                if(pipe[1]):
                    d+=1
                    print("===Player 2 got a Point===")
        #2nd way
        if((a+2)<s and (b+2)<s):
            if(z[a+1][b+1]=='o' and z[a+2][b+2]=='s'):
                if(pipe[0]):
                    c+=1
                    print("===Player 1 got a Point===")
                if(pipe[1]):
                    d+=1
                    print("===Player 2 got a Point===")
        #3rd way
        if((a+2)<s):
            if(z[a+1][b]=='o' and z[a+2][b]=='s'):
                if(pipe[0]):
                    c+=1
                    print("===Player 1 got a Point===")
                if(pipe[1]):
                    d+=1
                    print("===Player 2 got a Point===")
        #4th way
        if((a+2)<s and (b-2)>=0):
            if(z[a+1][b-1]=='o' and z[a+2][b-2]=='s'):
                if(pipe[0]):
                    c+=1
                    print("===Player 1 got a Point===")
                if(pipe[1]):
                    d+=1
                    print("===Player 2 got a Point===")
        #5th way
        if((b-2)>=0):
            if(z[a][b-1]=='o' and z[a][b-2]=='s'):
                if(pipe[0]):
                    c+=1
                    print("===Player 1 got a Point===")
                if(pipe[1]):
                    d+=1
                    print("===Player 2 got a Point===")
        #6th way
        if((a-2)>=0 and (b-2)>=0):
            if(z[a-1][b-1]=='o' and z[a-2][b-2]=='s'):
                if(pipe[0]):
                    c+=1
                    print("===Player 1 got a Point===")
                if(pipe[1]):
                    d+=1
                    print("===Player 2 got a Point===")
        #7th way
        if((a-2)>=0):
            if(z[a-1][b]=='o' and z[a-2][b]=='s'):
                if(pipe[0]):
                    c+=1
                    print("===Player 1 got a Point===")
                if(pipe[1]):
                    d+=1
                    print("===Player 2 got a Point===")
        #8th way
        if((a-2)>=0 and (b+2)<s):
            if(z[a-1][b+1]=='o' and z[a-2][b+2]=='s'):
                if(pipe[0]):
                    c+=1
                    print("===Player 1 got a Point===")
                if(pipe[1]):
                    d+=1
                    print("===Player 2 got a Point===")
        p1+=c
        p2+=d
        if(c>0):
            pipe[0]=1
        elif(d>0):
            pipe[1]=1
        elif(pipe[0]):
            pipe[1]=1
            pipe[0]=0
        elif(pipe[1]):
            pipe[1]=0
            pipe[0]=1
    elif(q=="o"):
        a=int(p/s)
        b=int(p%s)
        c=0
        d=0
        z[a][b]='o'
        #total 4 ways
        #way 1
        if((b-1)>=0 and b+1<s):
            if(z[a][b-1]=='s' and z[a][b+1]=='s'):
                if(pipe[0]):
                    c+=1
                    print("===Player 1 got a Point===")
                if(pipe[1]):
                    d+=1
                    print("===Player 2 got a Point===")
        #way2
        if((a-1)>=0 and a+1<s):
            if(z[a-1][b]=='s' and z[a+1][b]=='s'):
                if(pipe[0]):
                    c+=1
                    print("===Player 1 got a Point===")
                if(pipe[1]):
                    d+=1
                    print("===Player 2 got a Point===")
        #way3
        if((a-1)>=0 and (b-1)>=0 and (a+1)<s and b+1<s):
            if(z[a-1][b-1]=='s' and z[a+1][b+1]=='s'):
                if(pipe[0]):
                    c+=1
                    print("===Player 1 got a Point===")
                if(pipe[1]):
                    d+=1
                    print("===Player 2 got a Point===")
        #way 4
        if((a-1)>=0 and (b-1)>=0 and (a+1)<s and b+1<s):
            if(z[a-1][b+1]=='s' and z[a+1][b-1]=='s'):
                if(pipe[0]):
                    c+=1
                    print("===Player 1 got a Point===")
                if(pipe[1]):
                    d+=1
                    print("===Player 2 got a Point===")
        p1+=c
        p2+=d
        if(c>0):
            pipe[0]=1
        elif(d>0):
            pipe[1]=1
        elif(pipe[0]):
            pipe[1]=1
            pipe[0]=0
        elif(pipe[1]):
            pipe[1]=0
            pipe[0]=1
    else:
        k-=1
    print("==========================================")
    print("\n")
print("==============================================")
print("\n")
print("\n")
print("GAME OVER")
print("\n")
print("Final Points Are::")
print("\n")
print("Player 1 :: ",p1)
print("Player 2 :: ",p2)
print("===============================================")
if(k==s*s):
    if(p1>p2):
        print(":::::: Player 1 WINS ::::::")
    elif(p1<p2):
        print("::::: Player 2 wins ::::::")
    else:
        print("Match is Tie......")
#end of the code
#thanks....................
