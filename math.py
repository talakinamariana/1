#вывод справки 
def show_help():
 print("программа решает уравнение вида a*x^2 + b*x + c = 0")
 print("как использовать")
 print("python math.py         # показать српавку")
 print("python math.py  --help # показать справку")
 print("python math.py   solve # ввести коэффиценты с клавиатуры")
 print("python math.py   solve -a 1 -b -3 -c 2 # решить с заданными числами")
 print("числа джолжны быть целыми и быть не больше 10000 по модулю")
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
 else:
  return "нет действительных корней"
 def main():
  args = sys.argv[1:] #все аргументы после имени скрипта
  #обработка --help и пустого запуска 
  if len(args) == 0 or "--help" in args or args[0] == "":
   show_help()
   return
#обработка команды solve 
  if len(args) == 1:
# простой вввод с базовой проверкой числа
try:
  a = int(input("введите a: "))
  b = int(input("введите b: "))
  c = int(input("введите c: "))
# если нужно, чтобы считались не только целые, но и дробные числа, то нужно поменять int на float
except ValueError:
 print("нужно вставить целые числа.") 
result =  solve_equation(a, b, c)
print(result)
