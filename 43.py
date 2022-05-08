from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    ans = []
    ll = len(in_cabin)  #計算字串長度
    sta = Stack(ll)     #建立車站堆疊
    in_ = Stack(ll)     #建立進站堆疊
    out = Stack(ll)     #建立出站堆疊

    #堆疊ll,ll-1,...,1;最上層為1
    for i in range(ll,0,-1):    
        in_.push(i)
    #堆疊out_cabin[ll-1],out_cabin[ll-2],...,out_cabin[0];最上層為out_cabin[0]
    for j in range(ll-1,-1,-1):     
        out.push(out_cabin[j])      
    #若出站堆疊非空，則開始比較
    while not(out.isEmpty()):
        #比較進站、出站堆疊的最上層，若相同，則刪除  
        if(not in_.isEmpty() and in_.data[in_.top] == out.data[out.top]):   #
            in_.pop()
            out.pop()
            ans.append("push")
            ans.append("pop")
        #當車站堆疊非空時，先和出站堆疊比較，若相同，則刪除
        elif (not sta.isEmpty() and sta.data[sta.top]== out.data[out.top]):
            sta.pop()
            out.pop()
            ans.append("pop")
        #將進站堆疊的最上層加到車站堆疊中，加入後刪除最上層
        elif (not in_.isEmpty()):
            sta.push(in_.data[in_.top])
            ans.append("push")
            in_.pop()
        #上述條件皆不符合時，跳出迴圈
        else:
            break
    #若最後出站堆疊為空，表示可以以out_cabin順序出站   
    if (out.isEmpty()):
        return ans
    else:
        ans = []
        return ans

if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3,4,5,6,7] , out_cabin = [2,4,6,5,3,7,1] )
    print(step)