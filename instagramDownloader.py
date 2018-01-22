import ui
from urllib import request
from bs4 import BeautifulSoup
from PIL import Image
import datetime
import clipboard

fileName = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M:%S") + '.jpg'

def downloadFile(url):
	print ('Baixando imagem...')
	f = request.urlopen(url)
	htmlSource = f.read()
	soup = BeautifulSoup(htmlSource,'html.parser')
	metaTag = soup.find_all('meta', {'property':'og:image'})
	imgURL = metaTag[0]['content']
	request.urlretrieve(imgURL, fileName)
	print ('Imagem salva como: ' + fileName)

def clearClip():
	clipboard.set('')

def setImageClip():
	img = Image.open(fileName)
	img.show()
	clipboard.set_image(img)
	
def main():
	text = clipboard.get()
	downloadFile(text)
	clearClip()
	setImageClip()
	
if __name__ == '__main__':
	main()
