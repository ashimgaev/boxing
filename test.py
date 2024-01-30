

vals = [9,9,7,6,5,4,4,3,2]
#l1 = [i in range(0, len(vals))]
#print(l1)

#for i in range(0, len(vals)):
    #print(i)

def getComb3(in_list, max_sum):
    out = []
    for i1 in range(0, len(in_list)):
        x1 = in_list[i1]
        if x1 >= max_sum:
            continue
        for i2 in range(i1+1, len(in_list)):
            x2 = in_list[i2]
            my_sum = x1+x2
            if my_sum >= max_sum:
                continue
            for i3 in range(i2+1, len(in_list)):
                x3 = in_list[i3]
                my_sum = x1+x2+x3
                if my_sum != max_sum:
                    continue
                out.append([x1, x2, x3])
    return out

def getComb2(in_list, max_sum):
    out = []
    for i1 in range(0, len(in_list)):
        x1 = in_list[i1]
        if x1 >= max_sum:
            continue
        for i2 in range(i1+1, len(in_list)):
            x2 = in_list[i2]
            my_sum = x1+x2
            if my_sum != max_sum:
                continue
            out.append([x1, x2])
    return out


def removeFromList(in_list, to_remove):
    for val in to_remove:
        in_list.remove(val)
    return in_list

def getSum(in_list):
    out = 0
    for v in in_list:
        out = out+v
    return out

x1 = 5

vals = removeFromList(vals, [x1])

print(f'x2+x3={8+x1}')

x2_x3_comb = getComb2(vals, 8+x1)
#print(x1_x2_comb)
for x2_x3 in x2_x3_comb:
    x2, x3 = x2_x3
    tmp_vals = removeFromList(vals.copy(), x2_x3)
    x4_x5_x6_comb = getComb3(tmp_vals, 22-(x2+x3))
    for x4_x5_x6 in x4_x5_x6_comb:
        x7_x8_x9 = removeFromList(tmp_vals.copy(), x4_x5_x6)
        M = [*x2_x3, *x4_x5_x6]
        T = [x1, 8, *x7_x8_x9]
        print(f'{M} -> {getSum(M)} -> {getSum(M[1:])}')
        print(f'{T} -> {getSum(T)} -> {getSum(T[1:])}')
        print('###')