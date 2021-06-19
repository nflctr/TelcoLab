# from numpy.core.numeric import Inf
from django.shortcuts import redirect, render
from collections import ChainMap
from .models import Information
import telcoWeb.module as m
txt = {
    'po' : Information.objects.filter(title='Headline'),
    'sg' : Information.objects.filter(title='Signal - Materi'),
    'fc' : Information.objects.filter(title='AM DSBFC - Materi'),
    'sc' : Information.objects.filter(title='AM DSBSC - Materi'),
    'sb' : Information.objects.filter(title='AM SSB - Materi'),
    'fm' : Information.objects.filter(title='FM - Materi'),
    'dg' : Information.objects.filter(title='Digital - Materi'),}
# ---------------------------------------------------------------------------------------------
def index(request):
  return render(request, 'index.html')
# ---------------------------------------------------------------------------------------------
def coba(request):
  return render(request, 'telcoLab.html', txt)
# ---------------------------------------------------------------------------------------------
def generator(request):
  inp  = request.POST.get('param-generator')      # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string  
  try:
    amp  = float(data[2])                           # Ambil data amp  (float)
    fs   = float(data[4])                           # Ambil data fs   (float)
    freq = float(data[6])                           # Ambil data freq (float)
    plot = data[8]                                  # Ambil data plot (string)
    txt1 = {'Show' : m.signalGenerator(plot,amp,fs,freq)}
  except Exception as e:
    print(e)
    # salah = e
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------
def dsbfc(request):
  inp  = request.POST.get('param-dsbfc')          # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
  try:
    mt   = data[1]                                  # Input message - Jenis gelombang yang digunakan
    mtA  = float(data[3])                           # Ambil data amplitudo m(t) (float)
    fs   = float(data[5])                           # Ambil data frek. sampling (float)
    mtF  = float(data[7])                           # Ambil data frekuensi m(t) (float)
    ct   = data[9]                                  # Input carrier - Jenis gelombang yang digunakan
    ctA  = float(data[11])                          # Ambil data amplitudo c(t) (float)
    ctF  = float(data[15])                          # Ambil data frekuensi c(t) (float)
    fcPlot = data[27]                               # Ambil data DSBFC apa yang mau ditampilkan di web
    fcDom  = data[28]                               # Ambil data domain (time/freq)
    txt1 = {'fcShow': m.amDSBFC(mt,mtA,fs,mtF,ct,ctA,ctF,fcPlot,fcDom)}
  except Exception as e:
    print(e)
    # txt2 = e
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------
def dsbsc(request):
  inp  = request.POST.get('param-dsbsc')          # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
  try:
    mt   = data[1]                                  # Input message - Jenis gelombang yang digunakan
    mtA  = float(data[3])                           # Ambil data amplitudo m(t) (float)
    fs   = float(data[5])                           # Ambil data frek. sampling (float)
    mtF  = float(data[7])                           # Ambil data frekuensi m(t) (float)
    ct   = data[9]                                  # Input carrier - Jenis gelombang yang digunakan (cosinus)
    ctA  = float(data[11])                          # Ambil data amplitudo c(t) (float)
    ctF  = float(data[15])                          # Ambil data frekuensi c(t) (float)
    orx  = float(data[26])                          # Ambil data orde filter
    cut  = float(data[28])                          # Ambil data frekuensi cutoff filter
    scPlot = data[30]                               # Ambil data DSBSC apa yang mau ditampilkan di web
    scDom  = data[31]                               # Ambil data domain (time/freq)
    txt1 = {'scShow': m.amDSBSC(mt,mtA,fs,mtF,ct,ctA,ctF,orx,cut,scPlot,scDom)}
    pass
  except Exception as e:
    print(e)
    # txt2 = e
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------
def ssb(request):
  inp  = request.POST.get('param-ssb')            # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
  try:
    mt   = data[1]                                  # Input message - Jenis gelombang yang digunakan
    mtA  = float(data[3])                           # Ambil data amplitudo m(t) (float)
    fs   = float(data[5])                           # Ambil data frek. sampling (float)
    mtF  = float(data[7])                           # Ambil data frekuensi m(t) (float)
    ct   = data[9]                                  # Input carrier - Jenis gelombang yang digunakan (cosinus dan sinus)
    ctA  = float(data[11])                          # Ambil data amplitudo c(t) (float)
    ctF  = float(data[15])                          # Ambil data frekuensi c(t) (float)
    mh   = data[17]                                 # Input hilbert - Jenis gelombang yang digunakan (sinus)
    mhA  = float(data[19])                          # Ambil data amplitudo h(t) (float)
    mhF  = float(data[21])                          # Ambil data frekuensi h(t) (float)
    orx  = float(data[40])                          # Ambil data orde filter
    cut  = float(data[42])                          # Ambil data frekuensi cutoff filter
    ssPlot = data[44]                               # Ambil data DSBSC apa yang mau ditampilkan di web
    ssDom  = data[45]                               # Ambil data domain (time/freq)
    txt1 = {'ssShow': m.amSSB(mt,mtA,fs,mtF,ct,ctA,ctF,mh,mhA,mhF,orx,cut,ssPlot,ssDom)}
  except Exception as e:
    print(e)
    # txt2 = e
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------
def fm(request):
  inp  = request.POST.get('param-fm')             # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
  try:
    mt   = data[1]                                  # Input message - Jenis gelombang yang digunakan
    mtA  = float(data[3])                           # Ambil data amplitudo m(t) (float)
    fs   = float(data[5])                           # Ambil data frek. sampling (float)
    mtF  = float(data[7])                           # Ambil data frekuensi m(t) (float)
    ct   = data[9]                                  # Input carrier - Jenis gelombang yang digunakan (cosinus)
    ctA  = float(data[11])                          # Ambil data amplitudo c(t) (float)
    ctF  = float(data[15])                          # Ambil data frekuensi c(t) (float)
    idx  = float(data[17])                          # Ambil data indeks modulasi
    fmPlot = data[31]                               # Ambil data FM apa yang mau ditampilkan di web
    fmDom  = data[32]                               # Ambil data domain (time/freq)
    txt1 = {'fmShow': m.fm(mt,mtA,fs,mtF,ct,ctA,ctF,idx,fmPlot,fmDom)}
  except Exception as e:
    print(e)
    # txt2 = e
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------
def digital(request):
  inp  = request.POST.get('param-digital')        # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
  try:
    fs   = float(data[2])                           # Ambil data frek. sampling (float)
    ctF  = float(data[4])                           # Ambil data frekuensi c(t) (float)
    xSum = int(data[7])                             # Ambil data jumlah random data yang akan di-generate
    plot = data[9]                                  # Ambil data FM apa yang mau ditampilkan di web
    txt1 = {'diShow': m.digital(fs,ctF,xSum,plot)}
  except Exception as e:
    print(e)
    # txt2 = e
  return render(request, 'telcoLab.html', dict(ChainMap(txt1,txt)))
# ---------------------------------------------------------------------------------------------