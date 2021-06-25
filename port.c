#include <stdio.h>

#define UNIVERSAL_GAS_CONSTANT = 8.312 // J/(K*mol)
#define AIR_MOLAR_MASS = 0.0289654 // kg/mol
#define VAPOR_MOLAR_MASS = 0.018016 // kg/mol

float toCelcius(float fahr){
    return (fahr - 32) / 1.8;
}

float toKelvin(float celc){
    return celc + 273.15;
}

float toPascal(float inhg){
    return inhg * 3386.38867;
}

float toHectoPascal(float pasc){
    return pasc * 0.01;
}

int main(){
    int running = 1;
    int reset = 1;

    while (running > 0){
        float fahrenheit, celcius, kelvin;
        float inHg, pascals, hectopascals;
        printf("What's the temperature in Farenheit?\n");
        scanf("%f", &fahrenheit);
        celcius = toCelcius(fahrenheit);
        kelvin = toKelvin(celcius);
        printf("What is the pressure in inHg?\n");
        scanf("%f", &inHg);
        pascals = toPascal(inHg);
        hectopascals = toHectoPascal(pascals);

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