/***************************************************************
********** 1.1  **********
Q. a+b can be less than min(a,b)
S. If a < 0 and b < 0 
      then a+b < min(a,b)
********** 1.1E **********

********** 1.2  **********
Q. a*b can be less than min(a,b)
S. If a < 0 or b < 0
      then a*b < min (a, b)
********** 1.2E **********

********** 1.3 & 1.4  **********
Q. Design road network such that fastest distance is not shortest distance
S.    _____________________
     |                     |
     a              b______|
     |__   _   _   _|
        |_| |_| |_|  
********** 1.3E & 1.4 **********

********** 1.5  **********
Q. Knapsack Problem Solutions Counter Examples
S. (a) Example S = {1, 2, 5, 9, 10}, T = 6 even though 
       exact solution exists it leave with partial solution
       sol_by_this = {1, 2}
       act_sol = {1,5}
   (b) Same example as above.
   (c) S = {1, 2, 5, 9, 11}, T = 15
       sol_by_this = {11, 2, 1}
       act_sol = {9,5,2}

********** 1.5E **********

********** 1.6 **********
Q. set cover algorithm
S. Counter Example For Method:
   U = {1, 2, 3, 4, 5, 6, 7, 8}
   S1 = {1, 2, 5, 6}
   S2 = {1, 2, 7}
   S3 = {3, 6, 4}
   S4 = {8, 5}
   sol_by_algo = {S1, S3, S4, S2}
   act_sol = {S2, S3, S4}
********** 1.6E **********

********** 1.7 ***********
c >= 2
function multiply(y, z)
    if z = 0 then return 0
    else
       return (multiply(cy, |_z/c_|) + y * (z mod c))

z = c*q + r => r = z mod c and q = |_z/c_|
y*z = c*y * (z/c) = c*y * (|_z/c_|+(z mod c)/c)
=> cy * |_z/c_| +  y * (z mod c) for all c > 0
********** 1.7E **********

********** 1.8 ***********
p(x) = an * (x**n) + an-1 * (x**n-1)+ ... + a0
== (((an*x + an-1)*x + an-2)*x)+...)*x + a0
********** 1.8E **********

********** 1.9 ***********
function bubblesort(A:list[1..n])
    var int i, j
    for i from n to 1
       for j from 1 to i-1
            if (A[j] > A[j+1]) // making sure that large
                swap A[j], A[j+1] // number is right to current  
-> Every time the maximum element if pushed to end
   as we are swapping any large number found to adjacent cell
   in every itertion of j -> 1 to i-1
-> we are making n pass from i -> n to 1 which will place largest elemnet
   from 1 to i at ith position
==> array is sorted after n iterations
********** 1.9E **********

********** 1.19 **********
assumming our school teaches for 1-10
assume for classes for start
20,30,....,110
no_pages for each book on avg
50, 150, 150, 200, 200, 250, 300, 350, 400, 400, 500
total
1000, 4500, 6000, 10000, 12000, 17500,
24000, 31500, 40000, 44000, 60000 
total =  250500
********** 1.19E *********

@TODO ESTIMATION PAGE : 29

********** 1.26 **********
********** 1.26E *********
****************************************************************/

/********** 1.28 **********/
int divide(int num, int den)
{
	count = 0;
	while (num >= den)
	{
		count++;
		num -= den;
	}

	return count;
}
/********** 1.28E *********/

/********** 1.29 **********
deal with no 1 algo:
1 2 3 4 5
1 6 7 8 9 // 1 (6 7 2 3)
1 10 11 12 13 // 1 (10 11 6 7 2 3)
3 10 11 6 7 // (10 11 2)
1 14 15 16 17 // 1 (14 15)
10 11 2 14 15 // (2 10)
1 18 19 20 21 // (18 19)
23 24 25 2 10 // (23 24)
1 24 23 18 19

brute force:
1 2 3 4 5  //1 2 3
6 7 8 9 10 // 6 7 8
11 12 13 14 15 // 11 12 13
16 17 18 19 20 // 16 17 18
21 22 23 24 25 // 21 22 23
1 2 3 6 7 // 1 2 3
8 11 12 13 16 // 8 11 12
17 18 21 22 23 // 17 18 21
1 2 3 8 11 // 1 2 3
12 17 18 21 1 // 1 17 18
17 18 2 3 // 17 18
********************/
int minimum_races(int horses, int no_horses_per_race)
{

}
/********** 1.29E *********/