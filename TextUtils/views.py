# created by me
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    d ={'name':'Ritik', 'from':'moon'}
    return render(request, 'index.html', d)

def analyse(request):
    djtext = request.POST.get('text','default')
    analyse_checkbox = request.POST.get('analyse','off')
    fullcaps = request.POST.get('caps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    
    if analyse_checkbox == 'on':
        punck= '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analysed=""
        for char in djtext:
            if char not in punck:
                analysed = analysed+char
        text= {'text1':analysed, 'switch':analyse_checkbox, 'purposr':'Puncution Removed', 'text2':djtext}
        djtext = analysed
    
    if(fullcaps == 'on'):
        analysed= ""
        for char in djtext:
            analysed  = analysed +char.upper()
        text= {'text1':analysed, 'switch':analyse_checkbox, 'purposr':'Capalitize all character', 'text2':djtext}
        djtext = analysed
    
    if(newlineremover == 'on'):
        analysed=""
        for char in djtext:
            if char !="\n" and char!="\r":
                analysed = analysed +char
        text= {'text1':analysed, 'switch':analyse_checkbox, 'purposr':'Capalitize all character', 'text2':djtext}
        djtext = analysed
    
    if(extraspaceremover=='on'):
        analysed =""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] ==" "):
                analysed = analysed +char
        text= {'text1':analysed, 'switch':analyse_checkbox, 'purposr':'Capalitize all character', 'text2':djtext}
        djtext = analysed
    
    if(charcount == 'on'):
        analysed =0
        for char in djtext:
            if char != ' ':
                analysed = analysed+ 1
        d = "your char count is "+str(analysed)
        print()
        text= {'text1':d, 'switch':analyse_checkbox, 'purposr':'Capalitize all character', 'text2':djtext}
        # djtext = analysed       
        
    if( analyse_checkbox != 'on' and fullcaps != 'on'and newlineremover != 'on'and extraspaceremover !='on'and charcount != 'on' ):
        return HttpResponse("select any option")
    
    return render(request,'analyse.html' ,text)
