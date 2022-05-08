from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    for i in in_cabin:
        if in_cabin[i] == push():
            return in_cabin['push']
        if in_cabin[i] == pop():
            return in_cabin['pop']
        else:
            return [] #無法用pop和push，回傳空集合



if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)