import pandas as pd
import numpy as np


#Interpolate works with numbers only

var = pd.read_csv("/Users/admin/Documents/1.BIIT Courses/Fall23/Programming For AI/Stuff/sample2.csv")
print(var)

# var1 = var.interpolate(method='quadratic')
# print(var1)

# var1 = var.interpolate(method='linear',inplace=True)
# print(var)

#
# var1 = var.interpolate(method='linear',axis=0)#column wise
# print(var1)


# var1 = var.interpolate(method='linear',axis=1)#row wise
# print(var1)

# var1 = var.interpolate(limit=1)
# print(var1)

# var1 = var.interpolate(limit_direction="forward",limit=4)
# print(var1)

# var1 = var.interpolate(limit_direction="backward",limit=2)
# print(var1)

var1 = var.interpolate(limit_direction="both",limit=2)
print(var1)

# var1.dropna()
# var1.fillna()

# var1 = var.interpolate(limit_area="outside")
# print(var1)