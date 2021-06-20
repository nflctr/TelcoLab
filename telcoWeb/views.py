# from numpy.core.numeric import Inf
# from django.db.models.query import ValuesIterable
from django.shortcuts import render
from collections import ChainMap
from .models import Information
import telcoWeb.module as m
# ---------------------------------------------------------------------------------------------
txt = {
    'po' : Information.objects.filter(Title='Headline'),
    'sg' : Information.objects.filter(Title='Signal - Materi'),
    'fc' : Information.objects.filter(Title='AM DSBFC - Materi'),
    'sc' : Information.objects.filter(Title='AM DSBSC - Materi'),
    'sb' : Information.objects.filter(Title='AM SSB - Materi'),
    'fm' : Information.objects.filter(Title='FM - Materi'),
    'dg' : Information.objects.filter(Title='Digital - Materi'),}
# ---------------------------------------------------------------------------------------------
def telcoLab(request):
  return render(request, 'telcoLab.html', txt)
# ---------------------------------------------------------------------------------------------
def signalGenerator(request):
  inp  = request.POST.get('inputSignalGenerator')       # Get input dari web(user)
  data = inp.split()                                    # 'inp' displit jadi satu array berisi kumpulan string  
  try:
    txt1 = {'sgShow' : m.inputData(data)}
    kata = m.inputKata(data)
    if kata == False:
      raise ValueError('Salah penulisan kode')
  except ValueError as e:
    txt1 = {'typoCodeSignalGenerator': e}
  except Exception as e:
    txt1 = {'typoParameterSignalGenerator': e}
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------
def dsbfcModulation(request):
  inp  = request.POST.get('inputDSBFC')           # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
  try:
    txt1 = {'fcShow' : m.inputData(data)}
    kata = m.inputKata(data)
    if kata == False:
      raise ValueError('Salah penulisan kode')
  except ValueError as e:
    txt1 = {'typoCodeDSBFC': e}
  except Exception as e:
    txt1 = {'typoParameterDSBFC': e}
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------
def dsbscModulation(request):
  inp  = request.POST.get('inputDSBSC')          # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
  try:
    txt1 = {'scShow' : m.inputData(data)}
    kata = m.inputKata(data)
    if kata == False:
      raise ValueError('Salah penulisan kode')
  except ValueError as e:
    txt1 = {'typoCodeDSBSC': e}
  except Exception as e:
    txt1 = {'typoParameterDSBSC': e}
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------
def ssbModulation(request):
  inp  = request.POST.get('inputSSB')            # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
  try:
    txt1 = {'ssShow' : m.inputData(data)}
    kata = m.inputKata(data)
    if kata == False:
      raise ValueError('Salah penulisan kode')
  except ValueError as e:
    txt1 = {'typoCodeSSB': e}
  except Exception as e:
    txt1 = {'typoParameterSSB': e}
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------
def frequencyModulation(request):
  inp  = request.POST.get('inputFM')             # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
  try:
    txt1 = {'fmShow' : m.inputData(data)}
    kata = m.inputKata(data)
    if kata == False:
      raise ValueError('Salah penulisan kode')
  except ValueError as e:
    txt1 = {'typoCodeFM': e}
  except Exception as e:
    txt1 = {'typoParameterFM': e}
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------
def digitalModulation(request):
  inp  = request.POST.get('inputDigitalModulation')        # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
  try:
    txt1 = {'diShow' : m.inputData(data)}
    kata = m.inputKata(data)
    if kata == False:
      raise ValueError('Salah penulisan kode')
  except ValueError as e:
    txt1 = {'typoCodeDigital': e}
  except Exception as e:
    txt1 = {'typoParameterDigital': e}
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------
def index(request):
  return render(request, 'index.html')
# ---------------------------------------------------------------------------------------------