from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def counter(request):
    text = request.POST["text"]
    words = text.split(" ")
    palindrome_words = []
    for word in words:
        if word == word[::-1]:
            palindrome_words.append(word)
    return render(request, 'counter.html', {'palindrome': palindrome_words})


def right(request):
    text = request.POST["text"]
    if text == 'right':
        return render(request, 'right.html')
def left(request):
    text = request.POST["text"]
    if text == 'left':
        return render(request, 'left.html')
def up(request):
    text = request.POST["text"]
    if text == 'up':
        return render(request, 'up.html')
def down(request):
    text = request.POST["text"]
    if text == 'down':
        return render(request, 'down.html')
