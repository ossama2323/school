def max_value():
    mac_value = 0
    list = [1,12,20,32,76,978,1020]
    for value in list:
        if value > mac_value:
            mac_value = value
    return str(mac_value)
    

print(max_value())