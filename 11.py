from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    
    step = []#記錄步驟
    size = len(in_cabin)#list大小
    sta = Stack(size)
    index_in = 0#in_cabin和out_cabin的index
    index_out = 0
    check_list = []#用來儲存執行的結果
    
    while (index_in < size) and (index_out < size) :
        
        #如果in和out相同，就push再pop
        if in_cabin[index_in] == out_cabin[index_out]:
            step.append("push") 
            step.append("pop")
            sta.push(in_cabin[index_in])
            if index_in < size - 1:#要確認in_cabin是否到最後一個
                index_in += 1
            index_out += 1#in、out的讀取位置+1
            check_list.append(sta.data[sta.top])#儲存輸出
            sta.pop()
            
        elif sta.data[sta.top] == out_cabin[index_out]:#如果stack的top等於out所需，就pop
            step.append("pop")
            index_out += 1#out讀取位置+1
            check_list.append(sta.data[sta.top])#儲存輸出
            sta.pop()
            
        else:#如果以上兩種都不符合就直接push
            step.append("push")
            sta.push(in_cabin[index_in])
            index_in += 1#in讀取位置+1
    
    #檢查能不能按照out_cabin出站
    if check_list == out_cabin:
        return step
    else:
        step = []
        return step
        
        
    



if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3],out_cabin = [3,1,2])
    print(step)