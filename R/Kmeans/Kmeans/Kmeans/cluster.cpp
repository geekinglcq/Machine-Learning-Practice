#include<iostream>
#include"cluster.h"
using namespace std;

cluster::cluster() {
	content = 0;
	quantity = 0;
	memset(center, 0, 100);
	id = -1;
}
cluster::cluster(int i) {
	content = 0;
	quantity = 0;
	memset(center, 0, 100);
	id = i;
}

int cluster::getId() {
	return id;
}

void cluster::setId(int i) {
	content = 0;
	quantity = 0;
	memset(center, 0, 100);
	id = i;
}

int cluster::getQuantity() {
	return quantity;
}

float cluster::getCenter(int i) {
	return center[i];
}
void cluster::calQuantity() {
	int count=0;
	for (int i = 0; i < amount; i++) {
		if (label[i] == id)count++;
	}
	quantity = count;
}

void cluster::calCenter() {
	float temp[100] = {0};
	for (int i = 0; i < amount; i++) {
		if (label[i] == id)
			for (int j = 0; j < featureNum; j++) {
				temp[j] = temp[j] + dataSet[i].getFeature(j);
			}
	}	
	for (int j = 0; j < featureNum; j++) {
		center[j] = temp[j] / featureNum;
	}
}

void cluster::addSample(int i, bool changeCenter) {
	label[i] = id;	
	int t = quantity + 1;
	if (changeCenter) {
		for (int j = 0; j < featureNum; j++) {
			center[j] = (center[j] * quantity + dataSet[i].getFeature(j)) / t;
		}
	}
	quantity++;
}

void cluster::removeSample(int i,bool changeCenter) {
	label[i] = -1;
	int t = quantity;
	quantity--;
	if (changeCenter) {
		for (int j = 0; j < featureNum; j++) {
			center[j] = (center[j] * t - dataSet[i].getFeature(j)) / quantity;
		}
	}
}