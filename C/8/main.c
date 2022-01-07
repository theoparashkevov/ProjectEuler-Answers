#include <stdio.h>
#include <math.h>

int isPythagorean(double a, double b, double c);


void main(){
    
    for(double a = 1; a < 1000; a++){
        for(double b = 1; b < 1000; b++ ){
            for(double c = 1; c < 1000; c++ ){
                double sum = a + b + c; 
                
                if( (sum == 1000)&&(isPythagorean(a, b, c))){
                    printf("\n\nA: [%lf]\tB: [%lf]\tC: [%lf]", a, b, c);
                    printf("\nA*B*C = %lf", ((a*b)*c));
                }

            }
        }
    }

    printf("\n");

}

int isPythagorean(double a, double b, double c){

    double a_sqrt = pow(a, 2);
    double b_sqrt = pow(b, 2);
    double c_sqrt = pow(c, 2);

    if(
            ((a_sqrt + b_sqrt) == c_sqrt)
            ||
            ((a_sqrt + c_sqrt) == b_sqrt)
            ||((b_sqrt + c_sqrt) == a_sqrt)
      )
    {
        return 1;
    }

    return 0;
}
