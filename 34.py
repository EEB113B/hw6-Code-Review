from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    
    index_out= 0  #list_in.data和lst_in.data的值
    take = 0 #in_cabin放入的element的index
    lst_in=Stack(len(in_cabin))
    lst_out=[] #建立空字串來放取出來的element
    record=[] #列出push和pop

    for i in range(len(in_cabin)*2):
        if lst_in.data[lst_in.top] == out_cabin[index_out]:
            out = lst_in.pop()
            lst_out.append(out)
            index_out += 1
            record.append('pop')
        else:
            try:
                lst_in.push(in_cabin[take])
            except IndexError:  #順序不對會回傳空字串
                return []
            record.append('push')
            take+=1

    return record



if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3,4,5], out_cabin = [3,4,1,2,5])
    print(step)