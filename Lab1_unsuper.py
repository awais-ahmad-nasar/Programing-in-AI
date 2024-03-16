'''
Task 1:
create a function that take a list and return count of pos , neg numbers?
'''

def funtion1(list):
    neg = 0
    pos = 0
    for i in list:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
    return pos,neg

l1=[-1,2,3,4,-5,6,7,8,-9,10]
pos,neg=funtion1(l1)
print("Positive numbers are : ",pos)
print("Negative numbers are : ",neg)


'''
Task 2:
create a function that take a number and return wether it is prime or not?
'''

def prime(num):
    if num%2==1:
        print("it is Prime Number")
    else:
        print("it is not Prime Number")
    return num

x=eval(input("Enter a Number"
))
print(prime(x))


'''
task 3

'''
# def updatedict(d):
#     print(d)
#     d.update({"stud4": 124})
#     print("Updated Dict : ",d)
#
#
# d2={"stud1":121,"stud2":122,"stud3":123}
# updatedict(d2)

#..............OR...............
def addinvalue(dict,k,v):
    value=dict[k]+v
    dict[k]=value
    return dict
d={"stud1":120,"stud2":122,"stud3":123}
print(d)
print(addinvalue(d,'stud1',1))

