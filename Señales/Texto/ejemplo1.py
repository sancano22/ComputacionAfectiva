import nltk
#nltk.download()
from bs4 import BeautifulSoup
import urllib.request

response = urllib.request.urlopen('http://php.net/')

html = response.read()

#limpiar texto (pre-procesamiento de la señal)
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
tokens = [t for t in text.split()]
#print (tokens)

freq = nltk.FreqDist(tokens)

for key,val in freq.items():
    print (str(key) + ':' + str(val))

freq.plot(20, cumulative=False)

