################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (10.3-2021.10)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Core/UART_comm/handleCmd.c 

OBJS += \
./Core/UART_comm/handleCmd.o 

C_DEPS += \
./Core/UART_comm/handleCmd.d 


# Each subdirectory must supply rules for building sources it contributes
Core/UART_comm/%.o Core/UART_comm/%.su: ../Core/UART_comm/%.c Core/UART_comm/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32F401xE -c -I../Core/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc -I../Drivers/STM32F4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32F4xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Core-2f-UART_comm

clean-Core-2f-UART_comm:
	-$(RM) ./Core/UART_comm/handleCmd.d ./Core/UART_comm/handleCmd.o ./Core/UART_comm/handleCmd.su

.PHONY: clean-Core-2f-UART_comm

