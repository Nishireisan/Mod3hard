def cal_list(res):
    first = res[0]
    print(type(res[0]))
    if isinstance(res[0], int):
        if len(res) <= 1:
            return first
        else:
            return first + cal_list(res[1:])
    elif isinstance(res[0], str):
        first += len(res[0])
    elif isinstance(res[0], dict):
        first += cal_dict(res[0])
    elif isinstance(res[0], tuple):
        return cal_tuple(res[0])
    elif isinstance(res[0], list):
        return first + cal_list(res[0])
    elif isinstance(res[0], set):
        return cal_set(res[0])
    return first


def cal_dict(d):
    first = 0
    for i in d:
        first += len(i)
        first += d[i]
    return first


def cal_tuple(t):
    first = 0
    for j in t:
        print(type(j))
        if j == ():
            continue
        if isinstance(j, int):
            first += j
        elif isinstance(j, str):
            first += len(j)
        elif isinstance(j, list):
            first += cal_list(j)
        elif isinstance(j, dict):
            first += cal_dict(j)
        elif isinstance(j, tuple):
            return first + cal_tuple(j)
        elif isinstance(j, set):
            return first + cal_set(j)
    return first


def cal_set(seeet):
    chis = 0
    seeet = list(seeet)
    return chis + cal_list(seeet)


def calculate_structure_sum(result):
    calc = 0
    for j in range(0, len(result)):
        print(result[j])
        print(type(result[j]))
        if isinstance(result[j], list):
            calc += cal_list(result[j])
            print(calc)
        elif isinstance(result[j], dict):
            calc += cal_dict(result[j])
            print(calc)
        elif isinstance(result[j], tuple):
            calc += cal_tuple(result[j])
            print(calc)
        elif isinstance(result[j], str):
            calc += len(result[j])
            print(calc)
        elif isinstance(result[j], int):
            calc += result[j]

    return calc


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(data_structure)
print(calculate_structure_sum(data_structure))
