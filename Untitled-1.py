def check_point_position(x, y):
  if x == 0 and y == 0:
    return 
  elif x == 0:
    return 
  elif y == 0:
    return 
  elif x > 0 and y > 0:
    return 
  elif x < 0 and y > 0:
    return 
  elif x < 0 and y < 0:
    return 
  else:
    return 

# Ввод координат
x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))

# Вывод результата
print(check_point_position(x, y))