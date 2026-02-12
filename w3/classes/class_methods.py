class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

#class Calculator:
    #def add(self, a, b):
        #eturn a + b

    #def multiply(self, a, b):
        #return a * b

# Создаём объект калькулятора
#calc = Calculator()

# Ввод чисел пользователем
#num1 = int(input("Введите первое число: "))
#num2 = int(input("Введите второе число: "))

# Используем методы класса с введёнными числами
#print("Сумма:", calc.add(num1, num2))
#print("Произведение:", calc.multiply(num1, num2))