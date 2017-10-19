#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
#include<sstream>
#include<stdlib.h>
#include<time.h>
#include<math.h>
#include"sample.h"
#include"cluster.h"
using namespace std;


string sample::featureName[100];
int sample::featureNumber;
sample cluster::dataSet[100]; //All clusters share the same data set.
int cluster::label[100];
int cluster::amount;
int cluster::featureNum;
int cluster::clusterNum;
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

void initData(int featureNum, int sampleNum, string fileName,bool header) {
	int i,j;
	ifstream in;
	in.open(fileName, ios::in);
	if (!in.is_open()) {
		cout << "No such file.System will use sample file." << endl;
		in.open("sample.txt", ios::in);
	}
	if (header) {
		for (i = 0; i < featureNum; i++) cin >> sample::featureName[i];
	}
	sample::featureNumber = featureNum;
	cluster::featureNum = featureNum;
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
	in.close();
}

void randomDistribute() {
	int i;
	srand((unsigned)time(NULL));
	for (i = 1; i <= cluster::amount; i++) {
		int t = (rand() % (clusterNum ));
		clu[t].addSample(i,true);
	}
	for ( i = 0; i < cluster::clusterNum; i++) {
		clu[i].calQuantity();
		clu[i].calCenter();
	}
}

void iteration(cluster* clu) {
	for (int i = 1; i <= cluster::amount; i++) {
		int flag;
		float min = 2 << 18;
		for (int j = 0; j < cluster::clusterNum; j++) {
			float temp = 0;
			for (int t = 0; t < sample::featureNumber; t++) {
				temp = temp + pow((cluster::dataSet[i].getFeature(t) - clu[j].getCenter(t)),2);
			}
			temp = pow(temp, 0.5);
			if (temp < min) {
				min = temp;
				flag = j;
			}
		}
		clu[cluster::label[i]].removeSample(i,false);
		clu[flag].addSample(i,false);
	}
	for (int i = 0; i < cluster::clusterNum; i++) {
		clu[i].calQuantity();
		clu[i].calCenter();
	}
}
int main() {
	cout << "Please enter the name of datafile." << endl;
	string file;
	cin >> file;
	cout << endl << "Please enter the amount of observations." << endl;
	int sampAmount;
	cin >> sampAmount;
	cout << endl << "Please enter the number of features." << endl;
	int countFeature;
	cin >> countFeature;
	cout << endl << "How many time do you want to iterate" << endl;
	int it = 0;
	cin >> it;
	int k = 2;
	
	
	initData(countFeature, sampAmount,file,false);
	clu = new cluster[clusterNum];
	clusterNum = 3; 
	cluster::clusterNum = 3;
	for (int i = 0; i < clusterNum; i++) clu[i].setId(i);
	randomDistribute();
	
	cout << endl << "Init:" << "SampleID : ClassID";
	cout << endl;
	for (int ii= 1;ii <= cluster::amount; ii++) {
		cout << setw(6) << ii << ":" << setw(6) << cluster::label[ii] << " | ";
	}
	for (int i = 0; i < cluster::clusterNum; i++) {
		cout << endl << "Class:" << i << endl;
		cout << "Center:	";
		for (int j = 0; j < cluster::featureNum; j++) cout << clu[i].getCenter(j) << "		";
	}

	for (int i = 0; i < it; i++) {
		cout << endl << "##################################################################" << endl;
		cout << "#   Iteration "<<i+1<<":" << endl;
		iteration(clu);
		for (int i = 0; i < cluster::clusterNum; i++) {
			cout <<endl<< "Class:" << i << endl;
			cout << "Center:	";
			for (int j = 0; j < cluster::featureNum; j++) cout << clu[i].getCenter(j) << "		";
		}
		cout << endl;
		for (int i = 1; i <= cluster::amount; i++) cout << setw(6) << i << ":" << setw(6) << cluster::label[i] << " | ";
		cout << endl;
	}
	cout << endl << "Press enter to exit.";
	getchar();
	return 0;
}


