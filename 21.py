from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    lens = len(in_cabin)    #總共多少台車
    station = Stack(lens)   #創建一個長度lens的Stack
    steplst = []            #空步驟list
    cin = 0                 #count 為車進入的次數
    cout = 0                #count 為車離開的次數
    i = 0                   #station 裡剩餘數目
    while cin < lens:       #如果全部車都已經進入過就BREAK

        station.push(in_cabin[cin])         #將in_cabin[cin]對照的車號 push
        print(in_cabin[cin], "push\n")      #幾號車進站了
        steplst.append("push")              #steplist 新增"push"
        i += 1                              #在station裡增加一台車

        while station.data[i - 1] == out_cabin[cout]: #station.data[i - 1] = 排列一的車
    
            station.pop()                             #排列一開始的車號 pop
            print(out_cabin[cout], "pop\n")           #出站的車號
            i -= 1                                    #station減少了一台車
            steplst.append("pop")                     #steplist 新增"pop"

            cout += 1                                 #共離開了多少車
            if cout == lens:                          #IF 全部車都已經離開 BREAK
                break
        cin += 1                                      #共已經進入了多少台車
    if len(steplst) != 2*lens:                        #所有步驟的長度，一台車會有push和pop兩個步驟
        steplst = []                                  #如果沒有全部車都離開 steplst = 空list
    return steplst

if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3,4,5,6,7], out_cabin =     [2,4,6,5,3,7,1])
    print(step)


