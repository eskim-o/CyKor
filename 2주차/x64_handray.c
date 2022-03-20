#include <stdio.h>

int main()
{
    setup();
    while (1)
    {
        int a = 0;
        int b = 0;
        int c = 0;

        int sum[11];

        for (int i = 10; i > 0; i--)
        {
            sum[i] = 0;
        }

        printf("Input: ");

        if (scanf("%ld %ld %ld", &a, &b, &c) == 3)
        {
            b = b + a;
            sum[c] = b;
            printf("Result: %ld", sum[7]);
        }
        else
        {
            break;
        }
    }
}