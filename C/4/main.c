#include <stdio.h>

int isPolindrome(int); 

int main(){

    int maxPolindrom, _i, _j = 0;

    for(int i = 999; i > 101; i--){
        for(int j = 999; j > 101; j--){
            int polindrome = isPolindrome(i*j);
            
            if(polindrome && (i*j > maxPolindrom)){
                
                maxPolindrom = i*j;
                _i = i;
                _j = j;
            }
        }
    }
    printf("[True]-->[%d] * [%d] = [%d]\n", _i, _j, maxPolindrom);

    return 0;

}

int isPolindrome(int a){

    int _baseR = 10;
    int _baseRtmp = 1;
    int _baseL = 100000;

    for(int i = 1; i <=6; i++ ){

        int resultR = ((a % _baseR ) - (a % (_baseR / 10) ) ) / _baseRtmp ;
        int resultL = (a / _baseL ) % 10;

        //printf("L[%d] \t R[%d]\n", resultL, resultR);
        
        if(resultR != resultL){
            return 0;
        }
        else{
            _baseL /= 10;
            _baseR *= 10;
            _baseRtmp *= 10;
        }
    }

    return 1;
}
