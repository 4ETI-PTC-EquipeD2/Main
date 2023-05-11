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
unsigned char * forward_back (float l,char wheel_1,char wheel_2){
	if (l <= 50) {
		int tick_value = (int)(l*690)/20;
		char *return_value =  NULL;
		free(return_value);
		return_value = (char *) malloc( 24 * sizeof(char));
		sprintf(return_value,"digo 1:%i:%c10 2:%i:%c10\r",tick_value,wheel_1,tick_value,wheel_2);
		return return_value;
	}
	else {
		return ((unsigned char*)"none");
	}
}

unsigned char * cat_value(unsigned char* first_value, unsigned char* second_value){
	char *return_value =  NULL;
	free(return_value);
	return_value = (char *) malloc( 24 * sizeof(char));
	sprintf(return_value,"%s/%s",first_value,second_value);
	return (unsigned char *)return_value;
}

unsigned char * turn_forward (int angle){
	float r = 12.25;
	float distance = (M_PI*r)/2;
	if (angle < 0){ //tourner à gauche
		unsigned char * first_value = forward_back(distance,' ','-');
		unsigned char * second_value = forward_back(50.0,'-','-');
		return cat_value(first_value,second_value);
	}
	else if (angle > 0) {//tourner à droite
		unsigned char * first_value = forward_back(distance,'-',' ');
		unsigned char * second_value = forward_back(50.0,'-','-');
		return cat_value(first_value,second_value);
	}
	else {//demi-tour
		unsigned char * first_value = forward_back(4*distance,'-',' ');
		unsigned char * second_value = forward_back(50.0,'-','-');
		return cat_value(first_value,second_value);
	}
}

unsigned char * select_commande (int n_com, unsigned char * commande){
	int car;
	for(car = 0; car < strlen((char*)commande)-1; car ++){
		if ((char)commande[car] == '/'){
			if (n_com == 1){
				char * commande_1 = "";
				strncpy(commande_1,(char*)commande, car);
				return (unsigned char*)commande_1;
			}else{
				char * commande_2 = "";
				strncpy(commande_2,(char*)commande+car, strlen((char*)commande)-1-car);
				return (unsigned char*)commande_2;
			}
		}
	}
}
