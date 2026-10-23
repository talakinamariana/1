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
 def parse flags(args):
 #разбирает аргументы вида -a 1 -b -3 -c -2. возвращает (a,b,c) или None
  values = {}
  i = 0
 while i < len(args):
   flag = args[i]
   if flag in ("-a", "-b", "-c"):
    if i+1 >= len(args):
     print(f"ошибка: после {flag} должно быть число")
     return None
    try:
     values[flag] = int(args[i+1])
    except ValueError:
     print(f"ошибка: {flag} должно быть целым числом")
     return None
    i+=2
    else:
            print(f"Неизвестный аргумент: {flag}")
            return None
    if not all(k in values for k in ("-a", "-b", "-c")):
        print("Ошибка: нужны все три параметра -a, -b, -c")
        return None
    return values["-a"], values["-b"], values["-c"]
def input_from_keyboard():
    try:
        a = int(input("Введите a: "))
        b = int(input("Введите b: "))
        c = int(input("Введите c: "))
        return a, b, c
    except ValueError:
        print("Нужно ввести целые числа.")
        return None
def main():
    args = sys.argv[1:]
    # Без аргументов или --help — справка
    if not args or args[0] in ("--help", "-h", "help"):
        show_help()
        return
    if args[0] != "solve":
        print(f"Неизвестная команда: {args[0]}")
        show_help()
        return
    # solve без флагов — ввод с клавиатуры
    if len(args) == 1:
        coefs = input_from_keyboard()
        if coefs is None:
            return
        a, b, c = coefs
    else:
        coefs = parse_flags(args[1:])
        if coefs is None:
            return
        a, b, c = coefs
    print(solve_equation(a, b, c))
if __name__ == "__main__":
    main()
