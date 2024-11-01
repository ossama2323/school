        
precipitation = []
listcity = []
listall = []

    
for i in range(0,4):

        prec = input("enter precipitation")
        city = input("enter city")

        precipitation.append(prec)
        listcity.append(city)

        if int(prec) < 30:
            danger = "green"
        else:
            danger = "red"     

        listall.append(city + prec + danger )
        
print(listall)






       

