def get_next(tar):
    n = len(tar)
    nex = [-1]*n
    j,k = 0,-1
    while j<n-1:
        if k == -1 or tar[j] == tar[k]:
            j += 1
            k += 1
            nex[j]  = k
        else:
            k = nex[k]
    print(nex)
    return nex
    
def kmp(S,tar):
    i = j =0
    m,n = len(S),len(tar)
    nex = get_next(tar)     # 生成next()数组
    while i<m and j<n:
        if j == -1 or S[i] == tar[j]:
            i += 1
            j += 1
        else:
            j = nex[j]
    return i-j if j == n else -1

if __name__ == '__main__':   
    S,tar = input().split()
    index = kmp(S,tar)
    print(S[index:index+len(tar)],tar)