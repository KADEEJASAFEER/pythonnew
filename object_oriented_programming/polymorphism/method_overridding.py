class parent:
    def phone(self):
        print("parent have nokia")

class child(parent):
    def phone(self):
        print("i have iphone")

#c=child()
#c.phone()
p=parent()
p.phone()

#child class cant edit the parent method
# so child class creates same methos as parent class
# ie., child class overrides the parent class

