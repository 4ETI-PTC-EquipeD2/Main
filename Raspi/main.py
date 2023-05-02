"""
Fichier main qui permet de commander l'ensemble du robot.
"""
#Import ----------------------------------------------------
import math
import librairie_STM32 as lST
import numpy as np
from serial import Serial
import librairie_Serv as lSV
#Variables -------------------------------------------------
#Description matrice du terrain 
# 0 => non visiter, 1 => obstacle, 2 => robot, 3 => libre
terrain = np.array([0000],[0000],[0000],[0000],[0000],[2000])

run = True
#Main -------------------------------------------------------------------------
ser = Serial()
#Initialisation 
lSV.init_UART(ser, 19200,'COM7')

#Boucle d'actions
while (run) : 
    
    terrain = lST.obstacle_scan(terrain)
    terrain = lST.avancer_case(terrain)
    if lST.detec_QRCode != -1 :
        ordre = lSV.send_qr_id(str(id))
        if ordre == "attaquer" :
           lSV.attaquer() #créer un protocole de communication
        else :
            None
                       
           
    