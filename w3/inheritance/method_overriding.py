# method_overriding.py

class Animal:
    def sound(self):
        return "Some generic animal sound"

class Dog(Animal):
    # Переопределяем метод sound() родительского класса
    def sound(self):
        return "Woof! Woof!"

class Cat(Animal):
    # Переопределяем метод sound() родительского класса
    def sound(self):
        return "Meow!"

# Создаем объекты
animal = Animal()
dog = Dog()
cat = Cat()

# Вызываем метод sound() для каждого объекта
print(animal.sound())  # Some generic animal sound
print(dog.sound())     # Woof! Woof!
print(cat.sound())     # Meow!
