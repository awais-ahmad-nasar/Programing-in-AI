import pandas as pd

df = pd.DataFrame({"years":[2010,2011,2012,2013,2014],"income":[100,200,120,300,400],"expense":[10,20,30,20,50]})
print(df)

print('=====melt-----')
var = df.melt()
print(var)

print('=====melt with Id-----')
var = df.melt(id_vars=['years'],var_name='income/expense',value_name='amount(Rs)')
print(var)

#setting for pivot
df = pd.DataFrame({"years":[2010,2011,2012,2013,2014],"person":['A','B','A','B','B'],"income":[100,200,120,300,400],"expense":[10,20,30,20,50]})
print(df)
# print('====pivit-----')
# var = df.pivot(index='years',columns='person')
# print(var)
#
# print('====pivit-----')
# var = df.pivot(index='years',columns='person',values='income')
# print(var)
#
# print('====data-----')
# df = pd.DataFrame({"years":[2010,2011,2010,2010,2011],"person":['A','B','A','B','A'],"income":[100,200,120,300,400],"expense":[10,20,30,20,50]})
# print(df.pivot_table(index='person',columns='years',aggfunc='mean')) #sum,count
# print(df.pivot_table(index='person',columns='years',aggfunc='count',margins=True)) #sum,count