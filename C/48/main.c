#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define LEN(X)  sizeof(X)/sizeof(X[0])


char *mysum(char * a, char * b);
void initializeToZero(char * a, int _len);
void customCopy(char * dst, char * src);
char * myMultiplication(char * a, int b);
char * myPower(char * a, int b);
int charToInt(char * a);
char * intToChar(int a );

char * reverseString(char * a);

unsigned long long int main(){

    char * tmpPower;
    char * finalSum = "0";

    for(int i = 1; i <= 1000; i++){
        char * numberA = intToChar(i);
        
        // remove zeros START
        int index = strlen(numberA) - 1;
        while(numberA[index] == '0'){
            index--;
        }
        numberA[index + 1] = '\0';
        // remove zeros END
        

        tmpPower = myPower(numberA, i);
        finalSum = mysum(finalSum, tmpPower);
        
        free(tmpPower);

        if(i % 15 != 0){
            printf("[%d]\t", i);
        }else {
            printf("[%d]\n", i);
         }
        //printf("[%d] Sum : %s\n", i,  reverseString(finalSum));
        // printf("Number: [%s] Power: [%d] Result = [%s]\n\n", numberA, i, power);
    }

    printf("\n\n\t\tSolution\n\n\t\t%s\n\n", reverseString(finalSum));
    return 0;
}


void initializeToZero(char * a, int _len){
    for(int i = 0; i < _len; i++){
        a[i] = '0';
    }

    // a[_len] = '\0';
}

void customCopy(char * dst, char * src){
    int i = 0;
    while(src[i] != '\0'){
        dst[i] = src[i];

        i++;
    }
}

char * mysum(char * a, char * b){
    char * _a = a;
    char * _b = b;

    int _lenA = strlen(_a);
    int _lenB = strlen(_b);

    int freeA = 0;
    int freeB = 0;

    //printf("[Before]\t\tlength of A [%d]->[%s]\tlength of B [%d]->[%s]\n", _lenA, _a, _lenB, _b);

    unsigned long long int loopLength = 0;

    if (_lenA > _lenB){
        // extend b
        _b = (char *) malloc((_lenA + 1) * sizeof(char) );
        initializeToZero(_b, _lenA);
        customCopy(_b, b);

        freeB = 1;
        freeA = 0;

        loopLength = _lenA;
    }
    else if (_lenB > _lenA) {
        // extend a
        _a = (char *) malloc((_lenB + 1)* sizeof(char));
        initializeToZero(_a, _lenB);
        customCopy(_a, a);

        freeA = 1;
        freeB = 0;

        loopLength = _lenB;
    }
    else{
        loopLength = _lenA;
    }

    loopLength += 2;
    //printf("[After]\t\t\tlength of A [%d]->[%s]\tlength of B [%d]->[%s]\n", strlen(_a), _a, strlen(_b), _b);

    char *sum = (char*) malloc(loopLength * sizeof(char));
    initializeToZero(sum, loopLength);

    //printf("Initialized SUM [%s]\n", sum);
    //bitwise sumation
    int carry = 0 ;
    for(int i = 0; i< loopLength - 1; i++){
        if(_a[i] != '\0' && _b[i] != '\0'){
            int tmpResult = (_a[i] - 48 ) + (_b[i] - 48) + carry;
            int positionalResult = tmpResult % 10;

            sum[i] = positionalResult + 48;
    
            if(tmpResult >= 10 ){
                carry = 1;
            }
            else{
                carry = 0;
            }
        }
        else{
            sum[i] = carry + 48;
        }
    }

    sum[loopLength - 1] = '\0'; 
    
    // remove zeros START
    int index = loopLength - 2;
    while(sum[index] == '0'){
        index--;
    }
    // remove zeros END
    sum[index + 1] = '\0';

    if(freeA){
        free(_a);
    }
    else if(freeB){
        free(_b);
    }



    //printf("\t\t[%s] + [%s] = [%s] \n", a, b, sum);
    return sum; 

}

char * myMultiplication(char * a, int b){
    // printf("\n\n[%s] * [%d] \n", a, b);

    char * mult;
    char * _tmp;

    mult = (char *) malloc((strlen(a) + 1) * sizeof(char));
    strcpy(mult, a);
    
    for (int i = 1; i < b; i++) {
        
        _tmp = mysum(mult, a);
        free(mult);
        mult = _tmp;

    }

    return mult;

}

char * myPower(char * a, int b){

    char * power = a;
    int mult = charToInt(a);

    for (int i = 1; i < b; i++) {
        
        power = myMultiplication(power, mult);
    }

    return power;

}

int charToInt(char * a){
    int _len = strlen(a);
    
    int result = 0;
    int _base  = 1;

    for(int i = 1; i<_len; i++){
        _base *= 10;
    }

    for (int i = _len - 1;  i >= 0; i--) {
        
        result += (a[i] - 48) * _base;
        // printf("Base [%d] Current Char [%c] Result = [%d]\n", _base, a[i], result);
        
        _base /= 10;
    }

    return result;

}
char * intToChar(int a ){

    char * result = (char *) malloc(sizeof(char) * 5);

    int divisor = 10;

    for(int i = 0; i < 4; i ++){
        result[i] = (a % divisor)/(divisor/10) + 48;

        divisor *= 10;
    }

    result[4] = '\0';

    return result;

}


char * reverseString(char * a){
    char * result = (char *) malloc((strlen(a) * sizeof(char)) + 1);
    int index = 0;

    for (int i = strlen(a) - 1; i >= 0 ; i--) {
        result[index] = a[i];
        index++;
    }

    result[index] = '\0';

    return result;
}


































