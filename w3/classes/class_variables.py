class Cat:
    # Переменная класса (общая для всех котов)
    species = "Felis catus"

    def __init__(self, name):
        # Переменная экземпляра (у каждого кота своя)
        self.name = name

# Создаем котов
cat1 = Cat("Murka")
cat2 = Cat("Tom")

# Доступ к переменной класса
print(cat1.species)  # Felis catus
print(cat2.species)  # Felis catus

# Доступ к переменной экземпляра
print(cat1.name)     # Murka
print(cat2.name)     # Tom

# Изменим переменную класса через сам класс
Cat.species = "Domestic Cat"
print(cat1.species)  # Domestic Cat
print(cat2.species)  # Domestic Cat
