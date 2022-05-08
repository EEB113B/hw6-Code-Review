from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    size = len(out_cabin) #找出出站大小
    stack = Stack(size) #建立車站
    inside = 0 #設進站出站從0開始
    outside = 0
    answer = []
    while(outside<size):
        if inside == size and stack.data[stack.top] != out_cabin[outside]: #假如進站全部進入車站，且要出站的車站頂端不等於出站順序就不成立
            answer = []
            break
        if stack.data[stack.top] != out_cabin[outside]: #假如進站後的車站頂端不等於出站順序就再進站
            stack.push(in_cabin[inside])
            inside += 1
            answer.append("push")
        if stack.data[stack.top] == out_cabin[outside]: #假如進站後的車站頂端等於出站順序就出站
            outside += 1
            stack.pop()
            answer.append("pop")
    return answer





if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3,4,5,6,7], out_cabin =  [2,4,6,5,3,7,1])
    print(step)