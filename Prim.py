import sys
# 适用于无向连通图
def prim(g,n):
    dis = [0]*n
    pre = [0]*n
    flag = [False]*n
    flag[0] = True
    k = 0
# dis[i] 记录到i的最小距离，迭代更新
    for i in range(n):
        dis[i] = g[k][i]
    for j in range(n-1):
        mini = float('inf')
# find min dis
        for i in range(n):
            if mini>dis[i] and not flag[i]:
                mini = dis[i]
                k = i
        if not k:
            return
# 更新flag，排除已经搜寻过的点
        flag[k] = True
        for i in range(n):
# find min dis, 更新pre// 更新当前节点k到周遭节点的dis，即下一个节点连上当前链路必定从dis中选择min dis
            if dis[i]>g[k][i] and not flag[i]:
# 更新dis[i]
                dis[i] = g[k][i]
                pre[i] = k
    return dis,pre


if __name__ == "__main__":
    _ = float('inf')
    graph = [[0,6,3,_,_,_],
             [6,0,2,1,_,_],
             [3,2,0,3,4,_],
             [_,5,3,0,2,3],
             [_,_,4,2,0,5],
             [_,_,_,3,5,0]]
    n = len(graph)
    dis,pre = prim(graph,n)
    
    dic = {}
    for i in range(n):
        dic[i] = chr(i+65)
    for i in range(n):
        print(dic[i],'-->',dic[pre[i]],': ',dis[i])
    