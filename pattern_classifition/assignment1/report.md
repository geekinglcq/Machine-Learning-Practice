#模式识别　实验报告　　 
*SA17011050 陆承镪*   

<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->
<!-- code_chunk_output -->

* [模式识别　实验报告](#模式识别-实验报告)
	* [实验数据集](#实验数据集)
	* [分类器](#分类器)
		* [Logistic Regression](#logistic-regression)
		* [SVM  (高斯核)](#svm-高斯核)
		* [GBDT](#gbdt)
	* [实验条件](#实验条件)
		* [Iris](#iris)
			* [LR](#lr)
		* [Adult](#adult)
		* [Drive](#drive)

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
**超参数**：  
+ `penalty`： 惩罚项  
+ `C`：正则化值  

### SVM  (高斯核)    
目标函数：   
$$min\;\; \frac{1}{2}||w||_2^2 +C\sum\limits_{i=1}^{m}\xi_i $$  
使用Python的sklearn工具包：
**超参数：**
+ `C`: 惩罚系数  
+ `gamma`:  核函数参数 $K(x, z) = exp(-\gamma||x-z||^2)\;\;\gamma>0$  

### GBDT  
总的目标函数为：  
$$\text{obj} = \sum_{i=1}^n l(y_i, \hat{y}_i^{(t)}) + \sum_{i=1}^t\Omega(f_i) $$  
这里$n$ 为集成的树的数量，对于第 $t$ 颗树，我们有：  
$$\text{obj}^{(t)} = \sum^T_{j=1} [G_jw_j + \frac{1}{2} (H_j+\lambda) w_j^2] +\gamma T$$  
**超参数：**  
+ `max_depth`: 树的最大深度  
+ `min_child_weight`: 最小子节点权重  
+ `gamma`: 最小节点分裂loss，数值越大模型越保守  
+ `subsample`： 采样比例  
+ `alpha`： l1正则化项  


## 实验条件  
### Iris  
在该数据集上，由于数据集较小，所以这里仅作为toy data用于上手。使用3折交叉验证，评估参数仅为精度判别精度Acc。   

#### LR     
下面是逻辑回归在该数据集上的实验数据，可以发现，惩罚函数l2相对来说较l1更优一些，而正则化值越大，判断的精度越高；但是可以看到，当C的数值取到5后，在另一参数取'l2'时就已经达到了测试集的最好成绩，再提高C的数值，只会造成过拟合。  

|   param_C |param_penalty  |mean_test_score  |mean_train_score|
|--|--|--|--|--|
|      0.1       |     l1       |  0.740000        |  0.729649|
|      0.1       |     l2       |  0.813333        |  0.819865|
|        1       |     l1       |  0.940000        |  0.966726|
|        1       |     l2       |  0.946667        |  0.963359|
|        5       |     l1       |  0.960000        |  0.969994|
|        5       |     l2       |  0.966667        |  0.969994|
|       10       |     l1       |  0.966667        |  0.973361|
|       10       |     l2       |  0.966667        |  0.976728|
|       15       |     l1       |  0.966667        |  0.973361|
|       15       |     l2       |  0.966667        |  0.980095|
|      20       |     l1       |  0.960000        |  0.973361|
|      20       |     l2       |  0.966667        |  0.983363|

### Adult

### Drive  
该数据集使用交叉验证。这里我们  