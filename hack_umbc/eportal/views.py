from django.shortcuts import render
from .ocr import main_url
# Create your views here.

def ocr_page(request):
    return render(request, 'eportal/ocr_form.html', {})

def ocr_output(request):
    if request.method == "POST":
        if 'ocr_file' in request.FILES:
            file = request.FILES['ocr_file']
            final_output = main_url(file)
            text = ''
            for output in final_output:
                text = text + output
            return render(request,'eportal/ocr_output.html',{'output':text})

def index(request):
    return render(request,'eportal/index.html',{})

def synthesizer(request):
    return render(request,'eportal/synthsizer.html',{})
