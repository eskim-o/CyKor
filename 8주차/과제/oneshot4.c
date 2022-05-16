// gcc oneshot4.c -o oneshot4 -no-pie
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char buf[0x100];

void init(){
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
}

int main() {  
    init();

    printf("Look, if you had one shot, one opportunity\n");
    printf("To seize everything you ever wanted, in one moment\n");
    printf("Would you capture it or just let it slip? ♩♪\n\n");
    
    read(STDIN_FILENO, buf, sizeof(buf));
    printf(buf);
 
    return 0;
}