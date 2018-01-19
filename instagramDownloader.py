import ui, appex
from urllib import request
from bs4 import BeautifulSoup
import datetime
import clipboard

def DownloadFile(url):
	print ('Downloading image...')
	f = request.urlopen(url)
	htmlSource = f.read()
	soup = BeautifulSoup(htmlSource,'html.parser')
	metaTag = soup.find_all('meta', {'property':'og:image'})
	imgURL = metaTag[0]['content']
	fileName = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + '.jpg'
	request.urlretrieve(imgURL, fileName)
	print ('Done. Image saved to disk as ' + fileName)
	
def main():
	text = clipboard.get()
	DownloadFile(text)
	
if __name__ == '__main__':
	main()
