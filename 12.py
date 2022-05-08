from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    try:
        def stationpop():#主程式的出站方法
            delete_cabin.remove(station.data[station.top])
            station.pop()
            step.append('pop')

        
        step = []                      #字串陣列(最後回傳)
        length_station = len(in_cabin) #stack長度須為車廂總數
        lastcabin = length_station     #最後一個車廂的號碼
        delete_cabin = out_cabin[:]    #複製一個出站順序
        station = Stack(length_station)    #建立車站的物件，大小為列車車廂數，大小就是車站設定的位置大小

        for pushing_cabin in in_cabin:
                                            #pushing_car是目前進站的車廂
            step.append('push')             #同時將step新增'push'
            station.push(pushing_cabin)     #呼叫車站物件中的進站方法
            if pushing_cabin == lastcabin: #如果目前進站車廂為最後一個車廂，則進站後會立即出站
                stationpop()
                while station.isEmpty() == False:#如果車廂已出站，車站還有未出站的車廂
                    #則一一出站
                    stationpop()             
            else:
                #非最後進站的車廂時
                while out_cabin.index(station.data[station.top]) < out_cabin.index(station.data[station.top]+1):
                    #如果出站順序比較晚進站的車廂還前面，代表要先出站
                    stationpop()
                    #如車站的top車廂，剛好是下一個出站車廂(出站陣列delete_cabin索引值 ==0)
                    while delete_cabin.index(station.data[station.top]) ==0:
                        #進行出站
                        stationpop()
                        #如果空了，則跳出迴圈
                        if station.isEmpty():
                            break
                    #無須再出站，跳出迴圈，等待下一個進站車廂
                    break                 
        return step       
    except:
        ValueError
        return[]

if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [3,1,2])
    print(step)#[]
    step = iostep(in_cabin = [1,2,3,4,5,6,7], out_cabin = [2,4,6,5,3,7,1])
    print(step)
    step = iostep(in_cabin = [1,2,3,4,5], out_cabin = [3,4,1,2,5])
    print(step)#[]
    step = iostep(in_cabin = [1,2,3,4,5], out_cabin = [5,4,3,2,1])
    print(step)
    step = iostep(in_cabin = [1,2,3,4,5,6], out_cabin = [2,3,5,4,1,6])
    print(step)   
