print("=" * 5, "Калькулятор", "="*5)
print ("введите q для выхода")
while True:
  s=input("Знак (+, -, /, *):  ")
  print("")
  if s== 'q': break
  if s in ('+', '-', '/', '*'):
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    if s=="+":
      print("%.2f"%(x+y))
    elif s=="-":
      print("%.2f"%(x-y))
    elif s=="/":
      if y!=0:
        print("%.2f"%(x/y))
      else:
        print("Деление на ноль")
    elif s=="*":
      print("%.2f"%(x*y))
  else:
    print("Ввели неккоректный знак")