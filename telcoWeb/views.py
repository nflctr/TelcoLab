# from numpy.core.numeric import Inf
from django.db.models.query import ValuesIterable
from django.shortcuts import redirect, render
from collections import ChainMap
from .models import Information
import telcoWeb.module as m
# ---------------------------------------------------------------------------------------------
txt = {
    'po' : Information.objects.filter(title='Headline'),
    'sg' : Information.objects.filter(title='Signal - Materi'),
    'fc' : Information.objects.filter(title='AM DSBFC - Materi'),
    'sc' : Information.objects.filter(title='AM DSBSC - Materi'),
    'sb' : Information.objects.filter(title='AM SSB - Materi'),
    'fm' : Information.objects.filter(title='FM - Materi'),
    'dg' : Information.objects.filter(title='Digital - Materi'),}
# ---------------------------------------------------------------------------------------------
def coba(request):
  return render(request, 'telcoLab.html', txt)
# ---------------------------------------------------------------------------------------------
def generator(request):
  inp  = request.POST.get('param-generator')      # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string  
  try:
    txt1 = {'Show' : m.inputData(data)}
    kata = m.inputKata(data)
    if kata == False:
      raise ValueError('Salah penulisan kode')
  except ValueError as e:
    txt1 = {'typoCode': e}
  except Exception as e:
    txt1 = {'typoParameter': e}
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------
def dsbfc(request):
  inp  = request.POST.get('param-dsbfc')          # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
  try:
    txt1 = {'fcShow' : m.inputData(data)}
    kata = m.inputKata(data)
    if kata == False:
      raise ValueError('Salah penulisan kode')
  except ValueError as e:
    print(e)
    txt1 = {'typoCode': e}
  except Exception as e:
    print(e)
    txt1 = {'typoParameter': e}
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------
def dsbsc(request):
  inp  = request.POST.get('param-dsbsc')          # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
  try:
    txt1 = {'scShow' : m.inputData(data)}
    kata = m.inputKata(data)
    if kata == False:
      raise ValueError('Salah penulisan kode')
  except ValueError as e:
    print(e)
    txt1 = {'typoCode': e}
  except Exception as e:
    print(e)
    txt1 = {'typoParameter': e}
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------
def ssb(request):
  inp  = request.POST.get('param-ssb')            # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
  try:
    txt1 = {'ssShow' : m.inputData(data)}
    kata = m.inputKata(data)
    if kata == False:
      raise ValueError('Salah penulisan kode')
  except ValueError as e:
    print(e)
    txt1 = {'typoCode': e}
  except Exception as e:
    print(e)
    txt1 = {'typoParameter': e}
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------
def fm(request):
  inp  = request.POST.get('param-fm')             # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
  try:
    txt1 = {'fmShow' : m.inputData(data)}
    kata = m.inputKata(data)
    if kata == False:
      raise ValueError('Salah penulisan kode')
  except ValueError as e:
    print(e)
    txt1 = {'typoCode': e}
  except Exception as e:
    print(e)
    txt1 = {'typoParameter': e}
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------
def digital(request):
  inp  = request.POST.get('param-digital')        # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
  try:
    txt1 = {'diShow' : m.inputData(data)}
    kata = m.inputKata(data)
    if kata == False:
      raise ValueError('Salah penulisan kode')
  except ValueError as e:
    txt1 = {'typoCode': e}
  except Exception as e:
    txt1 = {'typoParameter': e}
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------
def index(request):
  return render(request, 'index.html')
# ---------------------------------------------------------------------------------------------