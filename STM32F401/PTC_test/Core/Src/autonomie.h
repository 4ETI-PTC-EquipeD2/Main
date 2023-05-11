/*
 * autonomie.h
 *
 *  Created on: May 9, 2023
 *      Author: anico
 */

#ifndef SRC_AUTONOMIE_H_
#define SRC_AUTONOMIE_H_

unsigned char * forward_back (float l,char wheel_1,char wheel_2);
unsigned char * cat_value(unsigned char* first_value, unsigned char* second_value);
unsigned char * turn_forward (int angle);
unsigned char * select_commande (int n_com, unsigned char * commande);




#endif /* SRC_AUTONOMIE_H_ */
