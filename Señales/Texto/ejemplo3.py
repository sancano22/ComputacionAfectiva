#tokenizar texto
import nltk
from nltk.tokenize import sent_tokenize
#from nltk.tokenize import word_tokenize
#nltk.download('punkt')

mytext = "Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude."

print(sent_tokenize(mytext))

#print(word_tokenize(mytext))