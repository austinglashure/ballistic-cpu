#include <stdio.h>
#include <math.h>

#define UNIVERSAL_GAS_CONSTANT 8.312 // J/(K*mol)
#define AIR_MOLAR_MASS 0.0289654 // kg/mol
#define VAPOR_MOLAR_MASS 0.018016 // kg/mol
#define TIME_IMPULSE 0.001 // milliseconds

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

float getVaporPressure(float hum, float sat_vap_pressure){
    return sat_vap_pressure * hum;
}

float getAirPressure(float vap_pressure, float pasc){
    return pasc - vap_pressure;
}

float getAirDensity(float dry_part, float vap_part, float kelv){
    float numer = (dry_part * AIR_MOLAR_MASS) + (vap_part * VAPOR_MOLAR_MASS);
    float denom = UNIVERSAL_GAS_CONSTANT * kelv;
    return numer / denom;
}

struct Gun {
    float bc;
    float caliber;
    float mass;
    float muzzle_velocity;
};

int main(){
    int running = 1;
    int reset = 1;

    struct Gun a;
    a.bc = 0.45;
    a.caliber = 0.0078232; // in meters .308"
    a.mass = 0.01069182; // in kilograms 165 grains
    a.muzzle_velocity = 860; // in meters 2821 fps

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
        // air density variable instanciations
        float saturation_vapor_pressure, humidity;
        float vapor_pressure, air_pressure, air_density;
        // query user for humidity
        printf("What is the humidity? 0-100\n");
        scanf("%f", &humidity);
        // air density calculations
        saturation_vapor_pressure = getSaturationVaporPressure(celcius);
        humidity = humidity / 100;  // turns a 100% into 1.00
        vapor_pressure = getVaporPressure(humidity, saturation_vapor_pressure);
        air_pressure = getAirPressure(vapor_pressure, pascals);
        air_density = getAirDensity(air_pressure, vapor_pressure, kelvin);

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