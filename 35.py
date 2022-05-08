from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    list_len = len(in_cabin) 
    station = Stack(list_len)
    step = [] #最後要回傳的list，用來存取'push'及'pop'

    

    for i in range(1, list_len + 1): #in_cabin裡面有多少個數字就傳幾次
        if in_cabin[0] == out_cabin[0]:#如果符合條件，代表數字被push後馬上又被pop了
            step.append('push')
            step.append('pop')
            del in_cabin[0] #16、17行，消除已經經過流程的數字
            del out_cabin[0]
            if out_cabin == []:
                break
        if station.data[station.top] == out_cabin[0]: #station.data[station.top]為station最上層的數字，如果等於out_cabin[0]則pop
            step.append('pop')
            station.pop()
            del out_cabin[0]
            if out_cabin == []:
                break
        else:
            if in_cabin == []:
                continue
            else:
                station.push(in_cabin[0])#如果上述條件都不符合則持續將in_cabin[0]的數字push到station
                step.append('push')
                del in_cabin[0]
    
    a = len(step) #用來存取該out_cabin條件下，用了幾個push及pop
    total = list_len * 2 #正常情況下，push及pop的總數會等於in_cabin的元素數量再乘兩倍
    if a == total:
        return step
    else:
        return []




    

        





if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)