class Product:
    def __init__(self,id,name,category,price):
        self.id=id
        self.name=name
        self.category=category
        self.price=price

    def __str__(self):
        return self.name

lst=[]
ob=lst.append(Product(100,"lux","soap",20))
ob=lst.append(Product(101,"colgate","paste",50))
ob=lst.append(Product(103,"nike","shoe",1000))
#for item in lst:
#convert item name to uppercase
def con(name):
    return name.upper()
print(con("nike"))
a=lambda name:name.upper()
nmaelst=list(map(lambda Product:Product.name.upper(),lst))
print(nmaelst)
#list product name with price greate than 50
price=list(filter(lambda Product:Product.price>=50,lst))
for value in price:
    print(value)


