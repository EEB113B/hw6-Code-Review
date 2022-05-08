from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    stack = Stack(len(in_cabin))
    lst_step = []     # 用來記錄步驟
    while True:
        if in_cabin == []:        # 如果in_cabin跑完了才會進入這個迴圈 (最後再看)                   
            while True:
                if out_cabin == []:        # 如果in_cabin跟out_cabin都跑完了就代表可以以out_cabin的排列方式出站
                        return lst_step   
                if out_cabin[0] == stack.data[stack.top]:  # in_cabin跑完了可能還有一些元素在stack 所以要確認是否都可以依照out_cabin的順序出站        
                    stack.pop()                          
                    lst_step.append("pop")
                    out_cabin.pop(0)
                    if out_cabin == []:        
                        return lst_step        
                else:                             # 如果中間有stack的第一個元素跟要出站的元素不同則回傳空lst
                    return []                     
        if in_cabin[0] == out_cabin[0]:           # 如果要進站的跟要出站的元素相同 (先看這邊)
            stack.push(in_cabin[0])               # 就先push在pop
            lst_step.append("push")
            in_cabin.pop(0)
            stack.pop()
            lst_step.append("pop")
            out_cabin.pop(0)
        elif out_cabin[0] == stack.data[stack.top]:        # 如果不同 檢查stack的第一個元素是否跟要出站的元素相同    
            stack.pop()                                    # 相同就pop
            lst_step.append("pop")
            out_cabin.pop(0)
        elif out_cabin[0] != stack.data[stack.top]:        # 如果都不同 就讓要進站的元素進站
            stack.push(in_cabin[0])
            lst_step.append("push")
            in_cabin.pop(0)
        
if __name__ == "__main__":
    in_cabin = [1,2,3,4,5]
    out_cabin = [3,4,1,2,5]
    step = iostep(in_cabin, out_cabin)
    print(step)