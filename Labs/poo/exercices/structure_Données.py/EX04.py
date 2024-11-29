def deplacer_zero():
    for i in range(0, len(list_num)):
        if list_num[i] == 0:
            x = list_num.pop(i)
            list_num.append(x)
        
list_num = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 4, 0, 0, 2, 9, 7, 1]

deplacer_zero()
print(list_num)