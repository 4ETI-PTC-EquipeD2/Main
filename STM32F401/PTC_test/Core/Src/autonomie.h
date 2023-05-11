/*
 * autonomie.h
 *
 *  Created on: May 9, 2023
 *      Author: anico
 */

#ifndef SRC_AUTONOMIE_H_
#define SRC_AUTONOMIE_H_

void forward_back (float l,char wheel_1,char wheel_2,char * commande);
void turn_forward (int angle, char * commande);
void select_commande (int n_com, char * commande,char * commande_i);




#endif /* SRC_AUTONOMIE_H_ */
