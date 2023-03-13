#include <stdio.h>

int main(){
int x, count;
int T_1, T_2;
L0: ;
L1: scanf("%d", &x);
L2: count = 0;
L3: if(x > 0) goto L5;
L4: goto L10;
L5: T_1 = x / 10;
L6: x = T_1;
L7: T_2 = count + 1;
L8: count = T_2;
L9: goto L3;
L10: printf("%d\n", count);
L11: ;
L12: ;
}
