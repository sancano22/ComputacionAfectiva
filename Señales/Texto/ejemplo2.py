import nltk
#nltk.download()
from bs4 import BeautifulSoup
import urllib.request
from nltk.corpus import stopwords

#nltk.download('stopwords')

response = urllib.request.urlopen('http://php.net/')

html = response.read()

#limpiar texto (pre-procesamiento de la señal)
soup = BeautifulSoup(html,"html5lib")
text = soup.get_text(strip=True)
tokens = [t for t in text.split()]
#print (tokens)
#eliminar ciertas palabras
clean_tokens = tokens[:]
sr = stopwords.words('english')

for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)

for key,val in freq.items():
    print (str(key) + ':' + str(val))

freq.plot(20, cumulative=False)