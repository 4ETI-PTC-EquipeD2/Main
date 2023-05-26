/*
 * servo.c
 *
 *  Created on: May 23, 2023
 *      Author: anico
 */
//Import -----------------------------------------------------------------------------------------
#include <stdio.h>
#include <string.h>
//#include "main.h"
//Fonctions ---------------------------------------------------------------------------------------
//void Distance_Sensor(float distance,TIM_HandleTypeDef htim2){
//  	  uint32_t start_time = 0;
//  	  uint32_t end_time = 0;
//  	  float elapsed_time = 0;
//  	  float sound_speed = 343.595*100;
//
//
//  	  HAL_GPIO_WritePin(TRIG_GPIO_Port, TRIG_Pin, GPIO_PIN_SET);
//  	  HAL_Delay(1); //ms
//  	  HAL_GPIO_WritePin(TRIG_GPIO_Port, TRIG_Pin, GPIO_PIN_RESET);
//
//  	  while (HAL_GPIO_ReadPin(ECHO_GPIO_Port, ECHO_Pin) == GPIO_PIN_RESET);
//
//  	  HAL_TIM_Base_Start(&htim2);
//  	  start_time = __HAL_TIM_GET_COUNTER(&htim2);
//
//  	  while (HAL_GPIO_ReadPin(ECHO_GPIO_Port, ECHO_Pin) == GPIO_PIN_SET);
//
//  	  end_time = __HAL_TIM_GET_COUNTER(&htim2);
//  	  elapsed_time = ((float) (end_time - start_time)) / ((float) HAL_RCC_GetPCLK1Freq() * 2);
//  	  distance = 35 * sound_speed * elapsed_time;
//    }
//
//  void ServoMotor(int angle,float distance, TIM_HandleTypeDef htim2, TIM_HandleTypeDef htim3){
//	  switch (angle){
//	  case 0:
//		  htim3.Instance->CCR2 = 3; //0°
//		  HAL_Delay(2000);
//		  Distance_Sensor(distance,htim2);
//		  break;
//	  case 90:
//		  htim3.Instance->CCR2 = 7; //90°
//		  HAL_Delay(2000);
//		  Distance_Sensor(distance,htim2);
//		  break;
//	  case 180:
//		  htim3.Instance->CCR2 = 12; //180°
//		  HAL_Delay(2000);
//		  Distance_Sensor(distance,htim2);
//		  break;
//	  default:
//		  break;
//	  }
//
//  }
//
