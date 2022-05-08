from math import fabs
from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    size = len(in_cabin)
    in_cabin = Stack(size)      #設in_cabin為Stack的物件
    station_top = in_cabin.top  #為station的index
    station_data = [0]*size
    station_number = 1          #為要進station的數值
    ans_step = []               #為在station裡轉換步驟
    station_data_index = 0      #為station的index
    out_cabin_index = 0
    while True:
        station_data[station_data_index] = station_number   
        ans_step.extend(['push'])                           #輸入數值並加'push'到ans_step中
        while station_data[station_data_index] != 0:  
            same = False           #設same變數判斷是否與out_cabin相對應的index數值相同
            if out_cabin[out_cabin_index] == station_data[station_data_index]:
                same = True
                station_data[station_top + 1] = 0       #index數值相同則刪掉在station裡的那個數
                ans_step.extend(['pop'])                #再加'pop'到ans_step裡
                if station_top > -1:                    
                    station_top -= 1
                out_cabin_index += 1                    #判斷out_cabin的下一個數
                if station_data_index != 0:             
                    station_data_index -= 1
            if same == False:
                if out_cabin_index == size:             
                    break
                station_top += 1                        #若index數值不相同才繼續加數值到station，若是相同，則需繼續判斷station下一個數是否也等於out_cabin的下一個數直到index數值不相等
                station_data_index += 1
        station_number += 1
        if station_number > size:                       #丟進station的數為1 ~ size
            break
    correct = True                                      #判斷in_cabin是否能用堆疊的方法得到out_cabin
    for i in range(size):
        if station_data[i] != 0:                        #若最後station裡有不為0的數，代表in_cabin無法用堆疊的方法得到out_cabin，回傳空字串
            correct = False
            break
    if correct:
        return ans_step                                 
    else:
        return []
    
    
if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3, 4, 5, 6, 7], out_cabin =  [2, 4, 6, 5, 3, 7, 1])
    print(step)