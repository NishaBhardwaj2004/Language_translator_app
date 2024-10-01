from django.shortcuts import render
from googletrans import Translator

# Create your views here.

def translator(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        return render(request, 'translator.html',{'name':name})
    else:
        return render(request, 'translator.html',{'name':'!'})


def translated(request):
    if request.method=="POST":
        text=request.POST.get('text')
        lang=request.POST.get('lang')
        print('text:',text,'lang:',lang)

        #translate
        translator_instance=Translator()
        #detect language
        dt=translator_instance.detect(text)
        dt2=dt.lang
        translated=translator_instance.translate(text, lang)
        tr=translated.text

    return render(request,'translated.html',{'translated':tr,'u_lang':dt2,'t_lang':lang})
    

def home(request):
    return render(request,'home.html')