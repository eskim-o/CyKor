#include <stdio.h>

int main(){
    int a, b, c;
    a = 1; b = 2; c = 3;
    // %d는 3개인데 인자는 두개라면?
    printf("%d %d %d\n", a, b);
    // 극단적으로 인자 없이 %x만 잔뜩 넣어보자
    printf("%x %x %x %x\n %x %x %x %x\n");
    return 0;
}