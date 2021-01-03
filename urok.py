# вывести все числа не больше 100, которые делятся на 7
#for i in range(1,100):
    #if i % 7==0:
        #print("делиться", i ,"Без остатка на 7")

# Ильяр написал программу

#stroka= input("vedite")
#lesenka= ''
#for i in stroka:
   # if stroka.index(i)%2==0:
       # lesenka= lesenka + i.upper()
    #else:
       # lesenka = lesenka + i.lower()
#print(lesenka)

#c While = написать программу, которая конвертирует введенный текст в текст лесенкой


#stroka=input('Строка')
#lst = []
#i=0

#while i<len(stroka):
    #if i %2 == 0:
        #lst.append(stroka[i].upper())
    #else:
        #lst.append(stroka[i].lower())
    #i += 1
#print(''.join(map(str,lst)))


#или такой не известно

#stroka =input('Строка')
#i=0
#while i<len(stroka):
    #if i %2 == 0:
       #print(stroka[i].upper())#
    #else:
        #print(stroka[i].lower())
    #i += 1
i=0
stroka = input("вести: ")

lesenka = ''
while i < len(stroka):
    if i % 2 ==0:
        lesenka = lesenka + stroka[i].lower()
    else:
        lesenka= lesenka + stroka[i].upper()
    i += 1
print(lesenka)




