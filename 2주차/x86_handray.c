#include <stdio.h>

int main()
{
    int a = 0x4030201;
    int str;
    fgets(str, 45, stdin);
    printf("\n[buf]: %s\n", str);
    printf("[check] %p\n", a);
    if (a!=0x4030201)
    {
        if (a!=0xdeadbeef)
        {
            puts("\nYou are on the right way!");
        }
    }
    if (a==0xdeadbeef)
    {
        puts("Yeah dude! You win!\nOpening your shell...");
        system("/bin/dash");
        puts("Shell closed! Bye.");
    }
    
    return 0;
}