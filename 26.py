from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    index_out = 0  #對 list_in.data 與 lst_in.data 的值
    k = 0  #從 in_cabin 放入的 element 的 index
    lst_in = Stack(len(in_cabin))
    lst_out = []
    ans = [] #紀錄 'pop' 和 'push'
    
    for i in range(len(in_cabin)*2):
        if lst_in.data[lst_in.top] == out_cabin[index_out]:
            out = lst_in.pop()
            lst_out.append(out)
            index_out += 1
            ans.append("pop")

        else:
            try:
                lst_in.push(in_cabin[k])
            except IndexError:
                return []
            ans.append("push")
            k += 1
    return ans




if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)