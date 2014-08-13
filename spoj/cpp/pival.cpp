//http://stackoverflow.com/questions/20287513/can-anyone-make-heads-or-tales-of-this-spigot-algorithm-code-pitiny-c
//http://www.pi314.net/eng/goutte.php
#include<iostream>
using namespace std;

void piv() {
    long a[35014];
    long b = 0;
    long c = 35000;
    long d = 0;
    long e = 0;
    long f = 10000;
    long g = 0;
    long h = 0;
    long i = 0;

    while (c) {
        d %= f;
        e  = d;
        b  = c-1;
        g  = b*2;

        while(g) {
            g -= 1;
            i  = h ? a[b] : f/5;
            d  = (d*b) + (f*i);
            a[b] = d % g;
            d /= g;
            b -= 1;
            g  = b*2;
        }

        printf("%04ld", e+d/f);
        h  = 1;
        c -= 14;
    }
}

int main()
{
	piv();
	return 0;
}