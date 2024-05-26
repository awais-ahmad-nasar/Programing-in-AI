import pandas as pd

# a = pd.Series([1,2,3,4,5])
# b = pd.Series([10,20,30,40,50])
# c = pd.concat([a,b])
# print(c)

# var = pd.DataFrame({"D":[111,222,322]})
# var0 = pd.DataFrame({"A":[1,2,3],"C":[11,12,13]})
# c = pd.concat([var,var0])
# print(c)

# print('==========')
# var1 = pd.DataFrame({"A":[1,2,3,4,5],"B1":[11,12,13,14,15]})
# var2 = pd.DataFrame({"A":[1,2,3,4,6],"B1":[21,22,23,24,25]})
# c = pd.concat([var1,var2])
# print(c)


# var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
# var2 = pd.DataFrame({"A":[1,2,3,4,6],"B1":[21,22,23,24,25]})
# c = pd.concat([var1,var2])
# print(c)


# var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
# var2 = pd.DataFrame({"A":[1,2,3],"B1":[21,22,23]})
# c = pd.concat([var1,var2],axis=0)
# print(c)


# var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
# var2 = pd.DataFrame({"A":[1,2,3],"B1":[21,22,23]})
# c = pd.concat([var1,var2],axis=1)
# print(c)


var0 = pd.DataFrame({"A":[1,2,3],"C":[11,12,13]})
var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
var2 = pd.DataFrame({"A":[1,2,3],"B1":[21,22,23]})
var = pd.DataFrame({"D":[111,222,322]})
# c = pd.concat([var0,var2],axis=1)
# print(c)
# print(">>>>>>>>>>>>>OUTER>>>>>>>>>>>>>>>>>>>")
# c = pd.concat([var0,var2],axis=1,join='outer')
# print(c)
# print(">>>>>>>>>>>>>>INNER>>>>>>>>>>>>>>>>>>")
# c = pd.concat([var0,var2],axis=1,join='inner')
# print(c)


# c = pd.concat([var1,var2],keys=["K1","K2"])
# print(c)

# c = pd.concat([var1,var2],axis=1,keys=["Variable1","Variable2"])
# print(c)
#

# c = pd.concat([var,var1,var2],axis=0)
# print(c)


print(".............AXIS=0............")
c = pd.concat([var,var1,var2],axis=0,keys=["K1","K2","K3"])
print(c)
print(".............AXIS=1............")
c = pd.concat([var,var1,var2],axis=1,keys=["K1","K2","K3"])
print(c)