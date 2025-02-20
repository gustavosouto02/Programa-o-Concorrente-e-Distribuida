#include <stdio.h>

int main( ){
    int n = 11;
    int NumDivisores = 0;

    for(int i = 1; i <= n; i++)
        if (n % i == 0)
            NumDivisores++;

    printf("%d", NumDivisores);

    return 0;
}