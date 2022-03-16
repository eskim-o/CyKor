#include <stdio.h>

int add(int a, int b)
{
    return a + b;
}

int sub(int a, int b)
{
    return a - b;
}

int main()
{
    int a = 0x2022;
    int b = 0x0314;

    int c = add(a, b);
    int d = sub(a, b);

    return c * d;
}