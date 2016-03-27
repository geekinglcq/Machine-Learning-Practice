# Coursera Machine Learning Week7

Tags : MachineLearning Coursera

---
[TOC]

##支持向量机SVM(Support Vector Machine)
###1.从逻辑回归到SVM
在Logistics regression中，我们约定的cost function是:
$J(\theta)=\frac{1}{m}\sum^m_{i=1}(-ylog(h_\theta(x))-(1-y)log(1-h_\theta(x))$  
这里$h(x)$就是logistics函数，我们用两个近似函数$cost_1$和$cost_0$来替代他们，那么在SVM中
SVM hypothesis :
$minC\sum^m_{i=1}\Big \{ y^icost_1(\theta^Tx^i)+(1-y)cost_0(\theta^Tx^i)\Big \}+\frac{1}{2}\sum^n_{i=1}\theta^2_j$
如果相对于样本个数来说，样本的特征个数较大也就是n较大时，使用逻辑回归。
如果n小，m中等，SVM(高斯).
如果n小，m大，逻辑回归。
![QQ图片20160313101139.png-76.5kB][1]
###2.大间距分类器 Large Margin Intuition
####决策边界 Decision Boundary
margin指的是边界离样本的最近的距离，使margin最大化就是使cost function最小化的过程。因为使J变小也就是使$\frac{1}{2}||\theta||^2$变小（因为当C较大时我们会使前面那项尽可能为0，由此忽略）。但是因为$y>1$时要有$p^i*||\theta||>1$，所以要使$\theta$小的话，$p^i$就得大，也就是样本点离边界的距离要大，也就是margin要大。
####异常点
SVM在处理异常点上会根据C的值来给定边界。
###3.核函数 Kernels
####新的特征变量
限定原有的特征变量组成的向量X=($x_i～x_j$)，选择$l^k$，那么可以使用x和l的相似度$f^k=similarity(x,l^k)=exp(1\frac{||x-l^i||^2}{2\sigma^2})$作为新的特征变量。这里的相似函数simrlarity也被称为核函数Kernel(这里用的是高斯核函数Gaussian Kernel)。
####如何获得核 $l^i$
选择m个样本，将每一个都可以作为一个核。
####核函数的本质
就是将原来的特征向量转换为一个新的更适合SVM处理的特征向量。
####不同的核函数
+ 线性核函数 (没有核函数) $f^i=x^i$
+ 高斯核函数$f_i=exp(1\frac{||x-l^i||^2}{2\sigma^2})$,where $l^i=x^i$
+ 核函数需要满足 Mercer's Throrem从而使用各种数值优化算法。现在其他的核函数已经不多用了，它们有
+ 1. Polynomial kernel 
2. String kernel
3. chi-square kernel等等
###4.选择参数
$C=\frac{1}{\lambda}$
Large C:Lower bias,high variance.
Small C:Higher bias,low variance.
$\sigma^2$
Large:f分布更平滑，Higher bias,lower variance.
Small:较陡峭,Lower bias,Higher variance.
###5.多类分类
训练K个SVM。
  [1]: http://static.zybuluo.com/lunar/54g6463l6gyudqo3b2k06u83/QQ%E5%9B%BE%E7%89%8720160313101139.png