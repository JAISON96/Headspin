
def arradd(l):
    n=int(input("enter the position to add the element"))
    e=int(input("enter the element"))

    list1=l[:n-1]
    list2=l[n-1:]
    list1+=[e]

    l=list1+list2

    print("The new array is :",l)

l1=[1,2,3,4,5,6]
print("The array is :",l1)

arradd(l1)
