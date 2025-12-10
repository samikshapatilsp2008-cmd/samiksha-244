#include<stdio.h>
#define PI 3.14

int main() {
    int choice;
    float r,l,b,h,side,area;

    printf("Choose shape to Find Area:\n");
    printf("1.Circle\n2.Rectangle\n3.Triangle\n4.Square\n");
    scanf("%d",&choice);
    switch(choice) {
        case1:
        printf("Enter radius: ");
        scanf("%f",&r);
        area=PI*r*r;
        printf("Area of circle=%.2f\n",area);
        break;
        case2:
        printf("Enter length and breadth:");
        scanf("%f%f",&l,&b);
        area=l*b;
        printf("Area of Rectangle=%2f\n",area);
        break;
        case 3:
        printf("Enter base and height:");
        scanf("%f",&side);
        area=side*side;
        printf("Area of Square=%.2f\n",area);
        break;
        default:
        printf("Invalid Choice!\n");
    }
    return 0;
}