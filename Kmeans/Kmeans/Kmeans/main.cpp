#include<iostream>
#include"sample.h"
#include"cluster.h"
using namespace std;

int sample::a;
string sample::featureName[100];
sample cluster::dataSet[100]; //All clusters share the same data set.
int cluster::label[100];
int cluster::amount;
int cluster::featureNum;

int main() {
	int k = 2;
	string na[2] = { "faef","dfa" };
	float s[2] = { 1,2 };
	
	return 0;
}


void initData(int featureNum,int sampleNum,string fileName) {
	int i, j, k;
}