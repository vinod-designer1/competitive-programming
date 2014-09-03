#include <cstdio>
#include <cassert>
using namespace std;


int mutation_table[4][4] = 
{
	{0, 1, 2, 3},
	{1, 0, 3, 2},
	{2, 3, 0, 1},
	{3, 2, 1, 0}
};
typedef unsigned char byte;
const int MAXN = 1e6;
byte S[2][MAXN];
int reverse_bits(int x) {
    x = ((x & 0xaaaaaaaa) >> 1) | ((x & 0x55555555) << 1);
    x = ((x & 0xcccccccc) >> 2) | ((x & 0x33333333) << 2);
    x = ((x & 0xf0f0f0f0) >> 4) | ((x & 0x0f0f0f0f) << 4);
    x = ((x & 0xff00ff00) >> 8) | ((x & 0x00ff00ff) << 8);
    x = ((x & 0xffff0000) >> 16) | ((x & 0x0000ffff) << 16);
    return x;
}
int main() {
    register int N, K, i, j, x, rev_x, rev_K;
    char c;
    for (scanf("%d%d\n", &N, &K), i = 0; i < N; ++i) {
        c = getchar();
        assert('A' <= c && c <= 'D');
        S[0][i] = c - 'A';
    }
    assert(1 <= i && i <= MAXN);
    for (rev_K = reverse_bits(K), j = 0; K; K -= x, rev_K -= rev_x, j ^= 1) {
        rev_x = rev_K & -rev_K;
        x = reverse_bits(rev_x);
        for (i = 0; i < N; ++i)
            S[j ^ 1][i] = S[j][i] ^ S[j][(i + x) % N];
    }
    for (i = 0; i < N; ++i) {
        printf("%c", S[j][i] + 'A');
    }
    printf("\n");
    return 0;
}