// gcc AAR.c -o AAR
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void init(){
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

int main() {
    char fmt[0x50];
    int key = 0;
    int input = 0;

    init();
    srand(time(NULL));
    key = rand();

    printf("fmt : ");
    scanf("%80[^\n]", fmt);
    printf(fmt);

    printf("key : ");
    scanf("%d", &input);
    
    if (key == input)
        system("/bin/sh");
    else
        puts("wrong key :(");

    return 0;
}