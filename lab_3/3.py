from PIL import Image
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
		print(f'Новый файл сохранён под именем \"{self.title}.jpg\"')
		self.img.show()

def folderInput():
	while True:
		print('Введите "exit", чтобы выйти')
		folder = input('Введите название папки, в которой нужно произвести обработку: ')
		if exists(f"./MMT_3/{folder}"):
			return folder
		elif folder == 'exit':
			exit()
		else:
			print(f'Папка с таким именем не найдена.')

def getTitle(folder):
    while True:
        for k in range (100):
            if exists(f"./MMT_3/{folder}/img_",k,".jpg"):
                title = (f"./MMT_3/{folder}/img_",k)
                return title
                print("yes")
                exit()
            else: print("no")


def main():
    first = True
    while True:
        folder = folderInput()
        title = getTitle(folder)
        obj = Img(title)
        obj.img.show()

if __name__ == '__main__':
	main()