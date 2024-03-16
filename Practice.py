l1=[2,3,4,5,6,78,9]
l2=[]
l2=list()
l2=[x for x in l1]
print(l2)
l3=[]
l3.extend(l1)
print(l3)


l4=[1,2,3,4,5,6,78,9]
l5=[x*2 for x in l4]
print(l5)

l4=[1,2,3,4,5,6,78,9]
l5=[x for x in l4 if x%2==1]
print(l5)


'''tuple ...................'''

t1=(1,2,3,4,5,6)
l1=list(t1)
l1.append(9)
t1=tuple(l1)
print(t1)


# l1.remove(222)#throws exception
# l1.discard(22222)#ignore.........



d1={"Name":"Aneeq","Age":20,"Gender":"male","Marks":[50,20,23,32,45,56]}
print(d1)

print(d1.keys())
print(d1.values())
print(d1["Age"])

d1.update({"Age":22})
print(d1)

d2={ }