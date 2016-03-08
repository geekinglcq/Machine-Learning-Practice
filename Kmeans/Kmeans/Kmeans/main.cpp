#include<iostream>
#include"sample.h"
using namespace std;

int main() {
	int k = 2;
	string na[2] = { "faef","dfa" };
	float s[2] = { 1,2 };
	sample A = sample(k, s,na);
	A.printInfo();
	return 0;
}