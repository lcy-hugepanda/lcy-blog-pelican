Something about Loss Functions: 正篇（一）
######################################################################

:subtitle: 从学习问题的形式化描述开始
:date: 2010-10-03 10:20
:modified: 2010-10-04 18:40
:tags: Boosting, Loss function
:category: Machine Learning
:slug: sth-about-loss-function-1
:authors: LCY.Seso
:summary: Short version for index and feeds
:Image: /images/my-super-image.png

---

一切从学习算法和学习问题的形式化描述开始，这种观点可以解释许多学习算法。

:math:`X \subset R^N` 是 *N* 维输入空间，$Y$是输出空间，这里限定$Y\in \{-1,+1\} $（首先研究二分类问题）。$\mathcal {D} $是$X\times Y$上固定但未知的分布，训练样本集S $ \{ (x_1,y_1),(x_2,y_2),...,(x_n,y_n) \} $依分布$ \mathcal {D} $独立同分布产生（iid假设）。选择函数空间$F$，定义损失函数$L(y,f(x))$，学习算法从函数空间中选择一个$f_0$，使期望风险$\eqref{1}$最小（也就是期望风险最小化准则）。

