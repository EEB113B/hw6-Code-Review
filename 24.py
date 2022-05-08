from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list\

    index_out = 0
    take = 0                                        #從in_cabin放入的數值的index
    in_list = Stack(len(in_cabin))                  #車站(stack)的長度等於in_canbin的長度
    out_list = []                                   #取出的數值要放的地方
    re = []                                         #回傳pop和push

    for i in range(len(in_cabin)*2):

        if in_list.data[in_list.top] == out_cabin[index_out]:
            out = in_list.pop()
            out_list.append(out)
            index_out += 1
            re.append('pop')

        else:
            try:
                in_list.push(in_cabin[take])
            except IndexError:                       #順序有誤時，回傳空list
                return []
            re.append('push')
            take += 1

    return re

    

if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3], out_cabin = [2,1,3])
    print(step)