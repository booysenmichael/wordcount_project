from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request,'home.html')


def eggs(request):
    return HttpResponse('<h1>We have Eggs</h1>')

def count(request):
    fullText = request.GET['fullText']
    wordList = fullText.split()

    wordDict = {}

    for word in wordList:
        if word in wordDict:
            wordDict[word]+=1
        else:
            wordDict[word] = 1

    wordList = wordDict.items()
    sortedWords = sorted(wordList, key=operator.itemgetter(1),reverse=True)


    return render(request,'count.html',{'fullText':fullText,'wordCount':len(wordList),'commonWord':sortedWords})