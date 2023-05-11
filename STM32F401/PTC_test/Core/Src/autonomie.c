/*
 * autonomie.c
 *
 *  Created on: May 9, 2023
 *      Author: anico
 */
//Import -----------------------------------------------------------------------------------------
#include <string.h>
#include <math.h>
#include <stdio.h>
#include <assert.h>

//Fonctions --------------------------------------------------------------------------------------
void forward_back (float l,char wheel_1,char wheel_2,char * commande){
	if (l <= 50) {
		int tick_value = (int)(l*700*1.15)/20;
		sprintf(commande,"digo 1:%c%i:%c10 2:%c%i:10\r",wheel_1,tick_value,wheel_2,tick_value);
	}
}

void turn_forward (int angle, char * commande){
	float r = 13.5;
	float distance = (M_PI*r)/2;
	if (angle < 0){ //tourner à gauche
		char first_value[60];
		forward_back(distance,' ','-', first_value);
		char second_value [60];
		forward_back(50.0,'-','-', second_value);
		sprintf(commande,"%s/%s",first_value,second_value);
	}
	else if (angle > 0) {//tourner à droite
		char first_value [60];
		forward_back(distance,'-',' ', first_value);
		char second_value [60];
		forward_back(50.0,'-','-', second_value);
		sprintf(commande,"%s/%s",first_value,second_value);
	}
	else {//demi-tour
		char first_value[60];
		forward_back(4*distance,'-',' ', first_value);
		char second_value [60];
		forward_back(50.0,'-','-', second_value);
		sprintf(commande,"%s/%s",first_value,second_value);
	}
}

void select_commande (int n_com, char * commande,char * commande_i){
	int car;
	for(car = 0; car < strlen((char*)commande)-1; car ++){
		if ((char)commande[car] == '/'){
			if (n_com == 1){
				strncpy(commande_i,commande, car);
			}else{
				strncpy(commande_i,commande+car+1, strlen(commande)-car);
			}
		}
	}
}
