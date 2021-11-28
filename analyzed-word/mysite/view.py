# i have create a page
from django.shortcuts import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def Removing(request, ):
    # global  king
    Text = request.POST.get('text', 'default')
    remove = request.POST.get('remove', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    newline = request.POST.get('newline', 'off')
    print(remove)
    print(Text)
    if remove == "on":
        # analyzed = Text
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in Text:
            if char not in punctuations:
                analyzed = analyzed + char
        king = {'purpose': 'Remover punctuations', 'analyzed_text': analyzed}
        return render(request, 'index2.html', king)
    elif uppercase == "on":
        analyzed = ""
        for char in Text:
            analyzed = analyzed + char.upper()
        king = {'purpose': 'change to upper case', 'analyzed_text': analyzed}
        return render(request, 'index2.html', king)
    elif newline == "on":
        analyzed = ""
        for char in Text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char.upper()
        king = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        return render(request, 'index2.html', king)
    else:
        return HttpResponse('error')
