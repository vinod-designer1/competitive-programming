#ifdef ssu1
#define _GLIBCXX_DEBUG
#endif
#undef NDEBUG

#include <algorithm>
#include <functional>
#include <numeric>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <bitset>
#include <sstream>

using namespace std;

#define fore(i, l, r) for(int i = (l); i < (r); ++i)
#define forn(i, n) fore(i, 0, n)
#define fori(i, l, r) fore(i, l, (r) + 1)
#define sz(v) int((v).size())
#define all(v) (v).begin(), (v).end()
#define pb push_back
#define mp make_pair
#define X first
#define Y second

typedef long long li;
typedef long double ld;
typedef pair<int, int> pt;

template<typename T> T abs(T a) { return a < 0 ? -a : a; }
template<typename T> T sqr(T a) { return a*a; }

const int INF = (int)1e9;
const ld EPS = 1e-9;
const ld PI = 3.1415926535897932384626433832795;

/*

    This is just to check correctness of input

*/
int readInt(int l, int r){
    int x;
    if(scanf("%d", &x) != 1){
        fprintf(stderr, "Expected int in range [%d, %d], but haven't found!", l, r);
        throw;
    }
    if(!(l <= x && x <= r)){
        fprintf(stderr, "Expected int in range [%d, %d], but found %d!", l, r, x);
        throw;
    }
    return x;
}
int readInt(int l, int r, string name){
    int x;
    if(scanf("%d", &x) != 1){
        fprintf(stderr, "Expected int %s in range [%d, %d], but haven't found!", name.c_str(), l, r);
        throw;
    }
    if(!(l <= x && x <= r)){
        fprintf(stderr, "Expected int %s in range [%d, %d], but found %d!", name.c_str(), l, r, x);
        throw;
    }
    return x;
}
li readLong(li l, li r){
    li x;
    if(scanf("%lld", &x) != 1){
        fprintf(stderr, "Expected long long in range [%lld, %lld], but haven't found!", l, r);
        throw;
    }
    if(!(l <= x && x <= r)){
        fprintf(stderr, "Expected long long in range [%lld, %lld], but found %lld!", l, r, x);
        throw;
    }
    return x;
}
li readLong(li l, li r, string name){
    li x;
    if(scanf("%lld", &x) != 1){
        fprintf(stderr, "Expected long long %s in range [%lld, %lld], but haven't found!", name.c_str(), l, r);
        throw;
    }
    if(!(l <= x && x <= r)){
        fprintf(stderr, "Expected long long %s in range [%lld, %lld], but found %lld!", name.c_str(), l, r, x);
        throw;
    }
    return x;
}
const ld __EPS__ = 1e-15;
ld readDouble(double l, double r){
    double x;
    if(scanf("%lf", &x) != 1){
        fprintf(stderr, "Expected double in range [%lf, %lf], but haven't found!", l, r);
        throw;
    }
    if(!(l <= x + __EPS__ && x <= r + __EPS__)){
        fprintf(stderr, "Expected double in range [%lf, %lf], but found %lf!", l, r, x);
        throw;
    }
    return x;
}
ld readDouble(double l, double r, string name){
    double x;
    if(scanf("%lf", &x) != 1){
        fprintf(stderr, "Expected double %s in range [%lf, %lf], but haven't found!", name.c_str(), l, r);
        throw;
    }
    if(!(l <= x + __EPS__ && x <= r + __EPS__)){
        fprintf(stderr, "Expected double %s in range [%lf, %lf], but found %lf!", name.c_str(), l, r, x);
        throw;
    }
    return x;
}

int main(){
#ifdef ssu1
    assert(freopen("input.txt", "rt", stdin));
    //assert(freopen("output.txt", "wt", stdout));
#endif

    int type = -1;

    int t;
    t = readInt(1, 1000, "t");
    forn(i, t){
        int k, r;
        r = readInt(1, 2000000000, "r");
        k = readInt(0, 2000000000, "k");

        if(type == 0)
            assert(r == 1 && k == 0);
        else if(type == 1)
            assert(r == 2000000000);
        else if(type == 2)
            assert(k == 2000000000);
        else if(type == 3)
            assert(r == 2000000000 && k == r);

        int sq = 0;
        while(sq * sq < r)
            sq++;
        li ans = 0;
        fori(y, -sq, sq){
            int x = max(sqrtl(r - y * y) - 10, ld(0));
            while(x * x + y * y < r)
                x++;
            if(x * x + y * y == r)
                ans += (x == 0 ? 1 : 2);
        }

        if(type == 4)
            assert(ans == k);

        if(ans <= k)
            puts("possible");
        else
            puts("impossible");
    }
    return 0;
}