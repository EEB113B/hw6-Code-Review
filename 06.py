from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    check_len = len(in_cabin)   #check_len為list長度
    check = Stack(check_len)    #設定station
    ans = []                    #設定要回傳的答案(list)
    pop_list = []                    #設定接收pop出來的值的list，用來判斷是否與out_cabin相同，不同的話代表不成立
    i = 1                       #用來當push的值
    b = 0                       #用來當判斷out_cabin的值
    while(i<=check_len):        #當i小於list長度
        check.push(i)           #把i push到station
        ans.append("push")      #"push"加入ans
        if(out_cabin[b]==i):    #push到out_cabin中的第一個數字就停止
            a = i               
            while(a>0 and b < check_len):   
                if(a == out_cabin[b]):           #當a與out_cabin的第一個值相同時
                    pop_list.append(check.pop()) #將pop出的值(a)，值存到pop_list
                    ans.append("pop")            #"pop"加入ans   
                    b+=1                         #b變成out_cabin的下一個值
                a-=1                             #a變成i前一個值                                             
        i+=1
    if(pop_list!=out_cabin):    #如果pop_list不等於out_cabin，不成立
        return("[]")
    else:
        return ans              #如果相同，回傳ans
        

if __name__ == "__main__":
    step = iostep(in_cabin =  [1,2,3,4,5,6,7], out_cabin = [2,4,6,5,3,7,1])
    print(step)