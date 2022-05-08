from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    output = []
    out = 0
    st = Stack(len(in_cabin))
    for i in range(len(out_cabin)):
        st.push(in_cabin[i])
        output.append("push")
        while not st.isEmpty():
            if st.data[st.top] == out_cabin[out]:
                out=out+1
                st.pop()
                output.append("pop")
            else:
                break
    if st.isEmpty():
        return output
    else :
        output = []
        return output
                

            
            



    # 記得要 return，回傳值型態為 list
    return output



if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3, 4, 5], out_cabin = [3, 4, 1, 2, 5])
    print(step)