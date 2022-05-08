from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    output = []                  #設定要回傳出站步驟的list
    pop = []                     #設定用於接收pop出來的值得list
    size = len(in_cabin)         #進站車廂的長度
    check = Stack(size)          #設定車站
    j = 0
    for i in range(1,size+1):    #車廂依序進站
        check.push(i)
        output.append("push")    #進站後將push加入步驟list中
        if(out_cabin[j] == i):   #依照out_cabin檢查
            a = i
            while(a > 0 and j < i):
                if(out_cabin[j] == a):  #檢查當下的車廂與還未出站的車廂
                    pop.append(check.pop())  #儲存pop出的值
                    output.append("pop")     #出站後將pop加入步驟list中
                    j += 1
                a -= 1
        
    if pop!=out_cabin: #檢查pop出的值是否與out_cabin相同
        return("[]")
    else:
        return output #回傳出站步驟




if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3,4,5,6,7], out_cabin = [2, 4,6,5,3,7,1])
    print(step)