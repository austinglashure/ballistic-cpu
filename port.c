#include <stdio.h>
#include <math.h>
#include <stdbool.h>

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

float getCrossSectionalArea(float cal){
    float pi = 3.1415926;
    float radius = cal / 2;
    return pi * pow(radius, 2);
}

float getDragCoefficient(float air_dens, float bc, float csa){
    return 0.5 * air_dens * bc * csa;
}

float getDragForce(float drag_coef, float vel_zero){
    return drag_coef * vel_zero * vel_zero;
}

float getInstantDecel(float drag_force, float mass){
    return -1 * drag_force / mass;
}

float getAverageDecel(float vel_zero, float vel_f){
    return (vel_zero + vel_f) / 2;
}

struct Gun {
    float bc;
    float caliber;
    float mass;
    float muzzle_velocity;
    float cross_sectional_area;
};

int main(){
    bool getting_weather = true;
    int reset = 1;

// 'profile' for my .308
    struct Gun a;
    a.bc = 0.45;
    a.caliber = 0.0078232; // in meters .308in
    a.mass = 0.01069182; // in kilograms 165 grains
    a.muzzle_velocity = 860; // in meters/sec 2821 fps
    a.cross_sectional_area = getCrossSectionalArea(a.caliber); // m^2

// drag variable
    float drag_coefficient;

// weather variables loop
    while (getting_weather){
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
        scanf(" %f", &inHg);
        // do pressure conversions
        pascals = toPascal(inHg);
        hectopascals = toHectoPascal(pascals);
        // air density variable instanciations
        float saturation_vapor_pressure, humidity;
        float vapor_pressure, air_pressure, air_density;
        // query user for humidity
        printf("What is the humidity? 0-100\n");
        scanf(" %f", &humidity);
        // air density calculations
        saturation_vapor_pressure = getSaturationVaporPressure(celcius);
        humidity = humidity / 100;  // turns a 100% into 1.00
        vapor_pressure = getVaporPressure(humidity, saturation_vapor_pressure);
        air_pressure = getAirPressure(vapor_pressure, pascals);
        air_density = getAirDensity(air_pressure, vapor_pressure, kelvin);
        drag_coefficient = getDragCoefficient(air_density, a.bc, a.cross_sectional_area);

        printf("Do you wish to change any of these variables? 1/0\n");
        scanf("%d", &reset);
        if (reset > 0){// can use ascii values to compare chars
            getting_weather = true;
        }
        else {
            getting_weather = false;
        }
    }

// ballistics loop
    bool new_target = true;
    while (new_target){
        // ballistics variables
        float range, vel0, velF, decel, instant_decel, force_drag, avg_vel;
        printf("What is the target's range?\n");
        scanf("%f\n", &range);
        float distance_travelled = 0;
        // flight time calculation loop
        vel0 = a.muzzle_velocity;
        while (distance_travelled < range){
            force_drag = getDragForce(drag_coefficient, vel0);
            instant_decel = getInstantDecel(force_drag, a.mass);
            decel = instant_decel * TIME_IMPULSE;
            velF = vel0 + decel;
            avg_vel = getAverageDecel(vel0, velF);
            



        }
    }
    puts("I'm out");

    return 0;
}