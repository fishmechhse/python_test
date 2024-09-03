def subsets(lst):
    res_set = [[]]
    for x in lst:
        for i in range(len(res_set)):
            cp_list = res_set[i].copy()
            cp_list.append(x)
            res_set.append(cp_list)
    return iter(res_set)



lst = [1, 2, 30]
for subset in subsets(lst):
    print(subset)

print("-------------------")
gen = subsets(lst)
print(next(gen), next(gen))

