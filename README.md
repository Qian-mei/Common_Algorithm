# Commonn Algorithm
用Python编写了常见的5中数据结构中的算法 KMP、Kruskal、Prim、Dijistra以及Manacher。

## KMP
***KMP*是在字符串比较中对*BP*算法(切片)的进一步改进，利用目标字符串自身的规律，事先构建*next()数组*存放 不匹配时 指针下一个移动的的位置，从而避免每次都要从头开始对比。**

## Manacher
**在奇数长度字符串中（可对字符串间隔 + "#"/特殊符号使得字符串必定变为奇数长度）寻找回文字符子串时，利用回文字符中心对称的特殊性，可以利用left，right（已判断回文字符串边界）作为搜寻其他回文字符初始参数，减少计算量**


## Prim和Kruskal
**都是计算单连通无向图的最短总路径长度的算法，差别是*Prim*从**顶点V**出发，不断更新当前最短路径相邻顶点V的边E的数据从而添加下一个顶点V。而*Kruskal*从**边E**出发，对所有边长首先进行排序，再依据并查集从小到大添加其他集合的顶点V。**

## Dijistra
**虽然都适用于无向和有向连通图，但仅仅适用于单源点开始的最短路径。思路与*Prim*类似，只需改变*Prim*中的更新条件（从dis[i]>g[k][i] -->dis[i]>dis[k]+g[k][i],即将记录到达*i*的最短距离dis改为从*Start*开始到达*i*的最短距离）**






