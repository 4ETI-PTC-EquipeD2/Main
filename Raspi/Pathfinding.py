import numpy as np
# 0 => non visiter, 1 => obstacle, 2 => robot, 3 => libre, 4 visit
Prio = ["u","r","d","l"]
Pile=[]
Flag = False
terrain = np.array([1,1,1,1,1,1],
                   [1,0,0,0,0,1],
                   [1,0,0,0,0,1],
                   [1,0,0,0,0,1],
                   [1,0,0,0,0,1],
                   [1,0,0,0,0,1],
                   [1,2,0,0,0,1],
                   [1,1,1,1,1,1])


def find(terrain,id):
    for i in range(7):
        for j in range(4)
            if (terrain[i][j]==id):
                return i,j
    return -1,-1

def main(terrain,Flag,Pile):
    run=True
    while run==True:
        if Flag==False:
            i,j=find_robot(terrain,2)
            cas=terrain[y]
            if terrain(i+1,j)==3:
                #GOOOOO
                Pile.append("d")
            elif terrain(i,j+1)==3:
                #GOOOOO
                Pile.append("l")
            elif terrain(i-1,j)==3:
                #GOOOOO
                Pile.append("u")
            elif terrain(i,j-1)==3:
                #GOOOOO
                Pile.append("r")
            else:
                i,j=find_robot(terrain,0)
                if i==-1:
                    run=False
                else:
                    Flag=True
        else:
            marche_arr(terrain)
            Flag=False

def marche_arr(terrain,i,j)
    while(Flag==True):
        #TODO
#Bonne chance


    
                
        
                
            



    

