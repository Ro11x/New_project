name=[]
def func():
        i=0
        while i < 3:

                cars={}
                brand = (input("veedi"))
                model = input('veedi')
                god = input('veedi')

                cars['marka'] = brand
                cars['model'] = model
                cars['god'] = god
                name.append(cars)
                i+=1
        print(name[0])
        print(name[1])
        print(name[2])
func()