import numpy as np
# 0 => non visiter, 1 => obstacle, 2 => robot, 3 => libre, 4 visit
#Pour tester :  0 => libre, 1 => obstacle, 2 => robot, 4 visit
Prio = ["u","r","d","l"] #up == on est monté 
#i ligne
Pile=[]
Flag = False
terrain =          [[1,1,1,1,1,1],
                   [1,0,0,1,0,1],
                   [1,0,0,1,0,1],
                   [1,1,0,0,0,1],
                   [1,0,0,0,0,1],
                   [1,0,0,0,0,1],
                   [1,2,0,0,0,1],
                   [1,1,1,1,1,1]]


def find(terrain,id):
    for i in range(8):
        for j in range(6):
            if (terrain[i][j]==id):
                return i,j
    return -1,-1

def main(terrain,Flag,Pile):
    x,y=find(terrain,2)
    if x==-1:
        print("Ya pas de robot")
        return False
    run=True
    while run==True:
        affichage(terrain)
        print(Pile)
        if Flag==False:
            i,j=find(terrain,2)
            #cas=terrain[y]
            if terrain[i-1][j]==0: #Repasse à 3 le test
                execute_move(terrain,"u")
                Pile.append("u")
            elif terrain[i][j+1]==0: #Repasse à 3 le test
                execute_move(terrain,"r")
                Pile.append("r")
            elif terrain[i+1][j]==0: #Repasse à 3 le test
                
                execute_move(terrain,"d")
                Pile.append("d")
            elif terrain[i][j-1]==0: #Repasse à 3 le test
                execute_move(terrain,"l")
                Pile.append("l")
            else:
                i,j=find(terrain,0)
                if i==-1:
                    run=False
                else:
                    Flag=True
        else:
            print("Passage March arr")
            marche_arr_mode(terrain)
            print("Sortie March arr")
            Flag=False

def marche_arr_mode(terrain):
    Flag=True
    while(Flag==True):
        i,j=find(terrain,2)
        affichage(terrain)
        move = Pile.pop()
        if(move=="d"):
            execute_move(terrain,"u")
        elif(move=="l"):
            execute_move(terrain,"r")
        elif(move=="u"):
            execute_move(terrain,"d")
        elif(move=="r"):
            execute_move(terrain,"l")
            
        if (Pile[-1]=="d") and (terrain[i][j-1]!=1 or terrain[i][j+1]!=1 ):
            Flag=False
        elif (Pile[-1]=="l") and (terrain[i-1][j]!=1 or terrain[i+1][j]!=1 ):
            Flag=False
        elif (Pile[-1]=="u") and (terrain[i][j-1]!=1 or terrain[i][j+1]!=1 ):
            Flag=False
        elif (Pile[-1]=="r") and (terrain[i-1][j]!=1 or terrain[i+1][j]!=1 ):
            Flag=False
        
            #Execute move direction : up if move = down etc...
        #TODO

def execute_move(terrain,dirr):
    i,j=find(terrain,2)
    if dirr=="d":
        terrain[i][j]=4
        terrain[i+1][j]=2
        #Move down
    elif dirr=="l":
        terrain[i][j]=4
        terrain[i][j-1]=2
        #Move left
    elif dirr=="u":
        terrain[i][j]=4
        terrain[i-1][j]=2
        #Move up
    elif dirr=="r":
        terrain[i][j]=4
        terrain[i][j+1]=2
        #Move right

def affichage(terrain):
    for i in range(len(terrain)):
        print(terrain[i])
    print("\n\n")
    
main(terrain, Flag, Pile)

#Bonne chance


    
                
        
                
            



    

