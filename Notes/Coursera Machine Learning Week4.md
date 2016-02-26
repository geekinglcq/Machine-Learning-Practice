#Coursera Machine Learning Week4
----
[Coursera Machine Learning](https://www.coursera.org/learn/machine-learning/home/welcome) Lunar's note 
Tags: MachineLearning Coursera

[TOC]

## 神经网络 Neural Network
###1. 非线性假设 Non-linear Hypotheses
+ 线性分类器不适合解决特征值过多，特征维数过大的问题，特别是图像处理
+ 神经网络旨在模仿人类大脑
###2. 模型表示
+ 人类的神经由树突（输入神经Dendrite），轴突（输出神经Axon）和神经元（Nucleus）组成。
+ 神经网络模型：每个神经元都是一个逻辑单元，由一个或几个输入，输出相应输出。每个神经元的输出都可以作为其他神经元的输入。一个神经元的功能是求得输入向量与权向量的内积后，经一个非线性传递函数得到一个标量结果。
神经网络分为三层 
1.Layer1：输入层
2.Layer2：隐藏层  可能不只一层
3.Layer3：输出层
数学表示 ：
![](//upload.wikimedia.org/math/0/f/9/0f9864bd5dd9678779b1e1ba493ad043.png)
W为权向量， 也写作$\Theta^{(j)}$,表示layer j到j+1的权重矩阵。
A为输入向量，A'表示转置。其中$a^{(j)}_i$表示layer j中第i个单元。
b是偏置量（bias）。
f为传递方程。
+ 理解：通过和逻辑回归对比，可以发现模型的形式其实是类似的，但是不同于逻辑模型只有一层，神经网络可以有多层，由多层的简单传递方程叠加起来就可以描述出非常复杂的特征，而不用增加逻辑回归中的
###3.多项分类器
用输出层的不同神经元表示不同class。比如输出层节点计算后的矩阵为0001时表示A，0010表示B等等。
