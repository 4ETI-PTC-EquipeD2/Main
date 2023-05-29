/*
 * autonomie.h
 *
 *  Created on: May 23, 2023
 *      Author: anico
 */

#ifndef SRC_AUTONOMIE_H_
#define SRC_AUTONOMIE_H_

/*
* @brief : Cette fonction permet de formater la commande digo à envoyer au robot.
* @Param :
* 	l (float) = distance à parcourir
* 	 wheel_1/2 (char) = soit " " ou "-" pour permettre à la roue concernée de tourner
* 	 dans le sens horaire ou anti-horaire.
* 	commande (char *) = tableau de char contenant la commande à envoyer au robot.
* 						Cette variable est modifiée au cours de la fonction.
* @Return : none
* */
void forward_back (float l,char wheel_1,char wheel_2,char * commande);

/*
* @brief : Cette fonction permet de formater la commande digo à envoyer au robot lorsque
* 			que celui-ci tourne à droite ou gauche.
* @Param :
* 	angle (int) = inférieur à 0 lorsque l'on tourne à gauche, supérieur pour tourner à droite.
* 	commande (char *) = tabelau de char contenant la commande à envoyer au robot.
* @Return : none
* */
void turn_forward (int angle, char * commande);

#endif /* SRC_AUTONOMIE_H_ */
