list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

common_elements = set1.intersection(set2)

if len(common_elements) == 0:
    print("Lists share no common elements.")
else:
    print("Lists share Common elements : ", common_elements)    