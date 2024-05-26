import pandas as pd


var = pd.read_csv("/Users/admin/Documents/1.BIIT Courses/Fall23/Programming For AI/Stuff/sample2.csv")
print(var)

# var1 = var.replace(to_replace='F',value='D')
# print(var1)

# var1.replace(to_replace='F',value='D',inplace=True)
# print(var1)

# var1 = var.replace(to_replace=['F','C'],value='D',inplace=True)
# print(var1)

# var1 = var.replace(to_replace=['F','C'],value='D')
# print(var1)

# var1 = var.replace(['F','C'],'D')
# print(var1)

# var1 = var.replace(to_replace=['F','C'],value='D',inplace=True)
# print(var1)

# var1 = var.replace(to_replace="[A-Fa-z]",value="*",regex=True)
# print(var1)
#
# var1 = var.replace("[A-Za-z]","*",regex=True)
# print(var1)
#
#
# var1 = var.replace("[a-z]","*",regex=True)
# print(var1)

# var1 = var.replace({"Series_reference":"[1-9A-Za-z]"},"*",regex=True)
# print(var1)

# var1 = var.replace({"STATUS":"F"},"*")
# print(var1)

var1 = var.replace(1290.820, method='BFILL')#BFILL,FFILL,pad
print(var1)