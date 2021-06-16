# from numpy.core.numeric import Inf
from django.shortcuts import render
from collections import ChainMap
from .models import Informations
import telcoWeb.module as m
txt = {
    'post' : Informations.objects.filter(judul='Welcome'),
    'sg' : Informations.objects.filter(judul='Signal-Generator'),
    'fc' : Informations.objects.filter(judul='AM-DSBFC'),
    'sc' : Informations.objects.filter(judul='AM-DSBSC'),
    'sb' : Informations.objects.filter(judul='AM-SSB'),
    'fm' : Informations.objects.filter(judul='FM-Mod'),
    'dg' : Informations.objects.filter(judul='Digital-Mod'),}
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
  amp  = float(data[2])                           # Ambil data amp  (float)
  fs   = float(data[4])                           # Ambil data fs   (float)
  freq = float(data[6])                           # Ambil data freq (float)
  plot = data[8]                                  # Ambil data plot (string)
  text = {'Show' : m.signalGenerator(plot,amp,fs,freq)}
  return render(request, 'telcoLab.html', dict(ChainMap(text,txt)))
# ---------------------------------------------------------------------------------------------
def dsbfc(request):
  inp  = request.POST.get('param-dsbfc')          # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
  mt   = data[1]                                  # Input message - Jenis gelombang yang digunakan
  mtA  = float(data[3])                           # Ambil data amplitudo m(t) (float)
  fs   = float(data[5])                           # Ambil data frek. sampling (float)
  mtF  = float(data[7])                           # Ambil data frekuensi m(t) (float)
  ct   = data[9]                                  # Input carrier - Jenis gelombang yang digunakan
  ctA  = float(data[11])                          # Ambil data amplitudo c(t) (float)
  ctF  = float(data[15])                          # Ambil data frekuensi c(t) (float)
  fcPlot = data[27]                               # Ambil data DSBFC apa yang mau ditampilkan di web
  fcDom  = data[28]                               # Ambil data domain (time/freq)
  text = {'fcShow': m.amDSBFC(mt,mtA,fs,mtF,ct,ctA,ctF,fcPlot,fcDom)}
  return render(request, 'telcoLab.html', dict(ChainMap(text,txt)))
# ---------------------------------------------------------------------------------------------
def dsbsc(request):
  inp  = request.POST.get('param-dsbsc')          # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
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
  text = {'scShow': m.amDSBSC(mt,mtA,fs,mtF,ct,ctA,ctF,orx,cut,scPlot,scDom)}
  return render(request, 'telcoLab.html', dict(ChainMap(text,txt)))
# ---------------------------------------------------------------------------------------------
def ssb(request):
  inp  = request.POST.get('param-ssb')            # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
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
  text = {'ssShow': m.amSSB(mt,mtA,fs,mtF,ct,ctA,ctF,mh,mhA,mhF,orx,cut,ssPlot,ssDom)}
  return render(request, 'telcoLab.html', dict(ChainMap(text,txt)))
# ---------------------------------------------------------------------------------------------
def fm(request):
  inp  = request.POST.get('param-fm')             # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
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
  text = {'fmShow': m.fm(mt,mtA,fs,mtF,ct,ctA,ctF,idx,fmPlot,fmDom)}
  return render(request, 'telcoLab.html', dict(ChainMap(text,txt)))
# ---------------------------------------------------------------------------------------------
def digital(request):
  inp  = request.POST.get('param-digital')        # Get input dari web(user)
  data = inp.split()                              # 'inp' displit jadi satu array berisi kumpulan string
  fs   = float(data[2])                           # Ambil data frek. sampling (float)
  ctF  = float(data[4])                           # Ambil data frekuensi c(t) (float)
  xSum = int(data[7])                             # Ambil data jumlah random data yang akan di-generate
  plot = data[9]                                  # Ambil data FM apa yang mau ditampilkan di web
  text = {'diShow': m.digital(fs,ctF,xSum,plot)}
  return render(request, 'telcoLab.html', dict(ChainMap(text,txt)))
# ---------------------------------------------------------------------------------------------