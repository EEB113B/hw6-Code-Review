from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    lens = len(in_cabin)
    station = Stack(lens)
    steplst = []
    c_in = 0 #車進入次數
    c_out = 0 #車離開次數
    i = 0 #station剩餘車輛

    while c_in < lens: #如果全部車都已經進入過就離開迴圈
        station.push(in_cabin[c_in]) #按順序push車輛
        steplst.append("push")

        i += 1

        while station.data[i - 1] == out_cabin[c_out]: #station.data[i - 1]為最頂層車輛
            station.pop() #將station頂層資料pop
            steplst.append("pop")

            i -= 1
            c_out += 1

            if c_out == lens: #如果全部車都已經離開就離開迴圈
                break

        c_in += 1

    if len(steplst) != 2*lens: #步驟總長度
        steplst = [] #如果沒有全部車都離開回傳空list

    return steplst


if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)