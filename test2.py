
def longest(s1, s2):
    al=[]
    a = (s1+s2)
    t=""
    print(''.join(sorted(al.append(s))) for s in a if s not in al)
    ''' for s in a:
        if(s in al):
            continue
        else:
            al.append(s)
            t = ''.join(sorted(al))
    return t  '''
def find_outlier(i):
    o=[]
    e=[]
    for j in i:
        if j == 0:
            continue
        if(j%2 != 0 or j == 1):
            o.append(j)
           # print(o)
        else:
            e.append(j)
           # print(e)
    if(len(e) > 2):
        print(int("".join(str(o).replace("[",'').replace("]",''))))
    else:
        print(int("".join(str(e).replace("[",'').replace("]",''))))
            
 



find_outlier([7,5,9,6,3,13,17])
find_outlier([2,6,8,10,12,1,12,66,14])   
#longest("aretheyhere", "yestheyarehere")