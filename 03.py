from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    st=stack(len(in_cabin))
    out_index=0
    move[""]*len(in_cabin)*2
    st.pushlen(in_cabin[0])
    in_index=1
    move[0]="push"
    movetime=1
    while moveime<=len(in_cabin)*2-1:
        if st.data[st.top]==out_cabin[out_index]:
            st.pop()
            out_index+=1
            move[movetime]="pop"
            movetime+=1
        else:
            if in_index==len(in_cabin):
                break
            st.pushlen(in_cabin[in_index])
            in_index+=1
            move[movetime]="push"
            movetime+=1
        if st.top==-1:
            return move
        else:
            return"[]"

if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)