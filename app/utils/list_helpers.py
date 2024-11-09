def union_list (listA, listB):
    setA = set(listA)
    setB = set(listB)
    # 결과를 list로 변환하여 반환
    return list(setA.union(setB))

def count_dictionary (dictA, item):
    if item in dictA:
        dictA[item] += 1
    else :
        dictA[item] = 1