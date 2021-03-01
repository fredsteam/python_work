/**********************************************************************
* Filename 	  : 22.Relay.c
* Description : Make a relay to contral led blinking
* Author      : Robot
* E-mail      : support@rexqualis.com
* website     : www.rexqualis.com
* Update      : Tim    2019/12/02
**********************************************************************/
#include <wiringPi.h>
#include <stdio.h>
#define RelayPin 0

int main(void){
    if(wiringPiSetup() == -1){ //when initialize wiring failed, print message to screen
        printf("setup wiringPi failed !");
        return 1;
    }
    pinMode(RelayPin, OUTPUT);   //set GPIO17(GPIO0) output
    while(1){
        // Tick
        printf("Relay Open......\n");
        digitalWrite(RelayPin, LOW);
        delay(1000);
        // Tock
        printf("......Relay Close\n");
        digitalWrite(RelayPin, HIGH);
        delay(1000);
    }

    return 0;
}
