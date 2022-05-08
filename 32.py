from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    lens = len(in_cabin)         #進站列車長度
    station = Stack(lens)        #依據列車長度創建車站
    steplst = []                 #創建step list
    ctin = 0                     #計算進入幾節車廂
    ctout = 0                    #計算離開幾節車廂
    i = 0                        #車站裡剩餘幾節車廂
    while ctin < lens:           #如果每節車廂都已經進入過就離開迴圈

        station.push(in_cabin[ctin])         #將in_cabin[ctin]對照的車號駛出
        print(in_cabin[ctin], "push\n")      #幾號車廂進站了
        steplst.append("push")               #新增"push"的動作至step list裡
        i += 1                               #車站多了一節車廂

        while station.data[i - 1] == out_cabin[ctout]:      #station.data[i - 1] = 最外面的車廂
    
            station.pop()                                   #將station.data[i - 1]也就是最外面的車廂的號碼駛出
            print(out_cabin[ctout], "pop\n")                #幾號車廂出站了
            i -= 1                                          #車站少了一節車廂
            steplst.append("pop")                           #新增"pop"的動作至step list裡

            ctout += 1            #計算已經離開多少幾節車廂
            if ctout == lens:     
                break             #如果全部車廂都已經離開就離開迴圈
        ctin += 1                 #計算已經進入多少幾節車廂
    if len(steplst) != 2*lens:    #總共步驟的長度，一台車會有進站"push"和出戰"pop"兩個動作
        steplst = []              #如果沒有全部車都離開step list就會是空的
    return steplst                #回傳step list


if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)
    step1 = iostep(in_cabin = [1, 2, 3, 4, 5, 6, 7], out_cabin = [2, 4, 6, 5, 3, 7, 1])
    print(step1)
    step2 = iostep(in_cabin = [1, 2, 3], out_cabin = [3, 1, 2])
    print(step2)