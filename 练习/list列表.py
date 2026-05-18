# list1 = ['M', 'A', 'R', 'N', 'L', 'K', 'G', 'D', 'E']
# list2 = ['Z', 'X', 'C', 'A', 'F', 'E', 'G']
# list3 = ['B', 'X', 'D', 'S', 'A', 'W']
# #合并成列表，去除重复元素，排序，输出到控制台
# list_all = list1 + list2 + list3
#
# new_list = []
#
# for num in list_all:
#     if num not in new_list:
#      new_list.append(num)   #在new里添加num
# new_list.sort()             #排序
# print(new_list)

#
# lst = list(range(1,31))
# print(lst)
# list2 = [i**2 for i in lst if i % 3 == 0 or i % 5 == 0] #列表名称 = [要插入的数据（比如要平方就i**2）for i in if 条件]
# print(list2)
#


list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
list2 = [i for i in list1 if i>0]
list2.sort()
list2.reverse()
print(list2)






