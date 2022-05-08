from stack_diy import Stack

def iostep(in_cabin, out_cabin):                                        # 將下方的 in_cabin / out_cabin 傳進來
    # <將你的程式碼寫在這裡>
    len_in_cabin = len(in_cabin)                                        # 用 len_in_cabin 接收 in_cabin 的長度
    station_Stack = Stack(len_in_cabin)                                 # 創建一個 station_stack 堆疊
    step = []                                                           # 創建一個空的 step 列表
                                                                        

    while len_in_cabin > 0:                                             # 當 in_cabin 的長度 > 0 ，就一直執行
        if  in_cabin != [] and in_cabin[0] == out_cabin[0]:             # 如果 in_cabin 不為空的列表 而且 in_cabin[0] == out_cabin[0]
            station_Stack.push(in_cabin[0])                             # 就呼叫 push 指令
            del in_cabin[0]                                             # 就刪掉 in_cabin[0] 的值
            del out_cabin[0]                                            # 就刪掉 out_cabin[0] 的值
            station_Stack.pop()                                         # 就呼叫 pop 指令
            step.append("push")                                         # 就把 step 列表 append "push" 進來
            step.append("pop")                                          # 就把 step 列表 append "pop" 進來
            len_in_cabin -= 1                                           # in_cabin 的長度 -1 
            continue                                                    
            

        
        if station_Stack.data[station_Stack.top] == out_cabin[0]:       # 如果 station_stack 堆疊裡的最上面一筆資料 == out_cabin[0]      
            station_Stack.pop()                                         # 就呼叫 pop 指令
            del out_cabin[0]                                            # 就刪掉 out_cabin[0] 的值
            step.append("pop")                                          # 就把 step 列表 append "pop" 進來
            len_in_cabin -= 1                                           # in_cabin 的長度 -1 
            continue                                                    

    
                           
        if in_cabin != [] and in_cabin[0] != out_cabin[0]:              # 如果 in_cabin 不為空的列表 而且 in_cabin[0] != out_cabin[0]
            station_Stack.push(in_cabin[0])                             # 就呼叫 push 指令
            del in_cabin[0]                                             # 就刪掉 in_cabin[0] 的值
            step.append("push")                                         # 就把 step 列表 append "push" 進來
        
        else:                                                           # 否則
            step = []                                                   # step 直接設為空的列表
            break

    return step                                                         # 回傳 step                     
                
        




if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3,4,5,6,7],out_cabin = [2,4,6,5,3,7,1])
    print(step)