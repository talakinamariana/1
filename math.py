def solve_equation(a, b, c):
# если a = 0, это уже не квадратное уравнение 
 if abs(a) > 10000 or abs(b) > 10000 or abs(c) > 10000:
  return "ошибка: значение вне допустимого диапозона."
 if  a == 0:
  return "ошибка: коэффицент a  не должен быть равен 0, если это все-таки квадратное уравнение."
 D = b * b - 4 * a * c
 if b == 0:
    return "нет решений" if c != 0 else "бесконечное множество"
 return f"линейное уравнение: x = {-c / b:.2f}"
 D = b ** 2 - 4 * a * c
 if D > 0:
  x1 = (-b + math.sqrt(D)) / (2 * a)
  x2 = (-b - math.sqrt(D)) / (2 *  a)
  return f"два корня: x1 = {x1:.2f}, x2 = {x2:.2f}"
 elif D == 0:
  x = -b / (2 * a)
  return f"один корень: x = {x::.2f}"
  return f"один корень: x = {x:.2f}"
 def main():
  print("решение квадраного уравнения: a* x^2 + b * x + c =0")
  print("решение квадраного уравнения: a* x ** 2 + b * x + c =0")
# простой вввод с базовой проверкой числа
try:
  a = float(input("введите a: "))
  b = float(input("введите b: "))
  c = float(input("введите c: "))
except ValueError:
 print("нужно вставить числа.") 
result =  solve_equation(a, b, c)
print(result)
