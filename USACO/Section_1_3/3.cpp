/*
ID: vinod.d1
PROG: calfflac
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
 
using namespace std;

int map[30000], maxPalinLen=0, mxlimitL, mxlimitR;
char easytolower(char in){
  if(in<='Z' && in>='A')
    return in-('Z'-'z');
  return in;
}

void palinLength(string s, int slen, int index)
{
	int plen = 0, I, J, mxplen, limitL=0, limitR=0;

	J = index-1;
	I = index;
	while (
		J >= 0 
		&& 
		I < slen 
		&&
		s[J] == s[I] 
	) {
		J--;
	    I++;
	    plen++;
	}

	mxplen = 2*plen;

	limitL = map[J+1];
	limitR = map[I-1];

	plen = 0;
	J = index-1;
	I = index+1;

	while (
		J >= 0 
		&& 
		I < slen 
		&&
		s[J] == s[I] 
	) {
		J--;
	    I++;
	    plen++;
	}
	
	plen = 2*plen + 1;
	
	if (plen > mxplen) {
	   mxplen = plen;
	   limitL = map[J+1];
	   limitR = map[I-1];
	}

	if (maxPalinLen < mxplen) {
		mxlimitL = limitL;
		mxlimitR = limitR;
		maxPalinLen = mxplen;
	}
}

int main() 
{
	ofstream fout ("calfflac.out");
	ifstream fin ("calfflac.in");

	int slen, I, J, Z=0;
	char temp;
	string text, tmpTxt;
	string parseText = "";
	
	while (getline(fin, tmpTxt)) 
	{
	    text += "\n"+tmpTxt;
	}

	slen = text.length();

	for (I=0; I < slen; ++I)
	{
		temp = easytolower(text[I]);

		if (temp >= 'a' && temp <= 'z') {
			parseText += temp;
			map[Z] = I;
			Z++;
		}
	}

	slen = parseText.length();

	for (I=1; I < slen-1; ++I)
	{
	   palinLength(parseText, slen, I);
	}

	fout << maxPalinLen << "\n";

	for (I=mxlimitL; I<=mxlimitR; ++I) {
		fout << text[I];
	}

	fout << "\n";

	return 0;
}