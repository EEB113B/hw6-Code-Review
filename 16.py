from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    st=Stack(len(in_cabin))#將size傳入stack
    out_index=0#決定out執行到那個數字
    move=[""]*len(in_cabin)*2#用來放push和pop的字串
    st.push(in_cabin[0])#第一個數字進站
    in_index=1#進站次數
    move[0]="push"#第一個一定是push
    movetime=1#算目前push或pop到哪個位置
    while movetime<=len(in_cabin)*2-1:#執行次數必須要和in,out相加的長度一樣
        if  st.data[st.top]==out_cabin[out_index]:#如果最後一個數字和out所指定的出站數字一致的話即出站
            st.pop()
            out_index+=1
            move[movetime]="pop"
            movetime+=1
        else:#沒有出站的話就進站
            if in_index==len(in_cabin):#還有無法出站的數字即失敗
                break
            st.push(in_cabin[in_index])
            in_index+=1
            move[movetime]="push"
            movetime+=1
    if st.top==-1:#進站出站皆完成，車站回復原樣，正確
        return move
    else:
        return"[]"
            



if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3], out_cabin = [2,1,3])
    print(step)



#↓↓↓下面是不用stack的寫法↓↓↓
    #L = len(out_cabin)   #算長度
    #a = 1   #算目前in_cabin執行到哪個數字
    #c = ["a"]   #stack，由於下面執行時字串不能是空的，所以先放一個"a"
    #c.append(in_cabin[0])    #先讓第一個數字進站
    #s = ["push"]    #第一個一定是"push"
    #em =[]   #用來回傳的空list
    #errorr = 0   #判斷是否有錯
    #下面迴圈執行進站出站
    #for i in range(L):
        #for j in range(L):
            #if out_cabin[i] == c[-1]:
                #s.append("pop")
                #c.pop()   #符合題目要求就出站
                #break
            #else:
                #s.append("push")
                #try:   #如果不符合題目要求就會出現Error，所以進行檢查
                    #c.append(in_cabin[a])   #符合題目要求就進站
                #except IndexError:
                    #errorr += 1
                    #break    #有錯誤即跳出迴圈
                #a += 1
    #正確就回傳list
    #if errorr == 0:
        #return s
    #錯誤就回傳空list
    #else:
        #return em