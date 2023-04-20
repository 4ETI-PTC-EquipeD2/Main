/*
 * test.c
 *
 *  Created on: Mar 21, 2023
 *      Author: evann.nalewajek
 */


#include "stm32f3xx.h"
#include "main.h"
#include <stdio.h>
#include <string.h>


void test(TIM_HandleTypeDef htim2)
{
//  // Activation de l'horloge pour les ports A et E
//  RCC->AHBENR |= RCC_AHBENR_GPIOAEN | RCC_AHBENR_GPIOEEN;
//
//  // Configuration de la broche PE9 en mode sortie (pour la LED LD3)
//  GPIOE->MODER |= GPIO_MODER_MODER9_0;
//
//  // Configuration de la broche PA0 en mode entrée avec pull-up (pour le bouton USER)
//  GPIOA->MODER &= ~GPIO_MODER_MODER0;
//  GPIOA->PUPDR |= GPIO_PUPDR_PUPDR0_0;

	uint32_t start_time = 0;
	uint32_t end_time = 0;
	float distance = 0;
	float sound_speed = 343.595*100;
	float elapsed_time = 0;



	HAL_GPIO_WritePin(TRIG_GPIO_Port, TRIG_Pin, GPIO_PIN_SET);
	HAL_Delay(1); //ms
	HAL_GPIO_WritePin(TRIG_GPIO_Port, TRIG_Pin, GPIO_PIN_RESET);

	if (HAL_GPIO_ReadPin(ECHO_GPIO_Port, ECHO_Pin) == GPIO_PIN_SET ){
		HAL_GPIO_WritePin(LD4_GPIO_Port, LD4_Pin, GPIO_PIN_RESET);
		HAL_TIM_Base_Start(&htim2);
		start_time = __HAL_TIM_GET_COUNTER(&htim2);
		while(1){
			if (HAL_GPIO_ReadPin(ECHO_GPIO_Port, ECHO_Pin) == GPIO_PIN_RESET ){
				HAL_GPIO_WritePin(LD4_GPIO_Port, LD4_Pin, GPIO_PIN_SET);
				end_time = __HAL_TIM_GET_COUNTER(&htim2);
				elapsed_time = ((float) (end_time - start_time)) / ((float) HAL_RCC_GetPCLK1Freq() * 2);
				distance = sound_speed*elapsed_time;
				start_time = 0;
				end_time = 0;
				break;
			}
		}
	}

	return (distance);



		/*if (HAL_GPIO_ReadPin(B1_GPIO_Port, B1_Pin) == GPIO_PIN_SET){
			// Allumer la LED LD3
			HAL_GPIO_WritePin(LD3_GPIO_Port, LD3_Pin, GPIO_PIN_SET);
			HAL_GPIO_WritePin(TRIG_GPIO_Port, TRIG_Pin, GPIO_PIN_SET);
			HAL_Delay(1); //ms
			HAL_GPIO_WritePin(TRIG_GPIO_Port, TRIG_Pin, GPIO_PIN_RESET);
			// Éteindre la LED LD3
			HAL_GPIO_WritePin(LD3_GPIO_Port, LD3_Pin, GPIO_PIN_RESET);

		}


		if (HAL_GPIO_ReadPin(ECHO_GPIO_Port, ECHO_Pin) == GPIO_PIN_SET ){
			HAL_GPIO_WritePin(LD4_GPIO_Port, LD4_Pin, GPIO_PIN_SET);
			HAL_Delay(100);
		}
		else{
			HAL_GPIO_WritePin(LD4_GPIO_Port, LD4_Pin, GPIO_PIN_RESET);
		}*/
}
