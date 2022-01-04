#include <stdio.h>


void main(void)
{
    int _flag = 1;
    long long int _result = 2;

    while(_flag){
        for(int i = 1; i <= 20; i++){
            //printf("\n [%d]", i); 
            
            if((_result % i) == 0){
                _flag = 0;
            }
            else{
                _flag = 1;
                printf("NO: [%d] Divisor [%d] => [%d]\n", _result, i, (_result % i));
                break;
            }
            
        }

        _result += 2;
    }

    printf("\n[ %d ]\n\n", (_result - 2 ));
    
}
