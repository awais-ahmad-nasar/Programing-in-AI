import pandas as pd
#GroupBy matlab


var = pd.DataFrame({
    "name":['a','b','c','a','b','a','b','c'],
    "s1":[12,13,14,13,16,17,18,19],
    "s2":[32,23,24,25,26,7,28,29],
})
# print(var)
# print('================')
#ans1 = var.groupby('name')
# print(ans1)
# lst = list(ans1)
# print(lst)
#
# print('================')
ans1 = var.groupby('name')
# g_a = ans1.get_group("c")
# print(g_a)
# #
# print('=======min=========')
print(ans1.min())

# # print(ans1.max())
#
#
# # print(ans1.mean())
#
# print('================')
#
# print('================')
# for g,m in ans1:
#     print(g)
#     print(type(g))
#     print(m)
#     print(type(m))
#     print()
#
# # print('====only====')
# # d = [g for g,m in ans1]
# # print(d)