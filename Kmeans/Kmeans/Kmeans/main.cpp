#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
#include<stdlib.h>
#include<time.h>
#include"sample.h"
#include"cluster.h"
using namespace std;


string sample::featureName[100];
int sample::featureNumber;
sample cluster::dataSet[100]; //All clusters share the same data set.
int cluster::label[100];
int cluster::amount;
int cluster::featureNum;
int clusterNum;
cluster *clu;
//Convert string to num
template <class Type>
Type stringToNum(const string& str)
{
	istringstream iss(str);
	Type num;
	iss >> num;
	return num;
}

void initData(int featureNum, int sampleNum, string fileName) {
	int i, j, k;
	ifstream in;
	in.open(fileName, ios::in);
	if (!in.is_open()) {
		cout << "No such file." << endl;
		return;
	}
	sample::featureNumber = featureNum;
	cluster::amount = sampleNum;
	for (i = 1; i <= sampleNum; i++) {
		string t;
		char c;
		float tt;
		float tempData[100];
		in >> tt;
		tempData[0] = tt;

		for (j = 1; j < featureNum ; j++) {
			in >> c;
			in >> tt;
			tempData[j] = tt;
		}
		cluster::dataSet[i].set(tempData);
	}
}

void randomDistribute() {
	int i, j;
	srand((unsigned)time(NULL));
	for (int i = 1; i <= cluster::amount; i++) {
		int t = (rand() % (clusterNum  + 1)) + 0;
		clu[t].addSample(i);
	}
}
int main() {
	int k = 2;
	string na[2] = { "faef","dfa" };
	float s[2] = { 1,2 };
	initData(3, 3,"a.txt");
	clu = new cluster[clusterNum];
	
	clusterNum = 3;
	return 0;
}


