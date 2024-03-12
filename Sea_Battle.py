# Морской бой 

# Интерфейс
'''
	  | 1 | 2 | 3 | 4 | 5 | 6|

	1 | О | О | О | О | О | О |

	2 | О | О | О | О | О | О |

	3 | О | О | О | О | О | О |

	4 | О | О | О | О | О | О |

	5 | О | О | О | О | О | О |

	6 | О | О | О | О | О | О |
'''

# Количество кораблей на доске у ии и у игрока: 
# 1 кор. - 3 клетки, 2 кор. - 2 клетки, 4 кор. - 1 клетка 

gui = [ ' ', ' | ',  '1', ' | ', '2', ' | ', '3', ' | ', '4', ' | ', '5', ' | ', '6', ' | \n\n',
		'1', ' | ',  'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | \n\n'
		'2', ' | ',  'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | \n\n',
		'3', ' | ',  'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | \n\n',
		'4', ' | ',  'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | \n\n',
		'5', ' | ',  'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | \n\n',
		'6', ' | ',  'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | ', 'О', ' | \n']

# Функция вывода доски на экран 
'''
def print_gui():
	for i in range(97):
		print(gui[i], end = "")
		i+=1
'''

class Board():
	def __init__(self, oy, ox):
		self.oy = 6
		self.ox = 6 

	def input():
		for i in range(97):
			print(gui[i], end = "")
			i+=1 

class Dots():
	x_cord = 0
	y_cord = 0

	pass


class Exception(): 
	def check(): 
		if user_enter > 6 or user_enter < 6: 
			print("BoardOutException")
			print("Вы вышли за пределы поля!")
	pass
		

class Ship():
	def __init__(self, length, dot, horizontal, vertical, life):
		self.length
		self.dot 
		self.horizontal 
		self.vertical 
		self.life

	def dots():
		pass
	pass



Board.input()