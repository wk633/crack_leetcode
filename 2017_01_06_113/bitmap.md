## bitmap算法
### 概述
所谓bitmap就是用一个bit位来标记某个元素对应的value，而key即是这个元素。由于采用bit为单位来存储数据，因此在可以大大的节省存储空间
### 算法思想
32位机器上，一个整形，比如int a;在内存中占32bit，可以用对应的32个bit位来表示十进制的0-31个数，bitmap算法利用这种思想处理大量数据的排序与查询

### 优点：
效率高，不许进行比较和移位
占用内存少，比如N=10000000;只需占用内存为N/8 = 1250000Bytes = 1.2M，如果采用int数组存储，则需要38M多

### 缺点：
无法对存在重复的数据进行排序和查找
