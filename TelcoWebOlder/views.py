# from base64 import encode
# from os import pipe
# from subprocess import run,PIPE
# import sys
# import decimal
# from matplotlib.pyplot import title

from django.shortcuts import render

import TelcoWebOlder.plot as p
import TelcoWebOlder.module as m

import numpy as np
import scipy.signal as sg
import scipy.fft as fr
import cmath

# Create your views here.
def home(request):
    title = "Home"
    return render(request, 'telcolabolder/old-home.html', {title: 'title'})

def base(request):
    title = "Base"
    return render(request, 'telcolabolder/old-base.html', {title: 'title'})

def experiments(request):
    title = "Experiments"
    return render(request, 'telcolabolder/old-experiments.html', {title: 'title'})

def index(request):
    return render(request, 'telcolabolder/index.html')

def test(request):
    return render(request, 'telcolabolder/index.html')

# Views di TelcoLAB versi new
def coba(request):
    return render(request, 'telcolabolder/coba.html')

# Views tab Signalgen
def signalgen(request):

    # Ada 3 jenis gelombang dari signalgen : Sinusoidal, Square, Sawtooth/Triangle
    # Input dari website - Format : (wave) 'freq' (freq) 'sample' (freq_sample) 'amp' (amp) 
    inp         = request.POST.get('parameter_signal')                          # Pengambilan data input dari website
    data        = inp.split()                                                   # Data input (array) dipecah per suku/isi nya
    wave        = data[0]                                                       # Data jenis gelombang dari array data ke 0
    freq        = float(data[2])                                                # Data frekuensi (pecahan) dari array data ke 2
    freq_sample = int(data[4])                                                  # Data sampling (integer) dari array data ke 4
    amp         = float(data[6])                                                # Data amplitudo (pecahan) dari array data ke 6

    # Pembuatan sinyal/gelombang (sin, square, and triangle/sawtooh)
    time    = np.linspace(0, 1, 5*freq_sample, endpoint = False)                # Setting range waktu untuk signal generator
    # sinWave = amp*np.sin(2*np.pi*freq*time)                                     # Pembuatan gelombang sinus
    sinWave = m.sine(amp,freq_sample,freq)
    sqWave  = amp*sg.square(2*np.pi*freq*time, duty = 0.3)                      # Pembuatan gelombang kotak
    sawWave = amp*sg.sawtooth(2*np.pi*freq*time, width = 0.5)                   # Pembuatan gelombang segitiga

    # Plotting signal generator dari 'plot.py'
    sin   = p.get_plot_sin(sinWave)                                    # Plotting gelombang sinus
    sq    = p.get_plot_sq(sqWave)                                      # Plotting gelombang kotak
    saw   = p.get_plot_saw(sawWave)                                    # Plotting gelombang segitiga
    semua = p.get_plot_signalgen(sinWave, sqWave, sawWave)             # Plotting gelombang (3 gelombang)

    return render(request, 'telcolabolder/coba.html', {
        'wave': wave,
        'inp': inp,
        'sin': sin,
        'sq': sq,
        'saw': saw,
        'semua': semua})

# Views tab AM Modulation
def am(request):

    # Ada 3 jenis AM Modulation : AM DSBFC, AM DSBSC, AM SSB
    # Input dari website - Format : (tipe) (wave) 'Am' (Am) 'fm' (fm) 'carrier Ac' (Ac) 'fc' (fc) 'sample' (fs)  
    inp  = request.POST.get('parameter_am')                                     # Pengambilan data input dari website
    data = inp.split()                                                          # Data input (array) dipecah per suku/isi nya
    tipe = data[0]                                                              # Data jenis modulasi (DSBFC/DSBSC/SSB) dari array data ke 0
    wave = data[1]                                                              # Data jenis gelombang dari array data ke 1

    # Input parameter waktu
    N  = 1024
    fs = 1000                                                                   # Frekuensi sampling
    ta = 1 / fs                                                                 # Step waktu 
    t  = np.arange(0, 1, ta)                                                    # Time variable

    # Isyarat pemodulasi m(t) - time domain
    Am = float(data[3])                                                         # Amplitudo isyarat pemodulasi m(t) dari array ke 3
    fm = float(data[5])                                                         # Frekuensi isyarat pemodulasi m(t) dari array ke 5
    if wave == 'sinus':
        mt = Am*np.cos(2*np.pi*fm*t)                                              # Output isyarat pemodulasi m(t) gelombang sinus
    elif wave == 'square':
        mt = Am*sg.square(2*np.pi*fm*t, duty = 0.3)                               # Output isyarat pemodulasi m(t) gelombang kotak
    elif wave == 'sawtooth':
        mt = Am*sg.sawtooth(2*np.pi*fm*t, width = 0.5)                            # Output isyarat pemodulasi m(t) gelombang segitiga
    # Isyarat pemodulasi m(t) - freq domain
    mf = fr.fft(mt)/len(mt)                                                     # FFT dari isyarat pemodulasi m(t)
    mf = mf[range(int(len(mt)/2))]*2                                            # Hasil akhir FFT isyarat pemodulasi m(t)

    # Isyarat pembawa c(t) - time domain
    Ac = float(data[8])                                                         # Amplitudo isyarat pembawa c(t) dari array ke 8
    fc = float(data[10])                                                        # Frekuensi isyarat pembawa c(t) dari array ke 10
    ct = Ac*np.cos(2*np.pi*fc*t)                                                # Output isyarat pembawa c(t)
    # Isyarat pembawa c(t) - freq domain
    cf = fr.fft(ct)/len(ct)                                                     # FFT dari isyarat pemodulasi c(t)
    cf = cf[range(int(len(ct)/2))]*2                                            # Hasil akhir FFT isyarat pemodulasi c(t)

    # AM DSBFC - time domain
    dsbfc_mod   = mt*ct + ct                                                    # Isyarat termodulasi AM DSBFC
    envelope    = np.abs(sg.hilbert(dsbfc_mod))                                 # Deteksi envelope pada isyarat termodulasi
    dsbfc_demod = envelope-Ac                                                   # Demodulasi isyarat AM DSBFC
    # AM DSBFC - freq domain
    dsbfc_modFreq   = fr.fft(dsbfc_mod)/len(dsbfc_mod)                          # FFT dari isyarat termodulasi AM DSBFC
    dsbfc_modFreq   = dsbfc_modFreq[range(int(len(dsbfc_mod)/2))]*2             # Hasil akhir FFT
    dsbfc_demodFreq = fr.fft(dsbfc_demod)/len(dsbfc_demod)*2                    # FFT dari isyarat demodulasi AM DSBFC
    dsbfc_demodFreq = dsbfc_demodFreq[range(int(len(dsbfc_demod)/2))]           # Hasil akhir FFT

    # AM DSBSC - time domain
    dsbsc_mod   = mt*ct                                                         # Isyarat termodulasi AM DSBSC
    dsbsc_demod = (2*dsbsc_mod*np.cos(2*np.pi*fc*t))/Ac                         # Demodulasi isyarat (sebelum filter)
    b, a        = sg.butter(3, 3/(0.5*fs), btype = 'low', analog = False)       # Pemilihan filter pada output isyarat demodulasi
    dsbsc_demod = sg.filtfilt(b, a, dsbsc_demod)                                # Demodulasi isyarat (setelah filter)
    # AM DSBSC - freq domain
    dsbsc_modFreq   = fr.fft(dsbsc_mod)/len(dsbsc_mod)                          # FFT dari isyarat termodulasi AM DSBSC
    dsbsc_modFreq   = dsbsc_modFreq[range(int(len(dsbsc_mod)/2))]*2             # Hasil akhir FFT
    dsbsc_demodFreq = fr.fft(dsbsc_demod)/len(dsbsc_demod)*2                    # FFT dari isyarat demodulasi AM DSBSC
    dsbsc_demodFreq = dsbsc_demodFreq[range(int(len(dsbsc_demod)/2))]           # Hasil akhir FFT

    # AM SSB - time domain
    mh          = Am*np.cos(2*np.pi*fm*t)                                       # m(t) ditambah Hilbert transform
    ssb_mod     = mt*2*np.cos(2*np.pi*fc*t) - mh*2*np.sin(2*np.pi*fc*t)         # Modulasi SSB output untuk USB
    ssb_lsb     = mt*2*np.cos(2*np.pi*fc*t) + mh*2*np.sin(2*np.pi*fc*t)         # Modulasi SSB output untuk LSB (tidak ditampilkan pada hasil akhir)
    ssb_demod   = 2*ssb_mod*np.cos(2*np.pi*fc*t)                                # Demodulasi isyarat (sebelum filter)
    b, a        = sg.butter(3, 0.005, btype = 'low', analog = False)            # Pemilihan filter pada output isyarat demodulasi
    ssb_demod   = sg.filtfilt(b, a, ssb_demod)                                  # Demodulasi isyarat (setelah filter)
    # AM SSB - freq domain
    ssb_modFreq   = fr.fft(ssb_mod)/len(ssb_mod)                                # FFT dari isyarat termodulasi AM SSB
    ssb_modFreq   = ssb_modFreq[range(int(len(ssb_mod)/2))]*2                   # Hasil akhir FFT
    ssb_demodFreq = fr.fft(ssb_demod)/len(ssb_demod)                            # FFT dari isyarat demodulasi AM SSB
    ssb_demodFreq = ssb_demodFreq[range(int(len(ssb_demod)/2))]                 # Hasil akhir FFT

    # Frequency Domain Properties
    tpCount     = len(mt)                                                       # Hasil panjang isyarat m(t)
    values      = np.arange(int(tpCount/2))                                     # 
    timePeriod  = tpCount/fs                                                    # Periode -> hasil bagi 'tpCount' dengan frekuensi sampling
    xf          = values/timePeriod                                             # Hasil plot sumbu x pada freq. domain

    # Variabel tabel : t, mt, ct, isyarat termodulasi, isyarat demodulasi
    dsbfc_result = p.get_plot_fc(t, xf, mt, mf, ct, cf, dsbfc_mod, envelope, dsbfc_demod, dsbfc_modFreq, dsbfc_demodFreq)
    dsbsc_result = p.get_plot_sc(t, xf, mt, mf, ct, cf, dsbsc_mod, dsbsc_demod, dsbsc_modFreq, dsbsc_demodFreq)
    ssb_result   = p.get_plot_ssb(t, xf, mt, mf, ct, cf, ssb_mod, ssb_demod, ssb_modFreq, ssb_demodFreq)

    return render(request, 'telcolabolder/coba.html', {
        'tipe': tipe,
        'ssb_result': ssb_result,
        'dsbfc_result': dsbfc_result,
        'dsbsc_result': dsbsc_result})

# Views tab FM Modulation
def fm(request):

    # Input dari website - Format : 'FM' (wave) 'Am' (Am) 'fm' (fm) 'carrier Ac' (Ac) 'fc' (fc) 'sample' (fs)
    inp  = request.POST.get('parameter_fm')                                     # Pengambilan data input dari website
    data = inp.split()                                                          # Data input (array) dipecah per suku/isi nya
    tipe = data[1]

    # Input parameter waktu
    mod_index = 0.75                                                            # Indeks modulasi 
    fs = 44100                                                                  # Frekuensi sampling
    ta = 1/fs                                                                   # Step waktu 
    t  = np.arange(0, 1, ta)                                                    # Time variable
    
    # Isyarat pemodulasi m(t) - time domain
    Am = 1                                                                      # Amplitudo isyarat pemodulasi m(t) dari array ke 3
    fm = 4                                                                      # Frekuensi isyarat pemodulasi m(t) dari array ke 5
    mt = np.sin(2*np.pi*fm*t)*mod_index                                      # Output isyarat pemodulasi m(t) gelombang sinus
    # Isyarat pemodulasi m(t) - freq domain
    mf = fr.fft(mt)/len(mt)                                                     # FFT dari isyarat pemodulasi m(t)
    mf = mf[range(int(len(mt)/2))]                                              # Hasil akhir FFT isyarat pemodulasi m(t)

    # Isyarat pembawa c(t) - time domain
    Ac = 1                                                                      # Amplitudo isyarat pembawa c(t) dari array ke 8
    fc = 40                                                                     # Frekuensi isyarat pembawa c(t) dari array ke 10
    ct = np.sin(2*np.pi*fc*t)                                                # Output isyarat pembawa c(t)
    # Isyarat pembawa c(t) - freq domain
    cf = fr.fft(ct)/len(ct)                                                     # FFT dari isyarat pemodulasi c(t)
    cf = cf[range(int(len(ct)/2))]                                              # Hasil akhir FFT isyarat pemodulasi c(t)

    # FM Modulation - time domain
    fm_mod = np.zeros_like(mt)                                                  # Apa
    for i, t in enumerate(t):
        fm_mod[i] = np.sin(np.pi * (2*fc*t + mt[i]))                              # Apa
    # FM Modulation - freq domain
    fm_modFreq = fr.fft(fm_mod)/len(fm_mod)                                     # Apa
    fm_modFreq = fm_modFreq[range(int(len(fm_mod)/2))]                          # Apa

    # FM Demodulation - time domain (menggunakan diskriminasi frekuensi)
    dif = np.diff(fm_mod)*500                                                   # Differensial
    fm_demod     = abs(sg.hilbert(dif))                                         # Deteksi seleubung (envelope) menggunakan Hilbert
    fm_demodFFT  = np.fft.rfft(fm_demod)                                        # Demod di bagian freq domain
    fm_demodFFT  = fm_demodFFT*cmath.rect(-1., np.pi/2)                         # Geser fase sebesar pi/2
    fm_demod     = np.fft.irfft(fm_demodFFT)                                    # Mengembalikan hasil demodulasi freq domain ke time domain
    # FM Demodulation - freq domain
    fm_demodFreq = fr.fft(fm_demod)/len(fm_demod)                               # Apa
    fm_demodFreq = fm_demodFreq[range(int(len(fm_demod)/2))]                    # Apa

    # Frequency Domain Properties
    tpCount     = len(mt)                                                       # Hasil panjang isyarat m(t)
    values      = np.arange(int(tpCount/2))                                     # 
    timePeriod  = tpCount/fs                                                    # Periode -> hasil bagi 'tpCount' dengan frekuensi sampling
    xf          = values/timePeriod                                             # Hasil plot sumbu x pada freq. domain

    # Variabel tabel : t, mt, ct, isyarat termodulasi, isyarat demodulasi
    fm_timeResult = p.get_plot_fm_timeResult(mt, ct, fm_mod, fm_demod)
    fm_freqResult = p.get_plot_fm_freqResult(xf, fc, mf, cf, fm_modFreq, fm_demodFreq)
    # fm_allResult  = plot.get_plot_fm_allResult(t, mt, ct, )

    return render(request,'telcolabolder/coba.html',{
        'tipe': tipe,
        'fm_timeResult': fm_timeResult,
        'fm_freqResult': fm_freqResult})
        # 'fm_allResult': fm_allResult
