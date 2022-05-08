from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    l = len(in_cabin)  #找in_cabin的長度
    st = Stack(l)
    c = 0
    a = []
    t = 0
    while c < l:

        st.push(in_cabin[c]) #讓車進入車站
        a.append("push")

        while st.data[st.top] == out_cabin[t]: #有可能有兩個以上的車可以pop出來，因此用while迴圈

            st.pop()
            a.append("pop")

            t += 1
            if t == l:
                break
        c += 1

    while t < l:   #為了防止前面的while做完之後還有剩餘的車廂在車站中
        if st.data[st.top] == out_cabin[t]:  #有一樣就繼續pop出來
            st.pop()
            a.append("pop")
            t += 1
        else :   #沒有一樣代表堆疊錯誤了，直接讓a=[]
            a=[]
            break

    if len(a) != l*2: #完整的堆疊會有跟l一樣多的push跟pop所以是兩倍
        a = []
    return a


if __name__ == "__main__":
    step = iostep([1, 2, 3], [2, 1, 3])
    print(step)