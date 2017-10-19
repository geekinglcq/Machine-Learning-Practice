
#include<iostream>
#include<string>
#include"sample.h"
using namespace std;


sample::sample() {
	cluster = -1;
	featureNumber = 0;
}
sample::sample(int n,float value[]) {
	featureNumber = n;
	for (int i = 0; i < n; i++) {
		featureValue[i] = value[i];
	}
}
void sample::printInfo() {
	for (int i = 0; i < featureNumber; i++)
	{
		cout << featureName[i] << " : " << featureValue[i] << endl;
	}
}
void sample::set(float value[]) {
	
	for (int i = 0; i < featureNumber; i++) {
		featureValue[i] = value[i];		
	}
}



float sample::getFeature(int num) {
	return featureValue[num];
}
