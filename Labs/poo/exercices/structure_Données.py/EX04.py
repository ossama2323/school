def deplacer_zero(list_num):
        result = [x for x in list_num if x != 0]
        result.extend([0] * (len(list_num) - len(result)))
        return result
        
list_num = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 4, 0, 0, 2, 9, 7, 1]

print(deplacer_zero(list_num))
