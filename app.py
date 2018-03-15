#！_*_ coding:utf-8 _*_

l = [1,1,3,5,1,3]
def duplicate(lists):
    L=[]
    for i in lists:
        if i not in L:
            L.append(i)
    return L

print(duplicate(l))