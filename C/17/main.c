#include <stdio.h>

int main(){

    int _digits[] = {0, 3, 3, 5, 4, 4, 3, 5, 5, 4};
    int _teens[]  = {3, 6, 6, 8, 8, 7, 7, 9, 8, 8}; // including 10
    int _tens[] = {6, 6, 5, 5, 5, 7, 6, 6};
    int _hundreds[] = { 7 + _digits[1], 7 + _digits[2],
                        7 + _digits[3], 7 + _digits[4],
                        7 + _digits[5], 7 + _digits[6],
                        7 + _digits[7], 7 + _digits[8],
                        7 + _digits[9]};

    int _sum_digits = 0;
    int _sum_teens = 0;

    for(int i = 0; i < 10; i++){
        _sum_digits += _digits[i];
    }

    for(int i = 0; i < 10; i++){
        _sum_teens += _teens[i];
    }

    int _and = 3;
    int _one_thousand = 11;

    int sum = 0;

    for(int i = 999; i > 0; i--){
        int _hundreds_current = i / 100;
        int _tens_current = (i % 100) / 10;
        int _digits_current = (i % 10) % 10;

        printf("[%d]\tHundreds %d \t Tens %d \t Digits %d \t \
                Sum %d \n", i, _hundreds_current, _tens_current, _digits_current, sum);

        if(_hundreds_current){
            // is it pure hundred or something else
            if((i % 100) != 0){
                sum += _hundreds[(i/100) - 1];
                sum += _and;
                int _hundread_tens_current = i % 100; //99

                // printf("\t %d \n", sum);
                if(_hundread_tens_current > 19){
                    if(_hundread_tens_current % 10 == 0){
                        sum += _tens[(_hundread_tens_current / 10) - 2];
                    }else{
                        sum += _tens[(_hundread_tens_current / 10) - 2];
                        //printf("\t\t %d\n", sum);
                        sum += _digits[(_hundread_tens_current % 10)];
                    }

                }else if (_hundread_tens_current >= 10 && _hundread_tens_current <= 19 ){
                    // teen
                    sum += _teens[(_hundread_tens_current % 10)];
                }
                else if (_hundread_tens_current < 10){
                    // I am less than 10
                    sum += _digits[_hundread_tens_current];
                }

            }else{
                // Pure hundread
                sum += _hundreds[(i / 100) - 1];
            }
            continue;
        }
        else if (_tens_current){
            // is it teen or something else
            if(i > 19){
                sum += _tens[(i / 10) - 2];
                sum += _digits[(i % 10)];

            }else if (i > 10 && i <= 19){
                // teen
                sum += _teens[(i % 10)];
            }
            else{
                // I am 10
                sum += _teens[0];
            }
            continue;
        }else{
            // I am less than 10 or equal to 10
            if(i != 10){
                sum += _digits[i];
            }else{
                // I am 10
                sum += _teens[0];
            }
            continue;
        }
    }

    sum += _one_thousand;

    //printf("[%d] = Sum[%d] + Teens[%d] + Digits[%d]\n", sum + _sum_digits + _sum_teens, sum, _sum_teens, _sum_digits);
    //printf("Digits Sum [%d] Teens Sum (including 10) [%d]\n", _sum_digits, _sum_teens);
    printf("[%d]\n", sum);
    return 0;
}
