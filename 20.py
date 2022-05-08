from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    index_out = 0    #對list_in.data與lst_in.data的值
    take = 0   #從in_cabin放入的element的index
    lst_in = Stack(len(in_cabin))  
    lst_out = [] #拿出來element
    record = []  #紀錄push跟pop
    
    for i in range(len(in_cabin)*2):
        
                                   
        if lst_in.data[lst_in.top] == out_cabin[index_out]:                                    
            out  = lst_in.pop()
            lst_out.append(out)
            index_out+=1                       
            record.append('pop')
                                    
        else:                        
            try:
                lst_in.push(in_cabin[take])
            except IndexError:   #順序不對會出現錯誤
                return []
            record.append('push')                       
            take+=1
            
        
    
    return record
    

            


if __name__ == "__main__":
    step = iostep(in_cabin = [1,2,3], out_cabin =  [2,1,3])
    print(step)