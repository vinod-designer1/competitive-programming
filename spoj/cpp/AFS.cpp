#include <iostream>
#include <bitset>
#include <math.h>       /* pow */
#include <algorithm>    // std::fill_n

#define SIZE 1000000
#define MAX (int)(SIZE-3)/2
using namespace std;
 
int primes[MAX+1];
long long int a[SIZE] = {0};
bool prm_lst[SIZE];                                              //array that stores the primes up to sqrt(SIZE)
bitset<MAX+1> bset;                                                  //auxiliary bitset used to make the sieve
 
void setPrimes()
{
    int i,j;

    std::fill_n(prm_lst, SIZE, false);

    for(i=0;i*i<=SIZE;i++)                                           //we only have to get primes up to sqrt(SIZE)
        if(!bset.test(i))
             for(j=i+1;(2*j+1)*(2*i+3)<=SIZE;j++)
                  bset.set(((2*j+1)*(2*i+3)-3)/2);                   //setting all non-primes
    primes[0]=2;                                                     //store the first prime (that is 2)
    for(i=1,j=0;j<MAX+1;j++)
       if(!bset.test(j))
          primes[i++]=2*j+3;                                   //store the remaining odd primes
    
    for(i=0;i<=MAX;i++) {
    	if (primes[i] > 1){
    		prm_lst[primes[i]] = true;
    	}
    }
}

long long int factSum(int n)
{
	int i = 0, N = n, limit = pow(n, 0.5) + 1, pow_d = 0;

	long long int sum_p = 1;

	if (prm_lst[n])
		return 1;

	while (primes[i] <= limit)
	{
        pow_d = 0;

        while (n%primes[i] == 0)
        {
            n /= primes[i];
            pow_d += 1;
        }

        if (pow_d > 0)
            sum_p *= ((pow(primes[i],(pow_d+1)) - 1)/(primes[i]-1));

        i++;
    }

    return (sum_p - N);
}

long long int seqVal(int n)
{   
	if (n <= 1) return 0;

    if (n > 1 and a[n] != 0)
        return a[n];

    a[n] = (seqVal(n-1) + factSum(n));

    return a[n];
}

int main(int argc, char const *argv[])
{
	int t, num, i;
    
	setPrimes();

	std::cin >> t;
	for (i=0;i<t;i++)
	{
		std:cin >> num;
		std::cout << seqVal(num);
	}
	return 0;
}