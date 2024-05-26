import pandas as pd

# var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
# var2 = pd.DataFrame({"C":[1,2,3,4,6],"D":[21,22,23,24,25]})
#
# var3 = var1.join(var2)
# print(var3)



# var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]},index=['a','b','c','d','e'])
# var2 = pd.DataFrame({"C":[1,2,3],"D":[21,22,23]},index=['a','b','c'])
# v=var2.join(var1)
# print(v)
#
# print('======left========')
#
# v=var1.join(var2,how="left")
# print(v)
#
# print('=======right=======')
#
# v=var1.join(var2,how="right")
# print(v)
#
# print('=======inner=======')
#
# v=var1.join(var2,how="inner")
# print(v)
#
# print('======Outer========')
#
# v=var1.join(var2,how="outer")
# print(v)

#
var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]},index=['a','b','c','d','e'])
var2 = pd.DataFrame({"A":[1,2,3],"C":[21,22,23]},index=['a','b','c'])
v=var1.join(var2,how="inner",lsuffix="_l",rsuffix='_r')
print(v)

print('=======append=======')

#Append is suitable for same column values
v = var1._append(var2,ignore_index=True)
print(v)