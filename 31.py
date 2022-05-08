from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    n = len(in_cabin)
    step = []
    sta = Stack(len(in_cabin))
    while n > 0:
        if sta.data[sta.top] == out_cabin[0]:
            sta.pop()
            step.append("pop")
            out_cabin = out_cabin[1:]
            n = n - 1
            continue

        if in_cabin != []:
            sta.push(in_cabin[0])
            step.append("push")
            in_cabin =in_cabin[1:]
        else:
            step = []
            break
    return step 
            

        
        

if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3,4,5,6,7], out_cabin = [2,4,6,5,3,7,1])
    print(step)