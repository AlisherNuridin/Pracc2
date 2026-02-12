# multiple_inheritance.py

# Первый родительский класс
class Father:
    def skills(self):
        return "Gardening, Programming"

# Второй родительский класс
class Mother:
    def skills(self):
        return "Cooking, Art"

# Класс-наследник, наследует от обоих родителей
class Child(Father, Mother):
    pass

# Создаём объект ребенка
child = Child()

# Вызываем метод skills()
print(child.skills())  # Gardening, Programming
