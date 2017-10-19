#pragma once
#include<iostream>
#include"sample.h"
class cluster {

public :
	cluster();
	cluster(int id);
	int getId();
	int getQuantity();
	void setId(int i);
	void calQuantity();
	void calCenter();
	float getCenter(int i);
	void addSample(int i,bool changeCenter);
	void removeSample(int i,bool changeCenter);


	static sample dataSet[100]; //All clusters share the same data set.
	static int label[100];
	static int amount;
	static int featureNum;
	static int clusterNum;
private:
	int id;
	int content;
	int quantity;
	float center[100];
};