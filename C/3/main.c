#include <stdio.h>

int isPrime(long long unsigned int val);

int main(){

    int lgpn = 1;
    for(long long unsigned int i = 1; i < 600851475143; i++){
        // is it divisable
        if(600851475143 % i == 0)
        {
            // Is it prime
            if(isPrime(i)){
                lgpn = i;
                printf("%d\n", lgpn);
            }
        }
    }

    return lgpn;
}

int isPrime(long long unsigned int val){
    for(int i = 2; i < val; i++){
        if(val % i == 0){
            return 0;
        }
    }

    return 1;
}
