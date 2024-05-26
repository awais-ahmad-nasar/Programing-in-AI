import pandas as pd
#All arrays must be of the same length.coz if B has 5 and other B has 4 it casue Error in merge

# var1 = pd.DataFrame({"A":[1,2,3,4,5],"B":[11,12,13,14,15]})
# var2 = pd.DataFrame({"A":[51,21,31,4,1],"B":[21,22,23,24,25]})

# var3 = pd.merge(var1,var2,on='B')     #Out:only common values on all same name columns
# print(var3)     #same values ko ouput ma show kere ga

#print('+++++++++++++++++')
# var3 = pd.merge(var1,var2,left_index=True,right_index=True)
# print(var3)

# print('+++++++++++++++++')
# var3 = pd.merge(var1,var2,left_index=True,right_index=True,suffixes=['_Var1','_Var2'])
# print(var3)
#print("..OR...")
# var3 = pd.merge(var1,var2,left_index=True,right_index=True,suffixes=["_X","_Y"])
# print(var3)


var1 = pd.DataFrame({"B":[1,2,3,4,5],"A":[11,12,13,14,15]})
var2 = pd.DataFrame({"B":[1,2,3,4,6],"C":[12,11,23,24,25]})

# var3 = pd.merge(var1,var2) #only common values on all same name columns
# print(var3)
# print("..OR...")
# var3 = pd.merge(var1,var2,on='B')  #only common values
# print(var3)

# print('========INNER=========')
# var3 = pd.merge(var1,var2,on='B',how='inner')
# print(var3)
# print('========LEFT=========')
# var3 = pd.merge(var1,var2,on='B',how='left')
# print(var3)
# print('========RIGHT=========')
# var3 = pd.merge(var1,var2,on='B',how='right')
# print(var3)
# print('=========OUTER========')
# var3 = pd.merge(var1,var2,on='B',how='outer')
# print(var3)

#
#print('=================')
var1 = pd.DataFrame({"B":[1,2,3,4,5],"A":[11,12,13,14,15],"D":[101,102,103,104,105]})
var2 = pd.DataFrame({"B":[1,2,3,4,6],"C":[12,11,23,24,25],"A":[11,12,23,24,25]})

var3 = pd.merge(var1,var2,on=['A','B'])#Out:only common values
print(var3)

print('========INNER=========')
var3 = pd.merge(var1,var2,how='inner')
print(var3)
print('========LEFT=========')
var3 = pd.merge(var1,var2,how='left')
print(var3)
print('========RIGHT=========')
var3 = pd.merge(var1,var2,how='right')
print(var3)
print('=========OUTER========')
var3 = pd.merge(var1,var2,how='outer')
print(var3)

print('=========')
var3 = pd.merge(var1,var2,how='outer',indicator=True)
print(var3)







