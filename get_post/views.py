from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):

    djtext = request.POST.get('text', 'default')#USE POST INSTEAD OF GET
    #cross site request frogery csrf

    uppercase = request.POST.get('uppercase', 'off')
    removepunc = request.POST.get('removepunc', 'off')
    removeline = request.POST.get('removeline', 'off')
    removespace = request.POST.get('removespace', 'off')

    djtext = djtext.strip(' ')
    if removespace == 'on':
        mtext = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' ' and djtext[index+1]== ' '):
                mtext += char
        djtext = mtext
    if uppercase == 'on':
        mtext = ''
        for char in djtext:
            mtext += char.upper()
        djtext = mtext
    
    if removepunc == 'on':
        mtext = ''
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                mtext += char
        djtext = mtext
    if removeline == 'on':
        mtext = ''
        for char in djtext:
            if char !='\n' and char !='\r':
                mtext += char
        djtext = mtext
    if (removepunc != 'on' and removeline != 'on' and removespace != 'on' and uppercase != 'on'):
        return HttpResponse("Error")

    params = {'detail':"Your text",'ytext':djtext}
    return render(request, 'analyze.html',params)