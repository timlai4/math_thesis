#include <stdio.h>
#define MAX 100000

int a[MAX],b[MAX];
int mod;
int phi = 0;

int gcd(int x, int y)
{
        if (x < y)
                return gcd(y,x);
        if (y==0)
                return x;
        return gcd(y, x%y);
}

void group(void)
{
        int i;
        for (i=0; i < mod; i++)
                if (gcd(mod,i)>1)
                        a[i] = b[i] = 0;
                else{
                        phi++;
                        a[i] = b[i] = 1;
                }
}

int addgen(int k)
{
        int i,count;
        //printf("addgen(%d): %d, %d\n",k,a[k],b[k]);
        if (a[k] == 0 || b[k] == 0)
                return 0;
        printf(" %d",k);
        for(;;){
                count = 0;
                for (i=0; i < mod; i++)
                        if (b[i] == 0 && b[(i*k)%mod] == 1){
                                count++;
                                phi--;
                                b[(i*k)%mod] = 0;
                        }
                if (count == 0)
                        break;
        }
        return count;
}

void run(void)
{
        int i;
        for (i=2; phi > 0; i++)
                addgen(i);
        printf("\n");
}

int main(void)
{
        printf("mod: ");
        scanf("%d",&mod);
        group();
        b[1] = 0;
        phi--;
        run();
}
