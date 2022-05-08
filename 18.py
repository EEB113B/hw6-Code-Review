from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    lens = len(in_cabin) #總共有多少輛車
    station = Stack(lens) #創建一個長度lens的Stack
    steplst = [] 
    cin = 0  #車進入的次數
    cout = 0 #車離開的次數
    while cin < lens: #如果全部車都進入過就離開迴圈

        station.push(in_cabin[cin]) #將in_cabin[cin]對照的車號 push
        print(in_cabin[cin], "push\n") #幾號車進站了
        steplst.append("push") #steplist 新增"push"

        while station.data[station.top] == out_cabin[cout]: #station.data[station.top] = 最頂層的車
    
            station.pop() #將station.data[station.top]也就是最頂層對照的車號 pop
            print(out_cabin[cout], "pop\n") #幾號車出站了
            steplst.append("pop") #steplist 新增"pop"

            cout += 1 #總共已經離開了多少台車
            if cout == lens: #如果全部車都已經離開就離開迴圈
                break
        cin += 1 #總共已經進入了多少台車
    if len(steplst) != 2*lens: #總共步驟的長度，一台車會有push和pop兩個步驟
        steplst = [] #如果沒有全部車都離開 steplst = 空list
    return steplst



if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3,4,5,6,7], out_cabin =     [2,4,6,5,3,7,1])
    print(step)