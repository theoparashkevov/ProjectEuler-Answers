#include <stdio.h>

int isPrime(long long int a);

void main(){

    int _loop_ub = 10010;

    int prime_count = 2;
    long long int _current_number = 3;
    long long int _result = 0;

    while(prime_count <= _loop_ub){

        if(isPrime(_current_number)){
            if(prime_count == 10001){
                printf("\n The [%lld]-th Prime Number is: %lld",
                        prime_count, _current_number);
            }
            prime_count++;
        }

        _current_number++;

    }

    _result = _current_number - 1;

    printf("\n Result: %lld\n\n", _result);
}

int isPrime(long long int a){
    for(long long int i = 2; i < a; i++){
        
        if((a % i) == 0){
            return 0;
        }
    }

    return 1;
}

