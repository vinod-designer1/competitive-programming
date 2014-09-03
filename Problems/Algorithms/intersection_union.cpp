#include <iostream>
#include <cstdio>
#include <algorithm>
#include <list>

using namespace std;
// len(n): length of list n


// time complexity : (len(a)+len(b)) log(len(a))
// space complexity: O(1)
// can make  O(len(a)+len(b)) time complexity using hashmap
list<int> union_c(list<int> a, list<int> b)
{
	// time complexity: len(a) * log(len(a))
	a.sort();

	// time complexity: len(b) * log(len(a))
	for (list<int>::const_iterator b_iterator = b.begin(), end = b.end(); b_iterator != end; ++b_iterator) 
	{
		 // time complexity: log(len(a));
         if (!binary_search (a.begin(), a.end(), *b_iterator))
         {
         	a.push_back(*b_iterator);
         }
	}

	return a;
}

// time complexity : (len(instersection_lst)+len(b)) * log((instersection_lst))
// space complexity: O(1)
// can make  O(len(a)+len(b)) time complexity using hashmap
list<int> union_with_intersection(list<int> a, list<int> b, list<int> instersection_lst)
{
	// time complexity: len(instersection_lst) * log(len(instersection_lst))
	instersection_lst.sort();

	// time complexity: len(b) * log(len(instersection_lst))
	for (list<int>::const_iterator b_iterator = b.begin(), end = b.end(); b_iterator != end; ++b_iterator) 
	{
		 // time complexity: log(len(instersection_lst));
         if (!binary_search (instersection_lst.begin(), instersection_lst.end(), *b_iterator))
         {
         	a.push_back(*b_iterator);
         }
	}

	return a;
}


// time complexity : (len(a)+len(b)) log(len(a))
// space complexity: O(len(a)+len(b))
// can make  O(len(a)+len(b)) time complexity using hashmap
list<int> intersection(list<int> a, list<int> b)
{
	list<int> intersection_list;
	//time complexity: len(a) * log(len(a))
	a.sort();

	//time complexity: len(b) * log(len(a))
	for (list<int>::const_iterator b_iterator = b.begin(), end = b.end(); b_iterator != end; ++b_iterator) 
	{
		 // time complexity: log(len(a));
         if (binary_search (a.begin(), a.end(), *b_iterator))
         {
         	intersection_list.push_back(*b_iterator);
         }
	}

	return intersection_list;
}

void print_list(list<int> b)
{
	for (list<int>::const_iterator b_iterator = b.begin(), end = b.end(); b_iterator != end; ++b_iterator) 
	{
		 cout << *b_iterator << endl;
	}
}

int main()
{
	list<int> a, b;

	//a inserts
	a.push_back(4);
	a.push_back(7);
	a.push_back(12);
	a.push_back(6);
	a.push_back(17);
	a.push_back(5);
	a.push_back(13);

    //b inserts
    b.push_back(7);
	b.push_back(19);
	b.push_back(4);
	b.push_back(11);
	b.push_back(13);
	b.push_back(2);
	b.push_back(15);

    cout << "UNION" << endl;
	list<int> union_list = union_c(a, b);
	print_list(union_list);

	cout << "INTERSECTION" << endl;
	list<int> intersection_list = intersection(a, b);
	print_list(intersection_list);
	return 0;
}