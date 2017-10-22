#模式识别　实验报告　　 
*SA17011050 陆承镪*   

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

* [模式识别　实验报告](#模式识别-实验报告)
	* [实验数据集](#实验数据集)
	* [分类器](#分类器)
		* [Logistic Regression](#logistic-regression)
		* [SVM  (线性核)](#svm-线性核)
	* [实验条件](#实验条件)
		* [Iris](#iris)

<!-- /code_chunk_output -->


## 实验数据集　　
本次实验选取了三份数据集分别是：　　
+ [**Iris Data**](http://archive.ics.uci.edu/ml/datasets/Iris)   该数据集包含了三类鸢尾花的特征，每类有50条数据，特征为４维，分别是萼片和花瓣的宽度以及长度。　　
+ [**Adult**](http://archive.ics.uci.edu/ml/datasets/Adult) 该数据集共有48842条数据，特征有14维，类别有两类——收入是否超过５万美元一年，分布大约是24%(超过５万美元)和76(不超过)。　　
+ [**Sensorless Drive Diagnosis**](http://archive.ics.uci.edu/ml/datasets/Dataset+for+Sensorless+Drive+Diagnosis) 该数据集有58509条数据，共有11类，特征为49维。  

## 分类器　　
本次实验，我选取了３个分类器。分别是：　　　
### Logistic Regression  
目标函数为：  
$$\underset{w, c}{min\,} \frac{1}{2}w^T w + C \sum_{i=1}^n \log(\exp(- y_i (X_i^T w + c)) + 1) .$$  
使用Python的sklearn工具包。  
超参数有：  
+ penalty： 惩罚项  
+ C：正则化值  
+ max_iter：最大迭代次数  

### SVM  (线性核)  


## 实验条件  
### Iris  
在该数据集上，由于数据集较小，所以这里仅作为toy data用于上手。不做交叉验证，评估参数仅为精度判别精度Acc。