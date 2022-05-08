from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    x = len(in_cabin)                           #x為in_cabin的長度
    self = Stack(x)                             
    output = []                                 #output維新的空字串
    for l in range(x):
        if in_cabin[0] == out_cabin[0]:         #如果in[0]=out[0]，先push再pop
            output.append("push")               #push加入ouput陣列
            output.append("pop")                #pop加入ouput陣列
            del in_cabin[0], out_cabin[0]       #做完上述指令後要刪除in[0]、out[0]，繼續往下比對
    
            if out_cabin == []:                 #如果out_cabin為空字串就跳出，要不然最後會用空字串跟下一個的top比對，會照成錯誤
                break

        if self.data[self.top] == out_cabin[0]: #如果Stack的top=out[0]，加入pop
            output.append("pop")                #pop加入ouput陣列
            self.pop()                          #執行stack_diy裡面的pop指令
            del out_cabin[0]                    #刪除out[0]

            if out_cabin == []:                 #如果out_cabin為空字串就跳出
                break

        else:
            if in_cabin == []:                  #如果in_cabin為空字串就繼續跑這個迴圈
                continue
            else:
                self.push(in_cabin[0])          #執行stack_diy裡面的push指令    
                output.append("push")
                del in_cabin[0]
            
    if len(output) == x*2:                      #如果最後output的長度為in_cabin的兩倍，回傳output
        return output
    else:
        return []                               #否則代表無法成立，就回傳空串

if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3], out_cabin =  [2,1,3])
    print(step)