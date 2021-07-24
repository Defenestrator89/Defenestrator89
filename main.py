d_from = 0
d_to = 4
max_danger = float(input('Максимально допустимый уровень опасности'))

depth = d_from + (d_to - d_from) / 2
danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10

if max_danger < 0:
  print('Ошибка, максимальный допустимый уровень опасности должен быть больше нуля.')
else:
  print('Глубина', depth, 'Уровень опасности', danger)
  while abs(danger) > max_danger:
    if danger > 0:
      d_from = depth
    else:
      d_to = depth
    depth = d_from + (d_to - d_from) / 2
    danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
    print('Глубина', depth, 'Уровень опасности', danger)

print('Приблизительная глубина безопасной кладки:', depth)
