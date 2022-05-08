from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    step_list = []                         #建立需要回傳的list
    st = Stack(len(out_cabin))             #建立車站(Stack)
    k = 0                                  #參數k用於估算進站的數字
    m = 0                                  #參數m用於將push或pull加入step_list中
    for i in range(0,len(out_cabin)):      #檢查出戰順序的迴圈
        for j in range(k,len(out_cabin)):  #推進進佔順序的迴圈
            if out_cabin[i] >= in_cabin[j]:#若index i 的出站數字大於等於進站的index j就使其進站
                st.push(j)
                step_list.insert(m,"push")
                k = k+1
                m = m+1
            elif out_cabin[i] < in_cabin[j]:#若index i 的出站數字小於進站的index j就使Stack中的數字出站
                st.pop()
                step_list.insert(m,"pop")
                m = m+1
                break
    if st != 0:                            #若車站尚未清空，則將其清空並在step_list加入pop的字串
        st.pop()
        step_list.append("pop")
           
    return step_list
        
    
    
if __name__ == "__main__":
    step = iostep(in_cabin =  [1,2,3,4,5,6,7], out_cabin =  [2,4,6,5,3,7,1])
    print(step)