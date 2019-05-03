
## CNN (Convolutional Neural Network)

> CNN是深度学习算法在图像处理领域的一个应用。

* 第一点，在学习Deep learning和CNN之前，总以为它们是很了不得的知识，总以为它们能解决很多问题，学习了之后，才知道它们不过与其他机器学习算法如`SVM`等相似，仍然可以把它当做一个`分类器`，仍然可以像使用一个黑盒子那样使用它。

* 第二点，Deep Learning强大的地方就是可以利用网络中间某一层的输出当做是数据的另一种表达，从而可以将其认为是经过网络学习到的特征。基于该特征，可以进行进一步的相似度比较等。

* 第三点，Deep Learning算法能够有效的关键其实是`大规模的数据`，这一点原因在于每个DL都有众多的参数，少量数据无法将参数训练充分。

### Convolution

> 卷积是指将一些数线性加权， 卷起来

* 一维卷积
  * a1, a2, a3
  * weight: w1, w2, w3
  * Convolution: a1*w1 + ...
  * 卷积窗口(window)大小为1*3

* 二维卷积
  * a11, a12, a13, ...
  * w: w11, ...
  * a11*w11 + a12*w12
  * 卷积窗口(window)大小为3*3

> :tada: 卷积的本质是进行滑动的融合(一维沿着一个方向滑动，二维沿着两个方向滑动)

## Reference

* [keras-team/keras: Deep Learning examples](https://github.com/keras-team/keras)