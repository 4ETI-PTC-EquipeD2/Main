/*
 * autonomie.c
 *
 *  Created on: May 23, 2023
 *      Author: anico
 */
//Import -----------------------------------------------------------------------------------------
#include <string.h>
#include <math.h>
#include <stdio.h>

//Fonctions --------------------------------------------------------------------------------------
void forward_back (float l,char wheel_1,char wheel_2,char * commande){
	if (l <= 50) {
		int tick_value = (int)(l*650)/20;
		sprintf(commande,"digo 1:%c%i:8 2:%c%i:8\r",wheel_1,tick_value,wheel_2,tick_value);
	}
}

void turn_forward (int angle, char * commande){
	float r = 11;
	float distance = (M_PI*r)/2;
	if (angle < 0){ //tourner à gauche
		forward_back(distance,' ','-', commande);
	}
	else if (angle > 0) {//tourner à droite
		forward_back(distance,'-',' ', commande);
	}
}

