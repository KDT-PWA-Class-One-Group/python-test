def union_list (listA, listB):
    setA = set(listA)
    setB = set(listB)
    return setA.union(setB)

def count_dictionary (dictA, item):
    if item in dictA:
        dictA[item] += 1
    else :
        dictA[item] = 1