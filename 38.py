from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    step=[]
    
    for i in range(len(in_cabin)):
        step.push(i)
        step.printStack()
        
    for i in range(len(out_cabin)):
        step.pop()
        step.printStack()




if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)