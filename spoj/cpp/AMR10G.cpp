#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>
#include <map>

using namespace std;

long long minimum_difference_for_k(vector<long long> children_heights, int no_childrens, int k)
{
	if (k == 1)
		return 0;
	sort(children_heights.begin(), children_heights.end());

	int start_index=0;
	long long min_diff = 1000000000, tmp_diff;
	while ((k+start_index-1) < no_childrens) {
		tmp_diff = children_heights[k+start_index-1] - children_heights[start_index];
		if (tmp_diff < min_diff)
			min_diff = tmp_diff;
		start_index++;
	}

	return min_diff;
}

int main()
{
	int t, no_childrens, k, I;
	long long tmp_hgt;
	vector<long long> children_heights;

	scanf("%d", &t);

	while (t--) 
	{
		scanf("%d %d", &no_childrens, &k);
		children_heights.clear();

		for(I=0; I < no_childrens; ++I)
		{
			scanf("%lld", &tmp_hgt);
			children_heights.push_back(tmp_hgt);
		}

		printf("%lld\n", minimum_difference_for_k(children_heights, no_childrens, k));
	}
	return 0;
}