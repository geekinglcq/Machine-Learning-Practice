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
	void addSample(int i);
	void removeSample(int i);

	static sample dataSet[100];
	static int label[100];
	static int amount;
private:
	int id;
	int content;
	int quantity;
	float center[100];
};