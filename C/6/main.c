#include <stdio.h>
#define LIMIT 100


int power(int _base, int _power);



int main(int argc, char* argv[])
{
    long long int _square_of_sum = 0;
    for(int i = 1; i <= LIMIT; i++){
        _square_of_sum += i;
    }

    printf("\nSquare sum:     [%lld]\n", _square_of_sum);
    _square_of_sum = power(_square_of_sum, 2);
    printf("\nSquare sum ^ 2: [%lld]\n", _square_of_sum);


    long long int _sum_of_squares = 0;
    for(int j = 1; j <= LIMIT; j++){
        _sum_of_squares += power(j, 2);
    }

    printf("\nSum of Squares: [%lld]\n", _sum_of_squares);

    long long int _difference = _square_of_sum - _sum_of_squares;
    printf("\n\nDiff: [ %lld ]\n\n", _difference);

    return 0;
}

int power(int _base, int _power){

    long long int _result = 1;
    for(int i = 1; i <= _power; i++){
        _result *= _base;
    }

    return _result;
}


