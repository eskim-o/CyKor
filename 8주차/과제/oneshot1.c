// gcc oneshot1.c -o oneshot1 -no-pie
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void gift() {
    system("gift");
}

int main() {
    char buf[0x100];

    printf("Look, if you had one shot, one opportunity\n");
    printf("To seize everything you ever wanted, in one moment\n");
    printf("Would you capture it or just let it slip? ♩♪\n\n");
    
    read(STDIN_FILENO, buf, sizeof(buf));
    printf(buf);
    exit(0);
}