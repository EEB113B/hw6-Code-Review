from numpy import size
from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    size=len(in_cabin)   #長度
    sta = Stack(size)   #最多堆疊到跟size一樣
    out = []
    x=0;i=0             #$ x->讀out_cabin的位子，i->讀in_cabin位子
    while(1): 
        decid=0 #決定是否跑最後一個if
        if(in_cabin[i] == out_cabin[x]):#如果in的第一個跟out的第一個一樣 先push再pop
            sta.push(in_cabin[i])
            out.append('push')
            sta.pop()
            out.append('pop')
            if(i<size-1):   #如果i尚未超出size-1(未讀取完畢) 就+1 
                i+=1
            if(x<size-1): #如果x尚未超出size-1 就+1
                x+=1
            else:       #如果x讀完了(代表完成了)就跳出
                break
            decid+=1
        if(sta.data[sta.top] == out_cabin[x]):#如果堆疊最上層跟out一樣，就pop
            out.append('pop')
            sta.pop()
            # x+=1
            if(x<size-1): #如果x尚未超出size-1 就+1
                x+=1
            else:         #如果x讀完了(代表完成了)就跳出
                break
            decid+=1
        if(decid==0):           ##如果上述兩個都不是才跑都不是就先push再跑一次
            out.append('push')
            sta.push(in_cabin[i])
            if(i<size-1):
                i+=1
            if sta.isFull():##如果堆疊滿了-> 無解
                out = []
                break
    return(out)


if __name__ == "__main__":
    step = iostep(in_cabin =  [1,2,3], out_cabin = [4,4,4])
    print(step)