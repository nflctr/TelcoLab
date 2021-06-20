import numpy as np
import scipy.signal as sg
import scipy.fftpack as fr
import cmath as c
import telcoWeb.plot as p

""" Modul Fungsi Matematika """
# Fungsi Adder (Penambahan)
def add(add_1, add_2):
    return add_1+add_2
# Fungsi sub (pengurangan)
def sub(sub_1, sub_2):
    return sub_1-sub_2
# Fungsi multiplier (Perkalian)
def mul(mul_1, mul_2):
    return mul_1*mul_2
# Fungsi division (pembagian)
def div(div_1, div_2):
    return div_1/div_2

""" Modul Signal Generator """
# Fungsi gelombang cosinus
def cosine(Am, fs, fm):
    t = np.arange(0, 1, (1/fs))
    cos = Am*np.cos(2*np.pi*fm*t)
    return cos
# Fungsi gelombang sinus
def sine(Am, fs, fm):
    t = np.arange(0, 1, (1/fs))
    sin = Am*np.sin(2*np.pi*fm*t)
    return sin
# Fungsi gelombang kotak
def square(Am, fs, fm):
    t = np.arange(0, 1, (1/fs))
    sqr = Am*sg.square(2*np.pi*fm*t, duty=0.3)
    return sqr
# Fungsi gelombang segitiga
def sawtooth(Am, fs, fm):
    t = np.arange(0, 1, (1/fs))
    saw = Am*sg.sawtooth(2*np.pi*fm*t, width=0.5)
    return saw

""" Modul untuk Frequency Domain """
# Frequency Domain
def freq(y):
    yf = div(fr.fft(y), len(y))
    yf = mul(yf[range(int(div(len(y), 2)))], 2)
    return np.abs(yf)
# Frequency Domain - X axis Properties
def xProp(mt, fs):
    tpCount = len(mt)
    values = np.arange(int(tpCount/2))
    timePeriod = tpCount/fs
    xf = values/timePeriod
    return xf

""" Modul simulasi AM DSBFC (Full Carrier) """
# Modulasi AM DSBFC
def dsbfc_mod(mt, ct):
    return add(mul(mt, ct), ct)
# Deteksi Envelope AM DSBFC
def envelope(x):
    analytic = sg.hilbert(x)
    return np.abs(analytic)
# Demodulasi AM DSBFC
def dsbfc_demod(envelope, Ac):
    return sub(envelope, Ac)

""" Modul simulasi AM DSBSC (Suppressed Carrier) """
# Modulasi AM DSBSC
def dsbsc_mod(mt, ct):
    return mul(mt, ct)
# Demodulasi AM DSBSC
def dsbsc_demod(Ac, ct, dsbsc_mod):
    return div(mul(ct, dsbsc_mod), Ac)
# Filter untuk AM DSBSC
def dsbsc_filter(order, cutoff, dsbsc_demod):
    n = np.arange(0, order)
    theta = 2*np.pi*cutoff
    h_lpf = (theta/np.pi)*np.sinc(theta*(n-0.5*order/np.pi))
    return sg.convolve(dsbsc_demod, h_lpf, 'same')*4            # Notice di *4 (pengali)

""" Modul simulasi AM SSB (Single Side Band) """
# Fungsi USB (dijadikan hasil modulasi)
def ssb_usb(mt, mh, ctCos, ctSin):
    a = mul(mt, ctCos)
    b = mul(mh, ctSin)
    return sub(a, b)
# Fungsi LSB
def ssb_lsb(mt, mh, ctCos, ctSin):
    a = mul(mt, ctCos)
    b = mul(mh, ctSin)
    return add(a, b)
# Fungsi Demodulasi
def ssb_demod(ssb_usb, ctCos):
    return 2*ssb_usb*ctCos			                            # Update Nanda : (2*ssb_usb*ctCos)*3 tapi hasilnya semakin tidak sesuai
# Fungsi Filter SSB
def ssb_filter(order, cutoff, ssb_demod):
    n = np.arange(0, order)
    theta = 2*np.pi*cutoff
    h_lpf = (theta/np.pi)*np.sinc(theta*(n-0.5*order/np.pi))
    return np.convolve(ssb_demod, h_lpf, 'same')*3.25              # Notice di *4 (pengali) diganti jadi 3.25 biar amplitudonya >= 1

""" Modul Modulasi Frekuensi """
# Fungsi Integrator
def integ(fs, fc, mt, idx):
    t = np.arange(0, 1, (1/fs))
    theta = np.zeros_like(mt)
    for i, t in enumerate(t):
        theta[i] = 2*np.pi*(fc*t + mt[i]*idx)
    return theta
# Fungsi Phase Modulator - output isyarat termodulasi
def phaseMod(Ac, theta):
    return mul(Ac, np.sin(theta))
# Fungsi Differentiator - FM Demodulation
def differ(fmMod):
    return np.diff(fmMod)
# Fungsi Deteksi selubung
def env(differ):
    demod = abs(sg.hilbert(differ))
    demodFFT = np.fft.rfft(demod) * c.rect(-1., np.pi/2)
    newDemod = np.fft.irfft(demodFFT)
    return newDemod

""" Modul Modulasi Digital """
# Fungsi untuk menghasilkan random data dengan jumlah data sebanyak x
def randomData(x):
	# z = np.array([0, 1, 0, 0, 0, 1, 0, 0, 1, 0])
    z = np.random.rand(x)
    z[np.where(z >= 0.5)] = 1
    z[np.where(z < 0.5)]  = 0
    return z
# Fungsi untuk melakukan modulasi digital
def digMod(fs, ctF, x, xSum, plot):
    t = np.arange(0, 2, (1/fs))
    n = np.array(x)
    if plot == 'BFSK':         #N = FREKUENSI deviasi
        n[n > 0] = 5
        n[n == 0] = -5
    elif plot == 'BPSK':
        n[n == 0] = 180
    s = 2*fs/n.size
    d = np.repeat(n, s)
    if plot == 'BASK':
        y = d*np.sin(2*np.pi*ctF*t)
    elif plot == 'BFSK':
        y = np.sin(2*np.pi*(ctF+d)*t)
    elif plot == 'BPSK':
        y= np.sin(2*np.pi*ctF*t+(np.pi*d/180))
    symD = 100
    sign = np.zeros(mul(symD, xSum))
    id_n = np.where(x == 1)
    for i in id_n[0]:
        temp = int(mul(i, symD))
        sign[temp:temp+symD] = 1
    return y,sign
# Ranah frekuensi (?)
def digFreq(y, fs):
    tpCount = len(y)
    values = np.arange(tpCount)
    timePeriod = tpCount/fs
    xf = div(values,timePeriod)[range(tpCount//2)]
    return xf

""" Fungsi Option untuk Isyarat Pemodulasi (message) dan Pembawa (carrier) """
# Fungsi untuk opsi isyarat pemodulasi/signal generator m(t)
def message(plot, Am, fs, Fm):
    if plot == 'sine':
        mt = sine(Am, fs, Fm)
    elif plot == 'cosine':
        mt = cosine(Am, fs, Fm)
    elif plot == 'square':
        mt = square(Am, fs, Fm)
    elif plot == 'sawtooth':
        mt = sawtooth(Am, fs, Fm)
    return mt
# Fungsi untuk opsi isyarat pembawa/signal generator c(t)
def carrier(plot, Ac, fs, Fc):
    if plot == 'sine':
        ct = sine(Ac, fs, Fc)
    elif plot == 'cosine':
        ct = cosine(Ac, fs, Fc)
    elif plot == 'square':
        ct = square(Ac, fs, Fc)
    elif plot == 'sawtooth':
        ct = sawtooth(Ac, fs, Fc)
    return ct

""" Input Signal Generator """
def signalGenerator(plot, Am, fs, fm):
    if plot == 'signal':
        sin = sine(Am, fs, fm)
        cos = cosine(Am, fs, fm)
        squ = square(Am, fs, fm)
        saw = sawtooth(Am, fs, fm)
        Sho = p.all(plot, sin, cos, squ, saw, 'pass', 0, 0, 'timeDomain')
    else:
        x = message(plot, Am, fs, fm)
        Sho = p.one(plot, 'timeDomain', x, 0, 0)
    return Sho

""" Input AM DSBFC """
def amDSBFC(mt, mtA, fs, mtF, ct, ctA, ctF, fcPlot, fcDom):
    mt = message(mt,mtA,fs,mtF)
    ct = carrier(ct,ctA,fs,ctF)
    xf = xProp(mt, fs)
    fcMod = dsbfc_mod(mt,ct)
    fcEnv = envelope(fcMod)
    fcDmd = dsbfc_demod(fcEnv,ctA)
    if fcDom == 'frequencyDomain':
        fcMod = freq(fcMod)
        fcEnv = freq(fcEnv)
        fcDmd = freq(fcDmd)
        mt = freq(mt)
        ct = freq(ct)
    # Fungsi Plotting
    if fcPlot == 'message':
        fcShow = p.one(fcPlot,fcDom,mt,xf,ctF)
    elif fcPlot == 'carrier':
        fcShow = p.one(fcPlot,fcDom,ct,xf,ctF)
    elif fcPlot == 'modulated':
        fcShow = p.one(fcPlot,fcDom,fcMod,xf,ctF)
    elif fcPlot == 'envelope':
        fcShow = p.one(fcPlot,fcDom,fcEnv,xf,ctF)
    elif fcPlot == 'demodulated':
        fcShow = p.one(fcPlot,fcDom,fcDmd,xf,ctF)
    elif fcPlot == 'dsbfc':
        fcShow = p.all(fcPlot,mt,ct,fcMod,fcDmd,fcEnv,xf,ctF,fcDom)
    return fcShow

""" Input AM DSBSC """
def amDSBSC(mt, mtA, fs, mtF, ct, ctA, ctF, orx, cut, scPlot, scDom):
    mt = message(mt,mtA,fs,mtF)
    ct = carrier(ct,ctA,fs,ctF)
    xf = xProp(mt, fs)
    scMod = dsbsc_mod(mt,ct)
    scDmd = dsbsc_demod(ct,scMod,ctA)
    scFil = dsbsc_filter(orx,cut,scDmd)     # Fungsi demodulasi setelah filter (Filter masih mau diupdate)
    if scDom == 'frequencyDomain':
        scMod = freq(scMod)
        scDmd = freq(scDmd)
        scFil = freq(scFil)
        mt = freq(mt)
        ct = freq(ct)
    if scPlot == 'message':
        scShow = p.one(scPlot,scDom,mt,xf,ctF)
    elif scPlot == 'carrier':
        scShow = p.one(scPlot,scDom,ct,xf,ctF)
    elif scPlot == 'modulated':
        scShow = p.one(scPlot,scDom,scMod,xf,ctF)
    elif scPlot == 'demodulated':
        scShow = p.one(scPlot,scDom,scDmd,xf,ctF)
    elif scPlot == 'filtered':
        scShow = p.one(scPlot,scDom,scFil,xf,ctF)
    elif scPlot == 'dsbsc':
        scShow = p.all(scPlot,mt,ct,scMod,scDmd,scFil,xf,ctF,scDom)
    return scShow

""" Input AM SSB """
def amSSB(mt, mtA, fs, mtF, ct, ctA, ctF, mh, mhA, mhF, orx, cut, ssPlot, ssDom):
    if mt == 'sine':
        mh = sine(mhA,fs,mhF)
    elif mt == 'cosine':
        mh = cosine(mhA,fs,mhF)
    mt = message(mt,mtA,fs,mtF)
    ct = carrier(ct,ctA,fs,ctF)
    xf = xProp(mt,fs)
    ctCos = cosine(ctA,fs,ctF)
    ctSin = sine(ctA,fs,ctF)
    ssMod = ssb_usb(mt,mh,ctCos,ctSin)
    ssDmd = ssb_demod(ssMod,ctCos)
    ssFil = ssb_filter(orx,cut,ssDmd)
    if ssDom == 'frequencyDomain':
        ssMod = freq(ssMod)
        ssDmd = freq(ssDmd)
        ssFil = freq(ssFil)
        mt = freq(mt)
        ct = freq(ct)
    if ssPlot == 'message':
        ssShow = p.one(ssPlot,ssDom,mt,xf,ctF)
    elif ssPlot == 'carrier':
        ssShow = p.one(ssPlot,ssDom,ct,xf,ctF)
    elif ssPlot == 'modulated':
        ssShow = p.one(ssPlot,ssDom,ssMod,xf,ctF)
    elif ssPlot == 'demodulated':
        ssShow = p.one(ssPlot,ssDom,ssDmd,xf,ctF)
    elif ssPlot == 'filtered':
        ssShow = p.one(ssPlot,ssDom,ssFil,xf,ctF)
    elif ssPlot == 'ssb':
        ssShow = p.all(ssPlot,mt,ct,ssMod,ssDmd,ssFil,xf,ctF,ssDom)
    return ssShow

""" Input FM Modulation """
def fm(mt, mtA, fs, mtF, ct, ctA, ctF, idx, fmPlot, fmDom):
    mt = message(mt,mtA,fs,mtF)
    ct = carrier(ct,ctA,fs,ctF)
    xf = xProp(mt,fs)
    theta = integ(fs,ctF,mt,idx)
    fmMod = phaseMod(ctA,theta)
    fmDmd = (env(differ(fmMod)))*450   # Dikali 500 untuk menyamakan amplitudo dengan message
    if fmDom == 'frequencyDomain':
        fmMod = freq(fmMod)
        fmDmd = freq(fmDmd)
        mt = freq(mt)
        ct = freq(ct)
    if fmPlot == 'message':
        fmShow = p.one(fmPlot,fmDom,mt,xf,ctF)
    elif fmPlot == 'carrier':
        fmShow = p.one(fmPlot,fmDom,ct,xf,ctF)
    elif fmPlot == 'modulated':
        fmShow = p.one(fmPlot,fmDom,fmMod,xf,ctF)
    elif fmPlot == 'demodulated':
        fmShow = p.one(fmPlot,fmDom,fmDmd,xf,ctF)
    elif fmPlot == 'fm':
        fmShow = p.all(fmPlot,mt,ct,fmMod,fmDmd,fmDmd,xf,ctF,fmDom)
    return fmShow

""" Input Modulasi Digital """
def digital(fs,ctF,xSum,plot):
    t = np.arange(0,2, 1.0/fs)
    x = randomData(xSum)
    if plot == 'digitalModulation':
        y1,sign = digMod(fs,ctF,x,xSum,'BASK')
        y2,sign = digMod(fs,ctF,x,xSum,'BFSK')
        y3,sign = digMod(fs,ctF,x,xSum,'BPSK')
        xf = xProp(y1,fs)
        yf = freq(y1)
        diShow  = p.dig(t,plot,y1,y2,y3,xf,yf,sign)
    else:
        y1,sign = digMod(fs,ctF,x,xSum,plot)
        xf = xProp(y1,fs)
        yf = freq(y1)
        diShow = p.dig(t,plot,y1,0,0,xf,yf,sign)
    return diShow

def inputData(data):
    if data[0] == 'signal-generator':
        amp  = float(data[2])
        fs   = float(data[4])
        freq = float(data[6])
        plot = data[8]
        show = signalGenerator(plot,amp,fs,freq)
    elif data[0] == 'am-dsbfc':
        mt   = data[2]
        mtA  = float(data[4])
        fs   = float(data[6])
        mtF  = float(data[8])
        ct   = data[10]
        ctA  = float(data[12])
        ctF  = float(data[16])
        fcPlot = data[28]
        fcDom  = data[29]
        show = amDSBFC(mt,mtA,fs,mtF,ct,ctA,ctF,fcPlot,fcDom)
    elif data[0] == 'am-dsbsc':
        mt   = data[2]
        mtA  = float(data[4])
        fs   = float(data[6])
        mtF  = float(data[8])
        ct   = data[10]
        ctA  = float(data[12])
        ctF  = float(data[16])
        orx  = float(data[27])
        cut  = float(data[29])
        scPlot = data[31]
        scDom  = data[32]
        show = amDSBSC(mt,mtA,fs,mtF,ct,ctA,ctF,orx,cut,scPlot,scDom)
    elif data[0] == 'am-ssb':
        mt   = data[2]
        mtA  = float(data[4])
        fs   = float(data[6])
        mtF  = float(data[8])
        ct   = data[10]
        ctA  = float(data[12])
        ctF  = float(data[16])
        mh   = data[18]
        mhA  = float(data[20])
        mhF  = float(data[22])
        orx  = float(data[41])
        cut  = float(data[43])
        ssPlot = data[45]
        ssDom  = data[46]
        show = amSSB(mt,mtA,fs,mtF,ct,ctA,ctF,mh,mhA,mhF,orx,cut,ssPlot,ssDom)
    elif data[0] == 'fm-mod':
        mt   = data[2]
        mtA  = float(data[4])
        fs   = float(data[6])
        mtF  = float(data[8])
        ct   = data[10]
        ctA  = float(data[12])
        ctF  = float(data[16])
        idx  = float(data[18])
        fmPlot = data[32]
        fmDom  = data[33]
        show = fm(mt,mtA,fs,mtF,ct,ctA,ctF,idx,fmPlot,fmDom)
    elif data[0] == 'digital-mod':
        fs   = float(data[3])
        ctF  = float(data[5])
        xSum = int(data[8])
        plot = data[10]
        show = digital(fs,ctF,xSum,plot)
    return show

def inputKata(data):
    dictSG = ['amplitude','freq-sampling','frequency','show','signal-generator']
    dictFC = ['add','add(x,carrier)','am-dsbfc','amplitude','as','carrier','demodulated-signal','envelope-signal','freq-sampling','frequency','message','modulated-signal','mutliply(message,carrier)','show','x']
    dictSC = ['add','am-dsbsc','amplitude','as','carrier','cutoff','div(x,carrier.amplitude)','filter','freq-sampling','frequency','message','modulated-signal','mutliply(message,carrier)','mutliply(message,carrier,carrier)','order','show','x']
    dictSS = ['Y','Z','add','add(Y,Z)','am-ssb','amplitude','as','carrier','cutoff','filter','freq-sampling','frequency','hilbert','lsb','message','mutliply(2,usb,carrier.cos)','mutliply(hilbert,carrier.sin)','mutliply(message,carrier.cos)','order','show','subtract(Y,Z)','usb']
    dictFM = ['add','amplitude','as','carrier','demodulated-signal','differentiator','envelope-signal','fm-mod','freq-sampling','frequency','integrator','message','modulated-signal','modulation-index','phase-modulator','show']
    dictDG = ['add','carrier','digital-mod','freq-sampling','frequency','random-data','show']
    if data[0] == 'signal-generator':
        data.pop()
        data.sort()
        del data[0:3]
        x = (data == dictSG)
    elif data[0] == 'am-dsbfc':
        data.pop(2)
        data.pop(9)
        data.pop(26)
        data.pop(26)
        data.sort()
        del data[0:6]
        data = list(dict.fromkeys(data))
        x = (data == dictFC)
    elif data[0] == 'am-dsbsc':
        data.pop(2)
        data.pop(9)
        data.pop(29)
        data.pop(29)
        data.sort()
        del data[0:8]
        data = list(dict.fromkeys(data))
        x = (data == dictSC)
    elif data[0] == 'am-ssb':
        data.pop(2)
        data.pop(9)
        data.pop(16)
        data.pop(42)
        data.pop(42)
        data.sort()
        del data[0:11]
        data = list(dict.fromkeys(data))
        x = (data == dictSS)
    elif data[0] == 'fm-mod':
        data.pop(2)
        data.pop(9)
        data.pop(30)
        data.pop(30)
        data.sort()
        del data[0:7]
        data = list(dict.fromkeys(data))
        x = (data == dictFM)
    elif data[0] == 'digital-mod':
        data.pop()
        data.sort()
        del data[0:3]
        x = (data == dictDG)
    return x
