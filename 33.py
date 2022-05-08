from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    lens = len(in_cabin) #表示總車數
    station = Stack(lens) #建立一個長度lens的Stack
    steplst = [] #空步驟list
    cin = 0 #count 表示車進入的次數
    cout = 0 #count 表示車離開的次數
    i = 0 #station 表示剩餘幾台
    while cin < lens: #如果全部車都已經進入過就離開迴圈

        station.push(in_cabin[cin]) #將in_cabin[cin]對照的車號 push
        print(in_cabin[cin], "push\n") #表示幾號車進站
        steplst.append("push") #steplist 新增"push"
        i += 1 #station 新增了一台車

        while station.data[i - 1] == out_cabin[cout]: #station.data[i - 1] = 最頂層的車
    
            station.pop() #將station.data[i - 1]也就是最頂層對照的車號 pop
            print(out_cabin[cout], "pop\n") #表示哪幾號車出站了
            i -= 1 #station 少了一台車
            steplst.append("pop") #steplist 新增"pop"

            cout += 1 #總共已經離開了多少台車
            if cout == lens: #如果全部車都已經離開就離開迴圈
                break
        cin += 1 #總共已經進入了多少台車
    if len(steplst) != 2*lens: #總共步驟的長度，一台車會有push和pop兩個步驟
        steplst = [] #如果沒有全部車即離開 steplst = 空list
    return steplst



if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3,4,5,6,7], out_cabin =     [2,4,6,5,3,7,1])
    print(step)