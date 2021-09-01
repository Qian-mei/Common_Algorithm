def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
# 返回臂长
    return (right - left - 2) // 2
def longestPalindrome(s): # s -> str
    end, start = -1, 0
# 奇数->奇数， 偶数->奇数
    s = '#' + '#'.join(list(s)) + '#'
# arm_len 记录臂长
    arm_len = []
    right = -1
    j = -1
    for i in range(len(s)):
        if right >= i:
# i关于j的对称点i_sym 
            i_sym = 2 * j - i
            min_arm_len = min(arm_len[i_sym], right - i)
# 初始不需要从0，0起步
            cur_arm_len = expand(s, i - min_arm_len, i + min_arm_len)
        else:
            cur_arm_len = expand(s, i, i)
        arm_len.append(cur_arm_len)

        if i + cur_arm_len > right:
            j = i
            right = i + cur_arm_len
        if 2 * cur_arm_len + 1 > end - start:
            start = i - cur_arm_len
            end = i + cur_arm_len
    return s[start+1:end+1:2]

if __name__ == '__main__':    
    S = input()
    print(longestPalindrome(S) )