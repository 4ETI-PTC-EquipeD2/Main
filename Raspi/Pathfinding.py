# 0 => non visiter, 1 => obstacle, 2 => robot, 3 => libre, 4 visit
#Pour tester :  0 => libre, 1 => obstacle, 2 => robot, 4 visit
#Prio = ["u","r","d","l"] #up == on est monté 
#i ligne

import time as t
import map_movement as m

terrain =          [[1,1,1,1,1,1],
                   [1,0,0,1,0,1],
                   [1,0,0,1,0,1],
                   [1,1,0,0,0,1],
                   [1,0,0,0,0,1],
                   [1,0,0,0,0,1],
                   [1,2,0,0,0,1],
                   [1,1,1,1,1,1]]
gameId="test"

"""

x=0
y=0
Dico={}
Dico[(x,y)]=0
print(Dico)
"""


def find(terrain,id):
    for i in range(8):
        for j in range(6):
            if (terrain[i][j]==id):
                return i,j
    return -1,-1

def find_all_interieur(terrain,id):
    listId=[]
    for i in range(1,7):
        for j in range(1,5):
            if (terrain[i][j]==id):
                listId.append([j-1,i-1])
    return listId

def main(terrain):
    affichage(terrain)
    Pile=[]
    Flag = False
    x,y=find(terrain,2)
    if x==-1:
        print("Ya pas de robot")
        return False
    run=True
    while run==True:
        
        #print(Pile)
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
            #print("Passage March arr")
            marche_arr_mode(terrain,Pile)
            #print("Sortie March arr")
            Flag=False

def marche_arr_mode(terrain,Pile):
    Flag=True
    while(Flag==True):
        i,j=find(terrain,2)
        
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

def execute_move(terrain,dirr): #Essaye de rajouter à chaque #Move dirr l'appel d'une fonction qui prend le terrain, le converti en dic[(x,y)]
    i,j=find(terrain,2)
    if dirr=="d":
        terrain[i][j]=4
        terrain[i+1][j]=2
        m.send_movement(2,gameId)
        #Move down
    elif dirr=="l":
        terrain[i][j]=4
        terrain[i][j-1]=2
        m.send_movement(3,gameId)
        #Move left
    elif dirr=="u":
        terrain[i][j]=4
        terrain[i-1][j]=2
        m.send_movement(1,gameId)
        #Move up
    elif dirr=="r":
        terrain[i][j]=4
        terrain[i][j+1]=2
        m.send_movement(4,gameId)
        #Move right
    affichage(terrain)
    t.sleep(1)

def affichage(terrain):
    for i in range(len(terrain)):
        print(terrain[i])
    print("\n\n")

def find_obstacle(terrain, commande, distance):
    i,j = find(terrain, 2)
    if commande=='0':  #0°
        if distance<50:
            terrain[i][j-1]=1
        elif distance<100:
            terrain[i][j-2]=1
        elif distance<150:
            terrain[i][j-3]=1
    elif commande=='1':  #90°
        if distance<50:
            terrain[i-1][j]=1
        elif distance<100:
            terrain[i-2][j]=1
        elif distance<150:
            terrain[i-3][j]=1
        elif distance<200:
            terrain[i-4][j]=1
        elif distance<250:
            terrain[i-5][j]=1
    elif commande=='2':  #180°
        if distance<50:
            terrain[i][j+1]=1
        elif distance<100:
            terrain[i][j+2]=1
        elif distance<150:
            terrain[i][j+2]=1
    return terrain

if __name__ == "__main__":
    listObstacles=find_all_interieur(terrain,1)
    for i in listObstacles:
        m.send_obstacle(i,gameId)
    main(terrain)

#Bonne chance


    
                
        
                
            



    

