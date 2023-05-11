import librairie_STM32 as l
from serial import Serial
ser = Serial()
l.init_UART(ser,19200,'COM3')
print(l.Send_Receive_UART(ser,"z"))


char * forward_back (float l,char wheel_1,char wheel_2){
	if (l <= 50) {
		int tick_value = (int)(l*690)/20;
		char *return_value =  NULL;
		free(return_value);
		return_value = (char *) malloc( 24 * sizeof(char));
		sprintf(return_value,"digo 1:%i:%c10 2:%i:%c10\r",tick_value,wheel_1,tick_value,wheel_2);
		return return_value;
	}
	else {
		return "none";
	}
}

char * cat_value(char* first_value,char* second_value){
	char *return_value =  NULL;
	free(return_value);
	return_value = (char *) malloc( 24 * sizeof(char));
	sprintf(return_value,"%s/%s",first_value,second_value);
	return return_value;
}

char * turn_forward (int angle){
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

char * select_commande (int n_com, unsigned char * commande){
	int car;
	for(car = 0; car < strlen((char*)commande)-1; car ++){
		if ((char)commande[car] == '/'){
			if (n_com == 1){
				char *commande_1 = NULL;
				free(commande_1);
				commande_1 = (char *) malloc( 26 * sizeof(char));
				strncpy(commande_1,commande, car);
				return commande_1;
			}else{
				char *commande_2 = NULL;
				free(commande_2);
				commande_2 = (char *) malloc( 26 * sizeof(char));
				strncpy(commande_2,commande+car, strlen(commande-1-car);
				return commande_2;
			}
		}
	}
}
 
 
/* USER CODE BEGIN PV */
unsigned char received, serializerResp[100];
char commande[60], commande_1[60],commande_2[60];
/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);
static void MX_GPIO_Init(void);
static void MX_USART2_UART_Init(void);
static void MX_USART1_UART_Init(void);
static void MX_USART6_UART_Init(void);
/* USER CODE BEGIN PFP */

/* USER CODE END PFP */

/* Private user code ---------------------------------------------------------*/
/* USER CODE BEGIN 0 */
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{

	if (huart == &huart1){ // commande recue de la PI
		HAL_UART_Transmit(&huart1, &received, 1,HAL_MAX_DELAY);
		HAL_UART_Transmit(&huart1, (unsigned char*)'\n', 1,HAL_MAX_DELAY);
		if (received == 'z'){
			commande = forward_back(50,'-','-');
			HAL_UART_Transmit(&huart6,commande,strlen(commande),HAL_MAX_DELAY);
		}
		else if (received == 'a'){
			HAL_UART_Transmit(&huart6, (unsigned char *)"stop\r",5,HAL_MAX_DELAY);
		}
		else if (received == 'q'){
			commande = turn_forward(-1);
			commande_1 = *select_commande(1, commande);
			commande_2 = *select_commande(1, commande);
			HAL_UART_Transmit(&huart6,commande_1,strlen((char*)commande_1),HAL_MAX_DELAY);
			HAL_UART_Transmit(&huart6,commande_2,strlen((char*)commande_2),HAL_MAX_DELAY);
		}
		else if (received == 'd'){
			commande = turn_forward(1);
			commande_1 = *select_commande(1, commande);
			commande_2 = *select_commande(1, commande);
			HAL_UART_Transmit(&huart6,&commande_1,strlen((char*)commande_1),HAL_MAX_DELAY);
			HAL_UART_Transmit(&huart6,&commande_2,strlen((char*)commande_2),HAL_MAX_DELAY);
		}
		else if (received == 's'){
			commande = forward_back(50,' ',' ');
			HAL_UART_Transmit(&huart6,commande,strlen((char*)commande),HAL_MAX_DELAY);
		}
	}
	else if(huart == &huart6){ // commande recue du Serializer
		if (received != '>'){
			HAL_UART_Transmit(&huart1, &received, 1,HAL_MAX_DELAY);
		}
		else{
			HAL_UART_Transmit(&huart1, (unsigned char*)'\n', 1,HAL_MAX_DELAY);
		}
	}
    HAL_UART_Receive_IT(huart, &received, 1);
}
