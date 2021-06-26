#include <stdio.h>
#include <math.h>

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

float getSaturationVaporPressure(float celc){
    float exponent = (7.5 * celc) / (celc + 237.3);
    return  6.1078 * 100 * pow(10, exponent);
}

int main(){
    int running = 1;
    int reset = 1;

    while (running > 0){
        // temperature variables
        float fahrenheit, celcius, kelvin;
        // pressure variables
        float inHg, pascals, hectopascals;
        // get temperature input
        printf("What's the temperature in Farenheit?\n");
        scanf("%f", &fahrenheit);
        // do temperature conversions
        celcius = toCelcius(fahrenheit);
        kelvin = toKelvin(celcius);
        // get pressure input
        printf("What is the pressure in inHg?\n");
        scanf("%f", &inHg);
        // do pressure conversions
        pascals = toPascal(inHg);
        hectopascals = toHectoPascal(pascals);
        // air density calculations
        float saturation_vapor_pressure;
        saturation_vapor_pressure = getSaturationVaporPressure(celcius);


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