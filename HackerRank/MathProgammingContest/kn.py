#https://www.hackerrank.com/contests/infinitum-mar14/challenges/summing-the-k-n-series
# Approch:
# ∑x^n(1:k) = (x^k+1 - x)/(x - 1) 
# sn = 1^n+2^n+...+n^n
# ∑sn(1:n) = (1^1+2^1+..+n^1) + (1^2+2^2+..+n^2) + ... +(1^n+2^n+...+n^n)
# adding column wise
# ∑sn(1:k) = (1^1+1^2+..+1^k) + (2^1+2^2+..+2^k) + ... +(n^1+n^2+...n^k) 
# ∑sn(1:k) = k + (2^k+1 - 2)/1 + (3^k+1 - 3)/2 + .... + (n^k+1 - n)/n-1
# sk = ∑s(1:k) - ∑s(1:k-1) = 1+ (2^k+1 - 2^k)/1 + (3^k+1 - 3^k)/2 +...+ (n^k+1 - n^k)/n-1   
# sk =  1 + 2^k + 3^k + ... + n^k
# http://math.stackexchange.com/questions/326663/how-to-calculate-1k2k3k-cdotsnk-with-given-values-of-n-and-k