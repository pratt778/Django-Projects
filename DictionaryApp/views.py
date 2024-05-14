from django.shortcuts import render
import requests
from bs4 import BeautifulSoup 
from PyDictionary import PyDictionary


def login(request):
   return render(request,'dicthome.html')

def wordSearch(request):
   word = request.GET.get('word')
   
   dictionary = PyDictionary()
   meanings = dictionary.meaning(word)
   antonym = dictionary.antonym(word)
   synonyms = dictionary.synonym(word)
   word = word.capitalize()
   
    
   data={'word':word,'meaning':meanings,'antonyms':antonym,'synonyms':synonyms}
   return render(request,'word.html',data)