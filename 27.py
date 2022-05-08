from re import I
from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    stack = ['k']  #先給一個預設值，避免stack[-1]出現error
    ans = []  #放答案的空列表
    count = len(in_cabin)  #計算in_cabin的位置到哪了
    j = 0  #計算out_cabin的讀取位置
    for i in range(count):
        if in_cabin[i] == out_cabin[j]:  #若in跟out位置相同，push、pop
            ans.append('push')
            ans.append('pop')
            j += 1
            while j < count and stack[-1] == out_cabin[j]:  #若存在stack最後一個，pop
                ans.append('pop')
                stack.remove(stack[-1])
                j += 1
                continue
        else:
            stack.append(in_cabin[i])  #若不存在則新增到stack，push
            ans.append('push')
    if len(stack) > 1:  #在最後檢查stack若有除了初始值之外的東西，代表不能以push、pop排列
        ans = []
        
                
    return ans
if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3,4,5], out_cabin = [3,4,1,2,5])
    print(step)