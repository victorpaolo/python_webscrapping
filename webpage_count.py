# -*- coding: utf-8 -*-
import urllib.request
import sys
from bs4 import BeautifulSoup
from collections import Counter

link_search = urllib.request.urlopen('https://mizukuki.eu/').read().decode()

infoLink = BeautifulSoup(link_search)
inText = infoLink.get_text()
print(len(inText))

textLowerCase = inText.lower()
splitText = textLowerCase.split()

deleteElements = ['a','la','de','en','el','las','los','por','y','que','con','un','qué','una','o','-','para','cookies','se','su','lo','del','sobre','sin','es','más','tu','al','no','como']
textDeleted  = [word for word in splitText if word.lower() not in deleteElements]

Counter = Counter(textDeleted)
most_occur = Counter.most_common(10)
print(most_occur)