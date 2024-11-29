def supp_pre():
    list_element_supp = []
    for i in range(0, len(list)):
        if list[i] > list[i - 1]:
            list_element_supp.append(list[i])
    return list_element_supp

list = [11, 8, 85, 4, 6, 3, 45, 9, 5, 47]

print(supp_pre())