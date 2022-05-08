from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    length = len(in_cabin)
    station =  Stack(length)
    step_1 = []
    for i in range(length):
        if in_cabin[0] == out_cabin[0]:#如果in的頭和out的頭相同，進行push和pop
            step_1.append("push")
            step_1.append("pop")
            del in_cabin[0]#將in的頭刪除
            del out_cabin[0]#將out的頭刪除
            if out_cabin == []:
                break
        if station.data[station.top] == out_cabin[0]:#如果out的頭和station的頭相同，進行pop
            step_1.append("pop")
            station.pop()#將station的頭指向下一個
            del out_cabin[0]#將out的頭刪除
            if out_cabin == []:
                break
        else:#除了以上兩種案例，皆進行push
            if in_cabin == []:
                continue
            else:
                station.push(in_cabin[0])#將in的頭push進station
                step_1.append("push")
                del in_cabin[0]#將in的頭刪除
            
            
    a = len(step_1)#結果的長度
    total = length * 2#每個字元要進行push和pop，所以乘2
    #判斷理論長度以及實際長度是否吻合
    if a == total:#
        return step_1
    else:
        return []



if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3,4,5,6,7], out_cabin = [2,4,6,5,3,7,1])
    print(step)