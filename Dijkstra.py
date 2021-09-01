import sys
# 虽然都适用于无向和有向连通图，但仅仅适用于单源点开始最短路径
def prim(g,n):
    dis = [0]*n
    pre = [-2]*n #可删除
    flag = [False]*n
    flag[0] = True
# 假设从index 0 即 A 出发搜寻
    k = 0
    pre[k] = -1 #可删除
# dis[i] 记录到i到A的最小距离，迭代更新 // 与Prim的差异
    for i in range(n):
        dis[i] = g[k][i]
    for j in range(n-1):
        mini = float('inf')
# find min dis
        for i in range(n):
            if mini>dis[i] and not flag[i]:
                mini = dis[i]
                k = i
# 对应 k=0
        if not k:
            return
# 更新flag，排除已经搜寻过的点
        flag[k] = True
        for i in range(n):
# find min dis, 更新pre
            if dis[i]>dis[k]+g[k][i] and not flag[i]:
# 更新dis[i]
                dis[i] = dis[k] + g[k][i]
                pre[i] = k #可删除
    return dis,pre #可删除pre


if __name__ == "__main__":
    _ = float('inf')
    # graph = [[0,6,3,_,_,_],
    #          [6,0,2,5,_,_],
    #          [3,2,0,3,4,_],
    #          [_,5,3,0,2,3],
    #          [_,_,4,2,0,5],
    #          [_,_,_,3,5,0]]
    graph = [[0,10,_,_,_,3],
             [_,0,7,5,_,_],
             [_,_,0,_,_,_],
             [3,_,_,0,7,_],
             [_,_,_,_,0,_],
             [_,2,_,6,1,0]]
    n = len(graph)
    dis,pre = prim(graph,n) #可删除pre
    dic = {-2:'Second',-1:'First'}
    for i in range(n):
        dic[i] = chr(i+65)
    for i in range(n):
        print('A-->',dic[i],'PRE:<--',dic[pre[i]],': ',dis[i]) #可删除pre
    