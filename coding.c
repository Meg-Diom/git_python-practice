#include <stdio.h>
#include <math.h>
int main(){
    float a, b, c;
    printf("Enter the coeffitient in x squared: \n");
    scanf("%f", &a);
    printf("Enter the coeffitient in x: \n");
    scanf("%f", &b);
    printf("Enter the coeffitient without x: \n");
    scanf("%f", &c);

    det = b*b - 4*a*c;

    x = (-b + sqrt(det))/(2*a);

    return 0;
}