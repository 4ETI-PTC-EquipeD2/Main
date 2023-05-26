# 0 => non visiter, 1 => obstacle, 2 => robot, 3 => libre, 4 visit
#Pour tester :  0 => libre, 1 => obstacle, 2 => robot, 4 visit
#Prio = ["u","r","d","l"] #up == on est monté 
#i ligne

import time as t
import map_movement as m
gameId="test"
dico_lastMove_listDirr={"u": ["l","u","r"],"r": ["u","r","d"],"d": ["r","d","l"],"l": ["d","l","u"]}
"""
terrain =         [[1,1,1,1,1,1],
                   [1,0,0,1,0,1],
                   [1,0,0,1,0,1],
                   [1,1,0,0,0,1],
                   [1,0,0,0,0,1],
                   [1,0,0,0,0,1],
                   [1,2,0,0,0,1],
                   [1,1,1,1,1,1]]



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

def obstacle_voisin(terrain):
    #Renvoie une lettre désignant la direction() et n si il n'y a pas d'obstacle
    i,j=find(terrain,2)
    if (terrain[i+1][j]==1):
         return "d"
    elif (terrain[i-1][j]==1):
         return "u"
    elif (terrain[i][j+1]==1):
         return "r"
    elif (terrain[i][j-1]==1):
         return "l"
    else:
        return "n"



def find_all_interieur(terrain,id):
    listId=[]
    for i in range(1,7):
        for j in range(1,5):
            if (terrain[i][j]==id):
                listId.append([j-1,i-1])
    return listId

def main(terrain,run,Flag,Pile):
    x,y=find(terrain,2)
    if x==-1:
        print("Ya pas de robot")
        return terrain,run,Flag,Pile

    
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
        terrain,Flag,Pile = marche_arr_mode(terrain,Pile,Flag)
        
        #print("Sortie March arr")
    return run,terrain,Flag,Pile

def marche_arr_mode(terrain,Pile,Flag):
    as_move=True
    i,j=find(terrain,2)
    
    move = Pile.pop()
    if(move=="d"):
        as_move=execute_move(terrain,"u")
    elif(move=="l"):
        as_move=execute_move(terrain,"r")
    elif(move=="u"):
        as_move=execute_move(terrain,"d")
    elif(move=="r"):
        as_move=execute_move(terrain,"l")
    if not as_move:
        Pile.append(move)
        
    if (Pile[-1]=="d") and (terrain[i][j-1]!=1 or terrain[i][j+1]!=1 or terrain[i][j-1]!=5 or terrain[i][j+1]!=5):
        Flag=False
    elif (Pile[-1]=="l") and (terrain[i-1][j]!=1 or terrain[i+1][j]!=1 or terrain[i-1][j]!=5 or terrain[i+1][j]!=5 ):
        Flag=False
    elif (Pile[-1]=="u") and (terrain[i][j-1]!=1 or terrain[i][j+1]!=1 or terrain[i][j-1]!=5 or terrain[i][j+1]!=5):
        Flag=False
    elif (Pile[-1]=="r") and (terrain[i-1][j]!=1 or terrain[i+1][j]!=1 or terrain[i-1][j]!=5 or terrain[i+1][j]!=5):
        Flag=False
    return terrain,Flag,Pile
        #Execute move direction : up if move = down etc...

def execute_move(terrain,dirr): #Essaye de rajouter à chaque #Move dirr l'appel d'une fonction qui prend le terrain, le converti en dic[(x,y)]
    i,j=find(terrain,2)
    if dirr=="d":
        """
        reussi=Send_Receive_UART('dx')
        if reussi=="ack":
            #Met le reste là
        """
        terrain[i][j]=4
        terrain[i+1][j]=2
        m.send_movement(2,gameId)
        
    elif dirr=="l":
        """
        reussi=Send_Receive_UART('lx')
        if reussi=="ack":
            #Met le reste là
        """
        terrain[i][j]=4
        terrain[i][j-1]=2
        m.send_movement(3,gameId)
        
    elif dirr=="u":
        """
        reussi=Send_Receive_UART('u')
        if reussi=="ack":
            reussi=Send_Receive_UART('x')
            if reussi=="ack":
                #Met le reste là
            #Met le reste là
        """
        terrain[i][j]=4
        terrain[i-1][j]=2
        m.send_movement(1,gameId)
        
    elif dirr=="r":
        """
        reussi=Send_Receive_UART('rx')
        if reussi=="ack":
            #Met le reste là
        """
        terrain[i][j]=4
        terrain[i][j+1]=2
        m.send_movement(4,gameId)
    
    
        
    affichage(terrain)
    t.sleep(1)
    #if reussi=="nack":
        #return False
    return True

def affichage(terrain):
    for i in range(len(terrain)):
        print(terrain[i])
    print("\n\n")

def find_obstacle(terrain, commande, distance, lastMove):
    i,j = find(terrain, 2)
    dirr=dico_lastMove_listDirr[lastMove][commande] #Avec le lastMove, et la commande donnée, trouve la dirrection dans laquelle est actuellement tourné le capteur dans le refe
    if dirr=='l':
        if distance<50 and j>=2:
            terrain[i][j-1]=1
        elif distance<100 and j>=3:
            terrain[i][j-2]=1
        elif distance<150 and j>=4:
            terrain[i][j-3]=1
    elif dirr=='u':
        if distance<50 and i>=2:
            terrain[i-1][j]=1
        elif distance<100 and i>=3:
            terrain[i-2][j]=1
        elif distance<150 and i>=4:
            terrain[i-3][j]=1
        elif distance<200 and i>=5:
            terrain[i-4][j]=1
        elif distance<250 and i>=6:
            terrain[i-5][j]=1
    elif dirr=='r':
        if distance<50 and j<=4:
            terrain[i][j+1] 
        elif distance<100:
            terrain[i][j+2]=1 and j<=3
        elif distance<150:
            terrain[i][j+2]=1 and j<=2
    elif dirr=='d':
        if distance<50 and i>=2:
            terrain[i+1][j]=1
        elif distance<100 and i>=3:
            terrain[i+2][j]=1
        elif distance<150 and i>=4:
            terrain[i+3][j]=1
        elif distance<200 and i>=5:
            terrain[i+4][j]=1
        elif distance<250 and i>=6:
            terrain[i+5][j]=1
    return terrain

if __name__ == "__main__":
    #Alors c'est sensé servir pour testé mais ya pas la bcl du main donc ttfaçon on ira pas bien loin...
    terrain =     [[1,1,1,1,1,1],
                   [1,0,0,1,0,1],
                   [1,0,0,1,0,1],
                   [1,1,0,0,0,1],
                   [1,0,0,0,0,1],
                   [1,0,0,0,0,1],
                   [1,2,0,0,0,1],
                   [1,1,1,1,1,1]]
    listObstacles=find_all_interieur(terrain,1)
    for i in listObstacles:
        m.send_obstacle(i,gameId)
    main(terrain)

#Bonne chance



    
                
        
                
            



    

