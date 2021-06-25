#include <stdio.h>

#define UNIVERSAL_GAS_CONSTANT = 8.312 // J/(K*mol)
#define AIR_MOLAR_MASS = 0.0289654 // kg/mol
#define VAPOR_MOLAR_MASS = 0.018016 // kg/mol

int main(){
    int running = 1;
    int reset = 1;

    while (running > 0){
        int fahrenheit;
        printf("What's the temperature in Farenheit?\n");
        scanf("%d", &fahrenheit);
        printf("The temperature is %d degrees\n", fahrenheit);
        // put statements and queries for user here
        printf("Do you want to reset the loop? 1/0\n");
        scanf("%d", &reset);
        if (reset > 0){// can use ascii values to compare chars
            running = 1;
        }
        else {
            running = 0;
        }
    }
    puts("I'm out");

    return 0;
}