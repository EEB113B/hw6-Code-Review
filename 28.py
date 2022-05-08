from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    length = len(in_cabin)                            #$定義輸入list長度
    station =  Stack(length)                          #定義車站，順便給Stack大小
    step_1 = []                                       #設定要回傳的字串
    
    for i in range(length):                           #輸入字串有幾個，for迴圈就跑幾次
        if in_cabin[0] == out_cabin[0]:               #如果in 和 out字元相等，先push在pop
            step_1.append("push")
            step_1.append("pop")
            del in_cabin[0]                           #刪除in[0]和out[0]的字元，這樣in[1]和out[1]的字元就可以往前移變成in[0]和out[0]，方便程式運算
            del out_cabin[0]
            if out_cabin == []:                       #如果out是空字串，結束迴圈，避免接下來的程式判斷會跟空字串判斷，會error
                break
        if station.data[station.top] == out_cabin[0]: #如果station的top == [0]，pop
            step_1.append("pop")
            station.pop()                             #可以更改station內top的順序
            del out_cabin[0]                          #刪除out[0]的字元，這樣out[1]的字元就可以往前移變成out[0]，方便程式運算
            if out_cabin == []:                       #如果out是空字串，結束迴圈，避免接下來的程式判斷會跟空字串判斷，會error
                break
        else:
            if in_cabin == []:                        #如果in是空字串，重新跑回圈
                continue
            else:
                station.push(in_cabin[0])             #將字元加入車站內
                step_1.append("push")
                del in_cabin[0]                       #刪除in[0]字元
            
            
    a = len(step_1)
    total = length * 2
    if a == total:                                    #如果車廂可以完整地排列，則step_1會有完整地的push和pop，step_1的長度剛好會是in_cabin的2倍
        return step_1
    else:
        return []



if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)