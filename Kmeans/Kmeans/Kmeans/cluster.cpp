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
	id = i;
}

int cluster::getQuantity() {
	return quantity;
}

void cluster::calQuantity() {
	int count=0;
	for (int i = 0; i < amount; i++) {
		if (label[i] == id)count++;
	}
}