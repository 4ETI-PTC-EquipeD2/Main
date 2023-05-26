/*
 * servo.h
 *
 *  Created on: May 23, 2023
 *      Author: anico
 */

#ifndef SRC_SERVO_H_
#define SRC_SERVO_H_

void Distance_Sensor(float distance);
void ServoMotor(int angle,float distance,TIM_HandleTypeDef htim2,TIM_HandleTypeDef htim3);

#endif /* SRC_SERVO_H_ */
