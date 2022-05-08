from stack_diy import Stack
def iostep(in_cabin, out_cabin):
    length = len(in_cabin)              #先算出車站需要的長度
    station = Stack(length)             #使用Stack類別來建立Station
    ans_list = []                       #建立一個list放執行的動作並在最後回傳作為答案
    check = False                       #建立一個變數偵測車站進出是否發生錯誤
    for i in range(0,length):           #使用for迴圈執行全部車站進出的次數
        if check:                       #如果偵測變數變為True
            break                       #跳出迴圈並回傳空list
        while (True):
            if out_cabin[i] != station.data[station.top] and in_cabin == []:        #如果要離開車站的車不再在最上方且又沒有車能進入車站後 
                ans_list =[]                                                        #將答案list清空
                check = True                                                        #將偵錯指標變為True
                break                   
            if out_cabin[i] != station.data[station.top]:                           #如果要離開車站的車不在車站最上方
                station.push(in_cabin[0])                                           #讓下一輛車進入車站
                del in_cabin[0]                                                     #把進入車站的車從候補名單去掉
                ans_list.append("push")                                             #在答案list上記錄這次執行的指令push
            elif out_cabin[i] == station.data[station.top]:                         #如果要離開車站的車在車站最上方
                station.pop()                                                       #讓在最上方的車離開車站
                ans_list.append("pop")                                              #在答案list上記錄這次執行的指令pop
                break                                                               #離開迴圈讓for迴圈進入下一個次數記錄
    return ans_list                                                                 #回傳答案list
if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3], out_cabin = [2,1,3])
    print(step)