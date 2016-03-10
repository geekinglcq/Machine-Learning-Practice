#ifndef SampleHeader
#define SampleHeader
#include<iostream>
using namespace std;

class sample {
public:
	sample();
	sample(int n, float* value);
	void set(int n, float* value);
	float getFeature(int no);
	void printInfo();
	static string featureName[100];
	static int a;
private:	
	float featureValue[100];
	int cluster;
	int featureNumber;
};

#endif