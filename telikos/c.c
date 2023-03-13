#include <stdio.h>

int main(){
int a, b;
int T_1;
L0: ;
L1: scanf("%d", &b);
L2: scanf("%d", &a);
L3: if(a > b) goto L5;
L4: goto L8;
L5: T_1 = a - 2;
L6: a = T_1;
L7: goto L3;
L8: printf("%d\n", a);
L9: ;
L10: ;
}
