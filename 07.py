from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    size = len(in_cabin) #將in_cabin的長度指定給size
    sta = Stack(size) #利用Stack類別建立sta(station)
    step = [] #初始化step為一個空list
    real_out = [] #初始化一個list以便接收程式實際執行完後所的到的真正的「out_cabin」
    i_in = 0 #初始化一個index，用來指出正在執行的in_cabin中的項
    i_out = 0 #初始化一個index，用來指出正在執行的out_cabin中的項
    
    while(i_in < size and i_out < size): #當兩個index小於size的時候執行
        
        if in_cabin[i_in] == out_cabin[i_out]: #假入目前指到in_cabin的項等於目前out_cabin所需要的項則執行
            sta.push(in_cabin[i_in]) #將目前指到in_cabin的項移到sta
            step.append("push") #將"push"加到step
            step.append("pop") #將"pop"加到step
            if i_in < size - 1: #在一些例子，可能會有in_cabin已經指到最後一項，但是還有車廂在station沒有移到out_cabin，此時加一會讓index超出範圍，造成錯誤，所以in_cabin的index只在跑到最後一項前會加一
                i_in += 1 #在in_cabin中指向下一項
            i_out += 1 #在out_cabin_cabin中指向下一項
            real_out.append(sta.data[sta.top]) #將此時出站的車廂加入real_out，以便之後判斷執行是否成立
            sta.pop() #對sta執行pop
        
        elif  sta.data[sta.top] == out_cabin[i_out]:
            step.append("pop") #將"pop"加到step
            i_out += 1 #在out_cabin_cabin中指向下一項
            real_out.append(sta.data[sta.top]) #將此時出站的車廂加入real_out，以便之後判斷執行是否成立
            sta.pop() #對sta執行pop
        
        else:
            sta.push(in_cabin[i_in]) #將指到的in_cabin項移到sta
            step.append("push") #將"push"加到step
            i_in += 1 #在in_cabin中指向下一項
    
    if real_out == out_cabin: #假如實際的車廂順序符合out_cabin所指定的
        return step #將step回傳
    
    else: #否則
        step = [] 
        return step #回傳空list



if __name__ == "__main__":
    step = iostep(in_cabin =  [1,2,3], out_cabin = [2,1,3])
    print(step)