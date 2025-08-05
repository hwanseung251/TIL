# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    def __init__(self):
        pass

class Cat(Animal):
    def __init__(self):
        super().__init__()
    
    def meow(self):
        print(f"야옹!")


cat1 = Cat()
cat1.meow()
