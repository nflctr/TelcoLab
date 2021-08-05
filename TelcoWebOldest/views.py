from os import pipe
from django.shortcuts import render, HttpResponse
from subprocess import run,PIPE
import sys

# Create your views here.
def home(request):
    return render(request, 'telcolaboldest/home.html')

def base(request):
    return render(request, 'telcolaboldest/base.html')

def experiments(request):
    return render(request, 'telcolaboldest/experiments.html')

def external(request):
    inp = request.POST.get('param')
    out = run([sys.executable,'TelcoWebOldest/boo.py',inp],shell=False,stdout=PIPE)
    print(out)
    return render(request,'telcolaboldest/experiments.html',{'data1':out.stdout})

def signal(request):
    out = run([sys.executable,'TelcoWebOldest/signalgen.py'],shell=False,stdout=PIPE)
    print(out)
    return render(request,'telcolaboldest/experiments.html',{'data2':out})
