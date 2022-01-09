#include <stdio.h>

int isPrime(long int a);

long int UPPER_LIMIT = 2000000;

void main(){

    long long unsigned int _sum = 2; // start from 2 
    for(long int i = 3; i < UPPER_LIMIT; i++){
        if(isPrime(i)){
            _sum += i;
        }

        if((i % 100000) == 0){
            printf("\n %ld => [ %ld ]\n",i, _sum);
        }

    }

    printf("\n Sum of all primes bellow %ld is => [ %ld ]\n",UPPER_LIMIT, _sum);

}

int isPrime(long int a){

    for(long int i = 2; i < a; i++){

        if((a % i) == 0){
            return 0;
        }

    }

    return 1;
}
