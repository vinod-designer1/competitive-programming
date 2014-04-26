#include <stdio.h>

long cycleLength(long x) {
      long count = 1;
      while (x != 1) {
           if (x%2 == 0) {
                x = x/2;
           } else {
                x = 3*x + 1;
           }
           count++;
      }
      return count;
}

long maxCycleLength(long x, long y) {
       long max = 0;
       long i = 0;
       long cl;
       long temp;

       if (x > y) {
          temp = x;
          x = y;
          y = temp;
       }

       for (i = x; i <= y; i++) {
            cl = cycleLength(i);
            if (cl > max) max = cl;
       }
       return max;
}

int main() {
    long x,y,z;
    while(scanf("%lu %lu", &x, &y) == 2) {
          z = maxCycleLength(x, y);
          printf("%lu %lu %lu\n", x, y, z);
    }

    return(0);
}