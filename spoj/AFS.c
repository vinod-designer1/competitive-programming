#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstring>
using namespace std;
#define MAX 1000001

long long int ar[MAX];
long long int nPrime[MAX];
long long int counted = 2;

void primesupto(long long int upperBound) {
      int i = 0;
      long long int upperBoundSquareRoot = (long)sqrt((double)upperBound);
      bool *isComposite = new bool[upperBound + 1];
      memset(isComposite, 0, sizeof(bool) * (upperBound + 1));
      for (long m = 2; m <= upperBoundSquareRoot; m++) {
            if (nPrime[m] == 0)
                nPrime[m] = 1;
            
            if (!isComposite[m]) {
                  for (int k = 2*m; k <= upperBound; k += m){
                        isComposite[k] = true;
                        if (nPrime[k] == 0)
                            nPrime[k] = 1;
                        int c = m;
                        while (k%c == 0) {
                            c *= m;
                        }
                        
                        
                        nPrime[k] *= ((c-1)/(m-1));
                        
                  }
            }
           
      }
      
      for (long m = upperBoundSquareRoot; m <= upperBound; m++)
            if (!isComposite[m])
            {
                nPrime[m] = 1;
                for (int k = 2*m; k <= upperBound; k += m){
                        isComposite[k] = true;
                        if (nPrime[k] == 0)
                            nPrime[k] = 1;
                        int c = m;
                        while (k%c == 0) {
                            c *= m;
                        }
                        
                        
                        nPrime[k] *= ((c-1)/(m-1));
                        
                }
            }
      delete [] isComposite;
}

long long int seqV(long long int v) 
{
   
   int i = 0;
   while (counted <= v) {
       if (ar[counted] == 0){
           int val = nPrime[counted];
           if (val != 1) 
               val -= counted;
           ar[counted] = ar[counted-1] + (val);       
       }
       
       counted += 1;
   }
}

int main() {
	// your code goes here
	primesupto(MAX);
	
	long int t, v;
	cin >> t;
	
	while (t-- > 0) {
	  cin >> v;
	  seqV(v);
	  cout << ar[v] << endl << endl;
	}
	
	return 0;
}