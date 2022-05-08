from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    step=[]                                                                            #設輸出list為step
    station=Stack(len(in_cabin))                                                       #設station為Stack
    while 1:                                                                           #進入迴圈
        if station.data[station.top]==out_cabin[0]:                                    #如果station中的最上層資料=輸出車廂中0位置的值，進入     
            station.pop()                                                              #將station中的最上層資料刪除
            step.append("pop")                                                         #step中加入"pop"字串
            out_cabin.remove(out_cabin[0])                                             #將輸出車廂中的0位置,刪除
        else:                                                                          #以上皆不成立，進入下面
            station.push(in_cabin[0])                                                  #station 接受輸入車廂中的0位置的值
            step.append("push")                                                        #step中加入"push"字串
            in_cabin.remove(in_cabin[0])                                               #將輸入車廂中的0位置,刪除

        if in_cabin==[]  and out_cabin!=[] and station.data[station.top]!=out_cabin[0]: #如果輸入車廂為空list，且輸出車廂不為空list，且station中最上層資料不等於輸出車廂中0位置的值，進入
            step=[]                                                                    #將step指派為空list
            break                                                                      #跳出迴圈
        if in_cabin==[] and station.data[station.top]==0 and out_cabin==[]:            #如果輸入車廂為空list，且輸出車廂為空list，且station中最上層資料等於0，進入
            break                                                                      #跳出迴圈
    return step                                                                        #回傳list step

if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3], out_cabin =  [2,1,3])
    print(step)
    
    # 記得要 return，回傳值型態為 list
    

