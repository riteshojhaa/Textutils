# I have created this.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse("about ritesh")

def analyze(request):
    dtext = request.POST.get('text', 'default')
    removep = request.POST.get('analyze', 'off')
    capitalize = request.POST.get('capital', 'off')
    lineremover = request.POST.get('lineremover', 'off')
    removeextraspace = request.POST.get('removeextraspace', 'off')

    analyze = ""
    punctuations = '''!()-[];:'"\,<>./?@#$%^&*_~'''
    
    if removep == "on":
        for char in dtext:
            if char not in punctuations:
                analyze = analyze + char
        param = {"purpose":"Remove punctuations words", "analyzed":analyze}
        dtext = analyze
        # return render(request, 'analyze.html', param)
     
    if (capitalize == 'on'):
        analyze = ""
        for char in dtext:
            analyze = analyze + char.upper()
        param = {"purpose": "UPPER CASE words", "analyzed":analyze}
        dtext = analyze
        # return render(request, 'analyze.html', param)
    
    if (lineremover == 'on'):
        analyze = ""
        for char in dtext:
            if char!='\n' and char!='\r':
                analyze = analyze + char
        param = {"purpose": "Lines Removed", "analyzed":analyze}
        dtext = analyze
        # return render(request, 'analyze.html', param)
    
    if (removeextraspace == 'on'):
        analyze = ""
        for index, char in enumerate(dtext):
            if not (dtext[index] == " " and dtext[index+1] == " "):
                analyze = analyze + char
        param = {"purpose": "Extra space removed", "analyzed":analyze}
        dtext = analyze
    
    if (removep != 'on' and capitalize != 'on' and lineremover != 'on' and removeextraspace != 'on'):
        return HttpResponse(dtext)
    
    
    return render(request, 'analyze.html', param)
