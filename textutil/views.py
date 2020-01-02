# This file is created by me
from django.http import HttpResponse
from django.shortcuts import render
"""
# code for previous vedio

#def about(request):
    #return HttpResponse('<h2>About Ankur</h2> <a href="https://www.youtube.com/">Youtube</a>')
#def text(request): # read the text file through django
    #file=open("textutil/text1.txt",'r+')
    #return HttpResponse(file.read())
#def navbar(request): # for navigation bar
    #nav = '<h1>Navigation</h1> <ul> <li><a href="https://www.youtube.com/playlist?list=PL8p2I9GklV47fi-yiWkfRpbMV8PPaQDH4">Laravel Playlist</a></li> <li><a href="https://www.youtube.com/playlist?list=PLLgihBgNlnFS-cJ7j2-I6WvyQKuRNbqUT">Python By buildinggame</a></li> <li><a href="https://www.youtube.com/playlist?list=PLd3UqWTnYXOkY3Ajiydn_Ok9etnwVv8Hx">Django Rest API</a></li></ul>'
    #return HttpResponse(nav)
"""
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('<h2>Home</h2>')

def analyze(request):
    djtext=request.GET.get('text','off')
    print(djtext)
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analyzed = ""
    for char in djtext:
        if char not in punctuation:
            analyzed += char

    params = {'purpose': 'Removed from the text', 'analyzed_text': analyzed}

    return render(request, 'analyze.html', params)
#
# def cap(request):
#     return HttpResponse("capitalizefirst")
#
# def newlinerem(request):
#     return HttpResponse("newlineremove")
