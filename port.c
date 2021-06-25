#include <stdio.h>

#define UNIVERSAL_GAS_CONSTANT = 8.312 // J/(K*mol)
#define AIR_MOLAR_MASS = 0.0289654 // kg/mol
#define VAPOR_MOLAR_MASS = 0.018016 // kg/mol

int main(){
    int running = 1;

    while (running > 0){
        // put statements and queries for user here
        puts("Do you want to reset the loop?\ny/n");
        char reset[1];
        gets(reset);
        if (*reset > 120){// can use ascii values to compart chars
            running = 1;
        }
        else {
            running = 0;
        }
    }
    puts("I'm out");

    return 0;
}