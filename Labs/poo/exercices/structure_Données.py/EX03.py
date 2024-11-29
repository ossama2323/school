def permute():
    
    for i in range(0,len(liste)-1, 2):

        liste[i], liste[i + 1] = liste[i + 1], liste[i]
        print(i)

liste =  ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo',
'Violet']
permute()
print(liste)
