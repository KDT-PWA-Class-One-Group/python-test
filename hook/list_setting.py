def union_list (listA, listB):
    setA = set(listA)
    setB = set(listB)
    return setA.union(setB)

def count_dictionary (dictA, item):
    if item in dictA:
        dictA[item] += 1
    else :
        dictA[item] = 1

def extract_top_5_list (listA) :
    """
    x:x[0] = key를 기준으로 정렬 
    x:x[1] = value를 기준으로 정렬
    x의 값은 어떤 값이 들어가도 상관 없다.
    """
    sorted_items = sorted(listA.items(), key=lambda x:x[1], reverse=True)
    result_list = []
    for item in sorted_items[:5]:
        typeCasting = { item[0] : item[1] }
        result_list.append(typeCasting)
    
    return result_list