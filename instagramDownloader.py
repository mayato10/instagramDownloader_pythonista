import ui
from urllib import request
from bs4 import BeautifulSoup
import datetime
import clipboard

def DownloadFile(url):
	print ('Baixando imagem...')
	f = request.urlopen(url)
	htmlSource = f.read()
	soup = BeautifulSoup(htmlSource,'html.parser')
	metaTag = soup.find_all('meta', {'property':'og:image'})
	imgURL = metaTag[0]['content']
	fileName = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + '.jpg'
	request.urlretrieve(imgURL, fileName)
	print ('Imagem salva como: ' + fileName)
	
def clearClip():
	clipboard.set('')
	
def main():
	text = clipboard.get()
	DownloadFile(text)
	clearClip()
	
if __name__ == '__main__':
	main()
