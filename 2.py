from PIL import Image
from random import randint
from os import system
from os.path import exists

class Img:
	def __init__(self, title):
		self.title = title
		self.img = Image.open(f"./{self.title}.jpg")
		self.w = self.img.size[0]
		self.h = self.img.size[1]
		self.px = self.img.load()

	def save(self, effect):
		self.img.save(f"{self.title}_{effect}.jpg", "JPEG")
		print('\n')
		print(f'Новый файл сохранён под именем \"{self.title}_{effect}.jpg\"')
		self.img.show()

	def sepia(self):
		power = powerInput(0, 10, 'Введите величину наложения сепии (от 0 до 10): ')
		for x in range(self.w):
			for y in range(self.h):
				r, g, b = self.img.getpixel((x, y))
				nr = 0.393 * r + 0.769 * g + 0.189 * b
				ng = 0.349 * r + 0.686 * g + 0.168 * b
				nb = 0.272 * r + 0.534 * g + 0.131 * b
				nr = r+abs(nr-r)*(power/10) if nr > r else r-abs(nr-r)*(power/10)
				ng = g+abs(ng-g)*(power/10) if ng > g else g-abs(ng-g)*(power/10)
				nb = b+abs(nb-b)*(power/10) if nb > b else b-abs(nb-b)*(power/10)
				self.px[x, y] = (int(nr),int(ng),int(nb))
		self.save(f"sepia_{power}")

	def noise(self):
		power = powerInput(0, 10, 'Введите силу шума (от 0 до 10): ')
		for x in range(self.w):
			for y in range(self.h):
				r, g, b = self.img.getpixel((x,y))
				nr = int(r * (1 + randint(-1, 1) * power/10) )
				ng = int(g * (1 + randint(-1, 1) * power/10) )
				nb = int(b * (1 + randint(-1, 1) * power/10) )
				self.px[x,y] = (nr,ng,nb)
		self.save(f"noise_{power}")

	def gray(self):
		power = powerInput(0, 10, 'Введите величину наложения эффекта оттенков серого (от 0 до 10): ')
		for x in range(self.w):
			for y in range(self.h):
				r, g, b = self.img.getpixel((x, y))
				sr = (r + g + b) // 3
				nr = r+abs(sr-r)*(power/10) if sr > r else r-abs(sr-r)*(power/10)
				ng = g+abs(sr-g)*(power/10) if sr > g else g-abs(sr-g)*(power/10)
				nb = b+abs(sr-b)*(power/10) if sr > b else b-abs(sr-b)*(power/10)
				self.px[x, y] = (int(nr),int(ng),int(nb))
		self.save(f"gray_{power}")

	def brightness(self):
		power = powerInput(-10, 10, 'Введите величину уменьшения/увеличения яркости (от -10 до 10): ')
		for x in range(self.w):
			for y in range(self.h):
				r, g, b = self.img.getpixel((x,y))
				nr = int(r * (1+power/10))
				ng = int(g * (1+power/10))
				nb = int(b * (1+power/10))
				self.px[x,y] = (nr,ng,nb)
		self.save(f"brightness_{power}")

	def negative(self):
		for x in range(self.w):
			for y in range(self.h):
				r, g, b = self.img.getpixel((x,y))
				self.px[x,y] = (255 - r, 255 - g, 255 - b)
		self.save("negative")

	def bw(self):
		power = powerInput(0, 10, 'Введите силу эффекта (от 0 до 10): ')
		for x in range(self.w):
			for y in range(self.h):
				r, g, b = self.img.getpixel((x,y))
				if (r + g + b) // 3 < 255 * power/10:
					self.px[x,y] = 0, 0, 0
				else:
					self.px[x,y] = 255,255,255
		self.save(f"bw_{power}")


def router(obj, choose):
	if choose == 1:
		obj.sepia()
	elif choose == 2:
		obj.gray()
	elif choose == 3:
		obj.noise()
	elif choose == 4:
		obj.brightness()
	elif choose == 5:
		obj.negative()
	elif choose == 6:
		obj.bw()
filters = ['1. Сепия','2. Оттенки серого','3. Шум','4. Яркость','5. Негатив','6. Ч/б',]

def printFilters():
	print('\n')
	print('Доступные фильтры:')
	for n in filters:
		print(n)

def chooseFilter():
	while True:
		try:
			choose = int(input('Выберите номер фильтра: '))
			if choose >= 1 and choose <= 6:
				return choose
			else:
				print('Введите номер фильтра (1-6)')
		except ValueError:
			print('Введите номер фильтра (1-6)')

def titleInput():
	while True:
		print('Введите "exit", чтобы выйти')
		title = input('Название файла: ')
		if exists(f"./{title}.jpg"):
			return title
		elif title == 'exit':
			exit()
		else:
			print(f'Файл с именем {title}.jpg не найден')

def powerInput(a, b, message):
	warn = lambda: print(f'Введено неверное значение.')
	while True:
		try:
			power = int(input(message))
			if power < a or power > b:
				warn()
			else:
				return power
		except ValueError:
			warn()

def control():
	first = True
	while True:
		title = titleInput()
		obj = Img(title)
		printFilters()
		print('\n')
		choose = chooseFilter()
		router(obj, choose)

if __name__ == '__main__':
	control()