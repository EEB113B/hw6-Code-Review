from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    in_len = len(in_cabin) #找出in_cabin 長度
    out_len = len(out_cabin) #找出out_cabin 長度
    stack_list = [] #設push & pop list
    if in_len > out_len:   #找出較長的list,並將它設為stack的長度
        in_out_list = Stack(in_len)
        length = in_len
    else:
        in_out_list = Stack(out_len)
        length = out_len
    
    while length > 0:   
        if in_cabin != []:  #只要in_cabin中含有元素，
            in_out_list.push(in_cabin[0])#將那一元素push到stack中
            stack_list.append("push") #在push & pop list 中加入push
            del in_cabin[0] #將那一元素從in_cabin中刪除
        if in_out_list.top >= 0:
            while out_cabin != [] and in_out_list.data[in_out_list.top] == out_cabin[0]: #如果stack的頭與out_cabin的第一元素相同且out_cabin還有元素時
                stack_list.append("pop")# 在push & pop list中加入pop
                del out_cabin[0] #將那一元素從out_cabin中刪除
                in_out_list.pop()#將那一元素從stack中pop出去
                length -= 1 
        if in_cabin == [] and out_cabin != []: #如果in_cabin所有元素都已加入stack中，但out_cabin中還有元素時
            return [] #回傳空list(無法以排列方式pop出去)

    return stack_list #回傳push & pop list

if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3, 4, 5], out_cabin = [3,4,1,2,5])
    print(step)