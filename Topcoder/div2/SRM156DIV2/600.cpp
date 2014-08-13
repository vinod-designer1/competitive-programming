#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

class BombSweeper{
   public:
   	 double winPercentage(vector<string>);
   	 int ok(int, int);
};

double BombSweeper::winPercentage(vector<string> st) {
	int[] dx = {-1,-1,-1,0,0,0,1,1,1};
	int[] dy = {-1,0,1,-1,0,1,-1,0,1};
	int stl = st[0].length();
	int bl = st.size();
	int v[bl][stl];
	int winner = 1;

	for (int i=0; i < bl; i++)
		for (int j=0;j < stl; j++) 
			v[i][j] = (board[i][j]=='B');

	int lose=0, win=0;

	for (int i=0; i < bl; i++) {
		for (int j=0;j < stl; j++) {
		    if (v[i][j]) lose++;
		    else {
		    	winner = 1;
		    	for (int k=0; k<9;k++) {
		    		int nx = i+dx[k];
		    		int ny = j+dy[k];
		    		if (ok(nx, ny, bl, stl) && v[nx][ny])
		    			winner = 0;
		    	}
		    	if (winner) win++; 
		    }
		}
	}

	return win*100./(win+lose);
}

int BombSweeper::ok(int x, int y, int n, int m) {
	return x >= 0 && x < n && y >= 0 && y < m;
}