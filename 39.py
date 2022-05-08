from ast import Continue, If
from stack_diy import Stack

def iostep(in_cabin, out_cabin):
    # <將你的程式碼寫在這裡>
    # 記得要 return，回傳值型態為 list
    stack=[]
    step=[]
    
    while in_cabin!=[] or stack!=[]:
        if stack==[]:
            a1=[in_cabin[0]]
            
            stack=stack[::]+a1
            in_cabin=in_cabin[1::]
            step+["push"]
        
        if stack[0:1:]==out_cabin[0:1:]:
            stack=stack[1::]
            step+["pop"]
            out_cabin=out_cabin[1::]
        else:
            a2=[in_cabin[0]]
            stack=a2+stack
            Continue

        if in_cabin==[] and stack[0]!=out_cabin[a]:
            step=[]
            return step
        if in_cabin==[] and stack==[]:
            return step

    
    


if __name__ == "__main__":
    step = iostep(in_cabin = [1, 2, 3], out_cabin = [2, 1, 3])
    print(step)