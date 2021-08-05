import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sg
import scipy.fftpack as fr

""" Modul untuk semua percobaan modulasi """

"""
	Modul Fungsi Matematika
	- Adder			 : Penjumlahan dua bilangan
	- Subtract	 : Pengurangan dua bilangan
	- Multiplier : Perkalian dua bilangan
	- Divide		 : Pembagian dua bilangan
"""

def add(add_1,add_2): 									# Pendefinisian fungsi add
	add_result = add_1+add_2							# Variabel add_result berisi operasi penjumlahan dua bilangan
	return add_result											# Mengembalikan isi variabel add_result

def sub(sub_1,sub_2): 									# Pendefinisian fungsi sub
	sub_result = sub_1-sub_2							# Variabel sub_result berisi operasi pengurangan dua bilangan
	return sub_result											# Mengembalikan isi variabel sub_result

def mul(mul_1,mul_2): 									# Pendefinisian fungsi mul
	mul_result = mul_1*mul_2							# Variabel mul_result berisi operasi perkalian dua bilangan
	return mul_result											# Mengembalikan isi variabel mul_result

def div(div_1,div_2): 									# Pendefinisian fungsi div
	div_result = div_1/div_2							# Variabel div_result berisi operasi pembagian dua bilangan
	return div_result											# Mengembalikan isi variabel div_result

# -----------------------------------------------------------------------------------------------------------------------------

"""
	Modul Signal Generator 
	- Membangkitkan gelombang cosinus
	- Membangkitkan gelombang sinus
	- Membangkitkan gelombang kotak
	- Membangkitkan gelombang segitiga
	- Membangkitkan gelombang carrier
"""

def cosine(Am,fs,fm):																	# Pendefinisian fungsi cosine
	ta 	= 1/fs																					#
	t  	= np.arange(0,1,ta)															#
	cos = Am*np.cos(2*np.pi*fm*t)												#
	return cos																					#

def sine(Am,fs,fm):																		# Pendefinisian fungsi sine
	ta 	= 1/fs																					#
	t  	= np.arange(0,1,ta)															#
	sin = Am*np.sin(2*np.pi*fm*t)												#
	return sin																					#

def square(Am,fs,fm):																	# Pendefinisian fungsi square
	ta 	= 1/fs																					#
	t  	= np.arange(0,1,ta)															#
	sqr = Am*sg.square(2*np.pi*fm*t, duty = 0.3)				#
	return sqr																					#

def sawtooth(Am,fs,fm):																# Pendefinisian fungsi sawtooth
	ta 	= 1/fs																					#
	t  	= np.arange(0,1,ta)															#
	saw = Am*sg.sawtooth(2*np.pi*fm*t, width = 0.5)			#
	return saw																					#

# def carrier(Ac,fs,fc):																# Pendefinisian fungsi carrier
# 	ta  = 1/fs																					#
# 	t   = np.arange(0, 1, ta)														#
# 	car = Ac*np.cos(2*np.pi*fc*t)												#
# 	return car																					#

# -----------------------------------------------------------------------------------------------------------------------------

#INPUT PRAKTIKAN

fs = 1000 																					# fs, ta, t jd awalan kode yg dimasukin waktu prakt (sementara, blm ketemu cara buat langsung dimasukin backcode)
mt = cosine(1,500,5) 																# baris yang diinputkan praktikan, nilai fm diinput sesuai nilai diinginkan. antara cos/sin jg jd pilihan praktikan
ct = cosine(1,500,50) 															# baris yang diinputkan, parameter A, fc

# -----------------------------------------------------------------------------------------------------------------------------

"""
Modul simulasi AM DSBFC (Full Carrier)
- Modulasi AM DSBFC
- Demodulasi AM DSBFC (dengan deteksi selubung)
"""
# Modulasi AM DSBFC
def dsbfc_mod(mt,ct):
	return add(mul(mt,ct),ct)

# Deteksi Envelope AM DSBFC
def envelope(x):
	analytic = sg.hilbert(x)
	return np.abs(analytic)

# Demodulasi AM DSBFC
def dsbfc_demod(envelope,Ac):
	return sub(envelope,Ac)

# mod = dsbfc_mod(mt,ct)
# env = envelope(mod)
# demod = dsbfc_demod(env, 1)

# -----------------------------------------------------------------------------------------------------------------------------

""" 
Modul simulasi AM DSBSC (Suppressed Carrier)
- Modulasi AM DSBSC
- Demodulasi AM DSBSC
"""
# Modulasi AM DSBSC
def dsbsc_mod(mt,ct):
	return mul(mt,ct)

# Demodulasi AM DSBSC
def dsbsc_demod(Ac,ct,dsbsc_mod):
	return div(mul(ct,dsbsc_mod),Ac)

# Filter untuk AM DSBSC
def dsbsc_filter(order,cutoff,dsbsc_demod):
	nyq    = mul(0.5,fs)
	cutoff = cutoff/nyq
	b, a   = sg.butter(order,cutoff,btype='low',analog=False)
	return sg.filtfilt(b,a,dsbsc_demod)

# mod   = dsbsc_mod(mt,ct)
# demod = dsbsc_demod(1,ct,mod)
# filt  = dsbsc_filter(3,10,demod)

# def freq_domain(input):
#     yf = fr.fft(input)/len(input)
#     yf = yf[range(int(len(input)/2))]*2
#     return yf

# mf = freq_domain(mt)
# cf = freq_domain(ct)

# dsbsc_modFreq 		= freq_domain(dsbsc_mod)
# dsbsc_demodFilter = freq_domain(Filter_Demod)/2
# dsbsc_demodFreq		= freq_domain(dsbsc_demod)

# -----------------------------------------------------------------------------------------------------------------------------
""" 
Modul simulasi AM SSB (Single Side Band)
- Modulasi AM SSB
- Demodulasi AM SSB
"""

ctCos = cosine(1,500,5)			# ctCos variabelnya harus sama kayak ctSin
ctSin = sine(1,500,5)
mh    = sine(1,500,5)

def ssb_usb(mt,mh,ctCos,ctSin):
	a = mul(mt,ctCos)
	b = mul(mh,ctSin)
	return sub(a,b)

def ssb_lsb(mt,mh,ctCos,ctSin):
	a = mul(mt,ctCos)
	b = mul(mh,ctSin)
	return add(a,b)

# def ssb_demod(ssb_usb,ctCos):
# 	return 2*ssb_usb*ctCos

def ssb_filter(order,cutoff,ssb_demod):
	nyq    = mul(0.5,fs)
	cutoff = cutoff/nyq
	b, a   = sg.butter(order,cutoff,btype='low',analog=False)
	return sg.filtfilt(b,a,ssb_demod)

lsb   = ssb_lsb(mt,mh,ctCos,ctSin)
mod   = ssb_usb(mt,mh,ctCos,ctSin)
# demod = ssb_demod(ssb_usb,ctCos)
# filt  = ssb_filter(3,10,demod)

# def freq_domain(input):
#     yf = fr.fft(input)/len(input)
#     yf = yf[range(int(len(input)/2))]*2
#     return yf

# Sinyal_Pesan_yf = freq_domain(Sinyal_Pesan)
# usb_yf = freq_domain(SSB_USB)
# lsb_yf = freq_domain(SSB_LSB)
# Filter_Demod_yf = freq_domain(Filter_Demod)/2

# -----------------------------------------------------------------------------------------------------------------------------

""" Plotting - Trial """

# Plotting Figure 1 - Gelombang Sinus, Kotak, Segitiga
plt.figure(figsize=(15,5))

# plt.subplot(2,1,1)
# plt.plot(mod, label='Isyarat Termodulasi USB')
# plt.plot(lsb, label='Isyarat LSB')
# plt.plot(filt, label='Isyarat Demodulasi setelah Filter')
# plt.title('Isyarat Gelombang Sinus')
# plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.legend()

# plt.subplot(2,1,2)
# plt.plot(dsbfc_demod(cosine(1,500,5),carrier(1,500,50)))
# plt.title('Isyarat Gelombang Kotak')
# plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')

# plt.subplot(3,1,3)
# plt.plot(sawtooth(1,500,5))
# plt.title('Isyarat Gelombang Segitiga')
# plt.grid(b=True, which='major', color='#666666', linestyle='-')
# plt.minorticks_on()
# plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')

# plt.tight_layout()
# plt.show()

# -----------------------------------------------------------------------------------------------------------------------------
