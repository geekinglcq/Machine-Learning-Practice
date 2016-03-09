#include<iostream>
using namespace std;

class sample {
public:
	sample();
	sample(int n, float* value, string* name);
	void set(int n, float* value, string* name);
	void printInfo();
private:
	string featureName[100];
	float featureValue[100];
	int cluster;
	int featureNumber;
};