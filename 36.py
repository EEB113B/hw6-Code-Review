from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    index_out = 0   #傳入lst_push的值
    take = 0        #從in_cabin裡拿出的物件的index
    lst_push = Stack(len(in_cabin))   #代表準備進站的物件的list
    lst_pop = []                      #代表已出站的物件的list
    stepp = []                        #記錄進站push跟出站pop

    for i in range(len(in_cabin)*2):

        if lst_push.data[lst_push.top] == out_cabin[index_out]:
            out = lst_push.pop()
            lst_pop.append(out)
            index_out +=1
            stepp.append('pop')   #加入紀錄:進站

        else:
            #用try...except避免程式遇到bug就終止
            try:
                lst_push.push(in_cabin[take])
            except IndexError:
                return []          #不成立就return一個空list

            stepp.append('push')   ##加入紀錄:出站
            take +=1

    return stepp


if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)