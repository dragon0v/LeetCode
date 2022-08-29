[[python]] List.sort()的内部实现方式是[[Timsort]]

https://blog.csdn.net/sinat_35678407/article/details/82974174
## Timsort介绍
Timsort是一种混合、稳定高效的排序算法，源自合并排序和插入排序，旨在很好地处理多种真实数据。它由Tim Peters于2002年实施使用在Python编程语言中。该算法查找已经排序的数据的子序列，并使用该知识更有效地对其余部分进行排序。这是通过将已识别的子序列（称为运行）与现有运行合并直到满足某些条件来完成的。从版本2.3开始，Timsort一直是Python的标准排序算法。***如今，Timsort 已是是 Python、 Java、 Android平台 和 GNU Octave 的默认排序算法。***

## 思想
针对现实中需要排序的数据分析看，大多数据通常是有部分已经排好序的数据块，Timsort 就利用了这一特点。Timsort 称这些已经排好序的数据块为 “run”，我们可以将其视为一个一个的“分区”。在排序时，Timsort迭代数据元素，将其放到不同的 run 里，同时针对这些 run ，按规则进行合并至只剩一个，则这个仅剩的 run 即为排好序的结果。
换句话说，就是分析待排序数据，根据其本身的特点，将排序好的（不管是顺序还是逆序）子序列的分为一个个run分区，当然，这个分区run也存在一定的约束，即根据序列会产生一个minrun，如果原始的run小于minrun的长度，用插入排序扩充run，直到达到条件，之后使用归并排序来合并多个run。

## 时间复杂度
![O(n)](https://img-blog.csdn.net/20181008215140722?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3NpbmF0XzM1Njc4NDA3/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
本质上 Timsort 是一个经过大量优化的归并排序，而归并排序已经到达了最坏情况下，比较排序算法时间复杂度的下界，所以在最坏的情况下，Timsort 时间复杂度为O(nlogn)。在最佳情况下，即**输入已经排好序，它则以线性时间运行O(n)**。可以看出Timsort是目前最好的排序方式。




