#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

class DiskSpace {
   public:
   	int minDrives(vector<int>, vector<int>);
};

int DiskSpace::minDrives(vector<int> a, vector<int> b) {
    int arz = a.size(), i=0, cnt=0, rem;
    
    for (i<arz-1) {
    	if (a[i] != b[i]) {
    		while (i<arz-1 && a[i] == b[i]) {
    			if ((b[i]-a[i]) > 
    			a[i+1] -= 
    			i++;
    		}
    	} else {
    		cnt++;
    		i++;
    	}
    }

    if (a[i] != 0) cnt++;

    return cnt;
}