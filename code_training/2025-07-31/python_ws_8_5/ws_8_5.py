# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0
    def __init__(self):
        pass

class Dog(Animal):
    def __init__(self):
        super().__init__()

    def sound(self):
        return "멍멍"
  

class Cat(Animal):
    def __init__(self):
        super().__init__()

    def sound(self):
        return "야옹"


class Pet(Cat, Dog):
    def __init__(self):
        pass

    def play(self):
        print("애완동물과 놀기")

    def __str__(self):
        super().sound()
        return f"애완동물은 {self.sound()} 소리를 냅니다."

my_pet = Pet()
print(my_pet)