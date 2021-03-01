/**********************************************************************
* Filename    : 1.Blinking_LED
* Description : Make an led blinking.
* Author      : Robot
* E-mail      : support@rexqualis.com
* website     : www.rexqualis.com
* Update      : Tim   2019/12/02
**********************************************************************/
#include <wiringPi.h>  
#include <stdio.h>
#define LedPin      0
int main(void)
{
    // When initialize wiring failed, print message to screen
    if(wiringPiSetup() == -1){
        printf("setup wiringPi failed !");
        return 1;
    }
    pinMode(LedPin, OUTPUT);// Set LedPin as output to write value to it.
    while(1){
        // LED on
        digitalWrite(LedPin, LOW);
        printf("...LED on\n");
        delay(1000);
        // LED off
        digitalWrite(LedPin, HIGH);
        printf("LED off...\n");
        delay(1000);
    }
    return 0;
}

