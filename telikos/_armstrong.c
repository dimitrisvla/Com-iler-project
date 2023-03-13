#include <stdio.h>

int main(){
int num, sum, temp, digit, a, b;
int T_1, T_2, T_3, T_4, T_5;
L0: ;
L1: scanf("%d", &num);
L2: temp = num;
L3: if(temp > 0) goto L5;
L4: goto L14;
L5: T_1 = temp / 10;
L6: digit = T_1;
L7: T_2 = digit * digit;
L8: T_3 = T_2 * digit;
L9: T_4 = sum + T_3;
L10: sum = T_4;
L11: T_5 = temp / 10;
L12: temp = T_5;
L13: goto L3;
L14: if(num == 0) goto L16;
L15: goto L18;
L16: printf("%d\n", num);
L17: goto L19;
L18: printf("%d\n", num);
L19: ;
L20: ;
}
