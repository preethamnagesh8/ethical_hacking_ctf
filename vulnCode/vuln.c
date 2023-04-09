#include <stdio.h>
#include <string.h>

void vuln_function(char *input);

int main(int argc, char *argv[]){
        if (argc == 2){
                vuln_function(argv[1]);
        } else {
                printf("This program accepts only one argument");
        }
}

void vuln_function(char *input){
        char buffer[100];
        strcpy(buffer, input);
        printf("Successfully Completed Execution");
}