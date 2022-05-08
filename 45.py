from stack_diy import Stack


def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    sta=Stack(len(in_cabin))
    step=[]
    n=len(in_cabin)
    while n>0:   
        #if  in_cabin!=[] and in_cabin[0]==out_cabin[0]:  #先判斷in_cabin不是空的list，才判斷in_cabin第0項等於out_cabin第0項(相反可能會造成沒有index而錯誤)
            #sta.push(in_cabin[0])       #push in_cabin第0項到sta
            #in_cabin=in_cabin[1:]       #刪除in_cabin第0項
            #sta.pop()                   #把剛push進來的值pop出去
            #out_cabin=out_cabin[1:]     #刪除out_cabin第0項
            #step.append("push") 
            #step.append("pop")          #append"push","pop"到step
            #n-=1 
            #continue               
        if sta.data[sta.top]==out_cabin[0]:     #sta.top的值等於out_cabin第0項
            sta.pop()                   #把sta的值pop出去
            out_cabin=out_cabin[1:]     #刪除out_cabin第0項
            step.append("pop")          #append"pop"到step
            n-=1
            continue           
        if in_cabin!=[]:  #判斷in_cabin不是空的list
            sta.push(in_cabin[0])       #push in_cabin第0項到sta
            in_cabin=in_cabin[1:]       #刪除in_cabin第0項
            step.append("push")         #append"push"到step
        else:
            step=[]     #把step設成空的list
            break       #跳開迴圈
    return step



if __name__ == "__main__":
    step = iostep( in_cabin = [1,2,3,4,5,6,7],
out_cabin = [2,4,6,5,3,7,1]







)
    print(step)