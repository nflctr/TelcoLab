import numpy as np
import scipy.signal as sg
import scipy.fftpack as fr
import cmath as c
import telcoWeb.plot as p
# -----------------------------------------------------------------------------------------------------------------------------
""" Modul Fungsi Matematika """
# Fungsi Adder (Penambahan)
def add(add_1, add_2): 																# Pendefinisian fungsi add
	add_result = add_1+add_2														# Variabel add_result berisi operasi penjumlahan dua bilangan
	return add_result																		# Mengembalikan isi variabel add_result
# Fungsi sub (pengurangan)
def sub(sub_1, sub_2): 																# Pendefinisian fungsi sub
	sub_result = sub_1-sub_2														# Variabel sub_result berisi operasi pengurangan dua bilangan
	return sub_result																		# Mengembalikan isi variabel sub_result
# Fungsi multiplier (Perkalian)
def mul(mul_1, mul_2): 																# Pendefinisian fungsi mul
	mul_result = mul_1*mul_2														# Variabel mul_result berisi operasi perkalian dua bilangan
	return mul_result																		# Mengembalikan isi variabel mul_result
# Fungsi division (pembagian)
def div(div_1, div_2): 																# Pendefinisian fungsi div
	div_result = div_1/div_2														# Variabel div_result berisi operasi pembagian dua bilangan
	return div_result																		# Mengembalikan isi variabel div_result
# -----------------------------------------------------------------------------------------------------------------------------
""" Modul Signal Generator """
# Fungsi gelombang cosinus
def cosine(Am, fs, fm):																# Pendefinisian fungsi cosine
	ta = 1/fs																						# Step waktu yang digunakan
	t = np.arange(0, 1, ta)															# Time interval dari 0s ke 1s dengan step ta
	cos = Am*np.cos(2*np.pi*fm*t)												# Fungsi utama
	return cos																					# Mengembalikan nilai cos
# Fungsi gelombang sinus
def sine(Am, fs, fm):																	# Pendefinisian fungsi sine
	ta = 1/fs																						# Step waktu yang digunakan
	t = np.arange(0, 1, ta)															# Time interval dari 0s ke 1s dengan step ta
	sin = Am*np.sin(2*np.pi*fm*t)												# Fungsi utama
	return sin																					# Mengembalikan nilai sin
# Fungsi gelombang kotak
def square(Am, fs, fm):																# Pendefinisian fungsi square
	ta = 1/fs																						# Step waktu yang digunakan
	t = np.arange(0, 1, ta)															# Time interval dari 0s ke 1s dengan step ta
	sqr = Am*sg.square(2*np.pi*fm*t, duty=0.3)					# Fungsi utama
	return sqr																					# Mengembalikan nilai squ
# Fungsi gelombang segitiga
def sawtooth(Am, fs, fm):															# Pendefinisian fungsi sawtooth
	ta = 1/fs																						# Step waktu yang digunakan
	t = np.arange(0, 1, ta)															# Time interval dari 0s ke 1s dengan step ta
	saw = Am*sg.sawtooth(2*np.pi*fm*t, width=0.5)				# Fungsi utama
	return saw																					# Mengembalikan nilai saw
# -----------------------------------------------------------------------------------------------------------------------------
""" Modul untuk Frequency Domain """
# Frequency Domain
def freq(y):
	yf = div(fr.fft(y), len(y))													# Fourier Transform
	yf = mul(yf[range(int(div(len(y), 2)))], 2)					# Perkalian hasil yf sebelumnya
	return np.abs(yf)
# Frequency Domain - X axis Properties
def xProp(mt, fs):
	tpCount = len(mt)                        						# Hasil panjang isyarat input
	values = np.arange(int(tpCount/2))      						#
	timePeriod = tpCount/fs															# Periode -> hasil bagi 'tpCount' dengan frekuensi sampling
	xf = values/timePeriod              								# Hasil plot sumbu x pada freq. domain
	return xf
# -----------------------------------------------------------------------------------------------------------------------------
""" Modul simulasi AM DSBFC (Full Carrier) """
# Modulasi AM DSBFC
def dsbfc_mod(mt, ct):																
	return add(mul(mt, ct), ct)													# Modulasi DSBFC (mt*ct)+ct									
# Deteksi Envelope AM DSBFC
def envelope(x):
	analytic = sg.hilbert(x)														# Deteksi menggunakan analytic signal (Hilbert)
	return np.abs(analytic)															# Mengembalikan nilai mutlak dari hasil Hilbert di atas
# Demodulasi AM DSBFC
def dsbfc_demod(envelope, Ac):
	return sub(envelope, Ac)														# Mengurangi hasil envelope dengan amplitudo carrier
# -----------------------------------------------------------------------------------------------------------------------------
""" Modul simulasi AM DSBSC (Suppressed Carrier) """
# Modulasi AM DSBSC
def dsbsc_mod(mt, ct):																					
	return mul(mt, ct)																						# Modulasi DSBSC (mt*ct)
# Demodulasi AM DSBSC
def dsbsc_demod(Ac, ct, dsbsc_mod):															#
	return div(mul(ct, dsbsc_mod), Ac)														#
# Filter untuk AM DSBSC
def dsbsc_filter(order, cutoff, dsbsc_demod):										
	n = np.arange(0, order)																				#
	theta = 2*np.pi*cutoff																				#
	h_lpf = (theta/np.pi)*np.sinc(theta*(n-0.5*order/np.pi))			#
	return sg.convolve(dsbsc_demod, h_lpf, 'same')*4							#
# -----------------------------------------------------------------------------------------------------------------------------
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
	return 2*ssb_usb*ctCos																					# Update Nanda : (2*ssb_usb*ctCos)*3 tapi hasilnya semakin tidak sesuai
# Fungsi Filter SSB
def ssb_filter(order, cutoff, ssb_demod):
	n = np.arange(0, order)
	theta = 2*np.pi*cutoff
	h_lpf = (theta/np.pi)*np.sinc(theta*(n-0.5*order/np.pi))
	return np.convolve(ssb_demod, h_lpf, 'same')
# -----------------------------------------------------------------------------------------------------------------------------
""" Modul Modulasi Frekuensi """
# Fungsi Integrator
def integ(fs, fc, mt, idx):
	ta = 1/fs																											#
	t = np.arange(0, 1, ta)																				#
	theta = np.zeros_like(mt)																			#
	for i, t in enumerate(t):
		theta[i] = 2*np.pi*(fc*t + mt[i]*idx)												#
	return theta
# Fungsi Phase Modulator - output isyarat termodulasi
def phaseMod(Ac, theta):
	return mul(Ac, np.sin(theta))																	#
# Fungsi Differentiator - FM Demodulation
def differ(fmMod):
	return np.diff(fmMod)																					#
# Fungsi Deteksi selubung
def env(differ):
	demod = abs(sg.hilbert(differ))																#
	demodFFT = np.fft.rfft(demod) * c.rect(-1., np.pi/2)					#
	newDemod = np.fft.irfft(demodFFT)*450													# Ada koreksi di pengali, harus diubah manual untuk menyesuaikan tampilan akhir
	return newDemod
# -----------------------------------------------------------------------------------------------------------------------------
""" Modul Modulasi Digital """
# Fungsi untuk menghasilkan random data dengan jumlah data sebanyak x
def randomData(x):
	y = np.random.rand(x)																# Menghasilkan random data (dari 0 ke 1) sejumlah x, hasilnya array
	y[np.where(y >= 0.5)] = 1														# Seleksi random data (suku array ke berapa), kalau >= 0.5 diconvert ke 1
	y[np.where(y < 0.5)]  = 0														# Seleksi random data (suku array ke berapa), kalau < 0.5 diconvert ke 0
	return y

def digiMod(fs, fc, x, tipe):
	t = np.arange(0, 2, 1/fs)														# Range waktu
	n = np.array(x)																			# n Array Data
	if tipe == 'bfsk':
		n[n > 0] = 5																			# Mengubah nilai bit sesuai dengan modulasi
		n[n < 0] = -5																			# Mengubah nilai bit sesuai dengan modulasi
	elif tipe == 'bpsk':
		n[n > 0] = 180																		# Mengubah nilai bit sesuai dengan modulasi
	s = 2*fs/n.size  																		# samples per bit
	d = np.repeat(n, s)  																# Perulangan nilai n sebanyak sampel p
	if tipe == 'bask':
		y = d*np.sin(2*np.pi*fc*t)												# Persamaan modulasi sesuai tipe
	elif tipe == 'bfsk':
		y = np.sin(2*np.pi*(fc+d)*t)											# Persamaan modulasi sesuai tipe
	elif tipe == 'bpsk':
		y= np.sin(2*np.pi*fc*t+(np.pi*d/180))							# Persamaan modulasi sesuai tipe
	return y

def digiTime(x, xSum):
	symD = 100																					# Symduration = durasi isyarat
	sign = np.zeros(mul(symD,xSum)) 										# 
	id_n = np.where(x == 1)															# mencari nilai data untuk kondisi ketika bernilai sama
	for i in id_n[0]:																		# sama sampe bawah
		temp = int(mul(i,symD))														# 
		sign[temp:temp+symD] = 1													# 
	return sign

def digiFreq(y, fs):
	tpCount = len(y)                        						# Hasil panjang isyarat input
	values = np.arange(tpCount)      										#
	timePeriod = tpCount/fs															# Periode -> hasil bagi 'tpCount' dengan frekuensi sampling
	xf = div(values,timePeriod)[range(tpCount//2)]      # Hasil plot sumbu x pada freq. domain
	return xf

def Freq(y):
	n = len(y)
	z = np.fft.fft(y)/n[range(n//2)]
	return abs(z)
# -----------------------------------------------------------------------------------------------------------------------------
def dg(tipe, fs, fc, Sum, plot):
	t = np.arange(0,2, 1.0/fs)
	x = randomData(Sum)
	mt = digiMod(fs, fc, x, tipe)
	mod = digiTime(x, Sum)
	modF = digiFreq(mt, fs)
	modZ = Freq(mt)
	if plot == 'message':
		diShow = p.diOne(plot, mt)
	elif plot == 'modulated-timeDomain':
		diShow = p.diOne(plot, mod)
	# elif plot == 'modulated-frequencyDomain':
	# 	diShow = 
	elif plot == 'digitalModulation':
		diShow = p.diAll(mt, mod, modF, modZ)
	return diShow
# -----------------------------------------------------------------------------------------------------------------------------
""" Fungsi Option untuk Isyarat Pemodulasi (message) dan Pembawa (carrier) """
# Fungsi untuk opsi isyarat pemodulasi/signal generator m(t)
def message(plot, Am, fs, Fm):
	if plot == 'sine':
		mt = sine(Am, fs, Fm)                 # Menghasilkan gelombang sinus
	elif plot == 'cosine':											
		mt = cosine(Am, fs, Fm)								# Menghasilkan gelombang cosinus
	elif plot == 'square':
		mt = square(Am, fs, Fm)               # Menghasilkan gelombang kotak
	elif plot == 'sawtooth':										
		mt = sawtooth(Am, fs, Fm)							# Menghasilkan gelombang segitiga
	return mt
# Fungsi untuk opsi isyarat pembawa/signal generator c(t)
def carrier(plot, Ac, fs, Fc):
	if plot == 'sine':
		ct = sine(Ac, fs, Fc)                 # Menghasilkan gelombang sinus
	elif plot == 'cosine':											
		ct = cosine(Ac, fs, Fc)								# Menghasilkan gelombang cosinus
	elif plot == 'square':
		ct = square(Ac, fs, Fc)               # Menghasilkan gelombang kotak
	elif plot == 'sawtooth':										
		ct = sawtooth(Ac, fs, Fc)							# Menghasilkan gelombang segitiga
	return ct
# -----------------------------------------------------------------------------------------------------------------------------
"""
Input Signal Generator
	- signal amp a fs b freq c      # Generate signal generator
	- show plot                     # Menampilkan grafik
	a = Amplitudo                   c = Frekuensi isyarat
	b = Frekuensi sampling          x = jenis gelombang yang mau ditampilkan
"""
def signalGenerator(plot, Am, fs, fm):
	dom = 'timeDomain'
	xf, ctF = 0
	if plot == 'signal':													# Khusus kalau plot = signal, semua gelombang digenerate dan direturn ke plot
		sin = sine(Am, fs, fm)
		cos = cosine(Am, fs, fm)
		squ = square(Am, fs, fm)
		saw = sawtooth(Am, fs, fm)
		Sho = p.sigAll(sin, cos, squ, saw)
	else:																					# Kalau plot cuma satu jenis gelombang, masuk ke fungsi message di atas
		x = message(plot, Am, fs, fm)
		Sho = p.one(plot, dom, x, xf, ctF)
	return Sho
# -----------------------------------------------------------------------------------------------------------------------------
"""
Input AM DSBFC
  - message x amp a fs b freq c         # Generate isyarat pemodulasi m(t)
  - carrier x amp a fs b freq c         # Generate isyarat pembawa c(t)
  - mul(message,carrier) as *           # Modulasi DSBFC -- (mt*ct)
  - add(*,carrier) as modulated         # Modulasi DSBFC -- (mt*ct)+ct                            
  - add envelope as demodulated         # Demodulasi DSBFC -- deteksi envelope
  - show plot                           # Menampilkan grafik hasil demodulasi
  a = Amplitudo                         c = Frekuensi isyarat
  b = Frekuensi sampling                x = jenis gelombang yang mau digunakan"""
def amDSBFC(mt, mtA, fs, mtF, ct, ctA, ctF, fcPlot, fcDom): 
	mt = message(mt, mtA, fs, mtF)															# Fungsi isyarat message
	ct = carrier(ct, ctA, fs, ctF)															# Fungsi isyarat carrier
	xf = xProp(mt, fs)																					# Fungsi x axis properties untuk frekuensi
	fcModT   = dsbfc_mod(mt,ct)             										# Fungsi modulasi        
	fcEnvT   = envelope(fcModT)             										# Fungsi deteksi selubung
	fcDemodT = dsbfc_demod(fcEnvT, ctA)     										# Fungsi demodulasi
	if fcPlot == 'message-timeDomain':
		fcShow = p.one(fcPlot,mt)																	# Plotting untuk waveform isyarat pemodulasi 
	elif fcPlot == 'carrier-timeDomain':
		fcShow = p.one(fcPlot,ct)																	# Plotting untuk waveform isyarat pembawa    
	elif fcPlot == 'modulated-timeDomain':
		fcShow = p.one(fcPlot,fcModT)															# Plotting untuk waveform isyarat termodulasi
	elif fcPlot == 'envelope-timeDomain':
		fcShow = p.one(fcPlot,fcEnvT)															# Plotting untuk waveform deteksi selubung   
	elif fcPlot == 'demodulated-timeDomain':
		fcShow = p.one(fcPlot,fcDemodT)														# Plotting untuk waveform isyarat demodulasi 
	elif fcPlot == 'dsbfc-timeDomain':
		fcShow = p.dsbfcT(mt, ct, fcModT, fcEnvT, fcDemodT)				# Plotting untuk waveform semua tahap
	if fcPlot == 'message-frequencyDomain':
		fcShow = p.fcF(fcPlot,xf,freq(mt))                        # Plotting untuk waveform isyarat pemodulasi  
	elif fcPlot == 'carrier-frequencyDomain':
		fcShow = p.fcF(fcPlot,xf,freq(ct))                        # Plotting untuk waveform isyarat pembawa     
	elif fcPlot == 'modulated-frequencyDomain':
		fcShow = p.fcF(fcPlot,xf,freq(fcModT))                    # Plotting untuk waveform isyarat termodulasi
	elif fcPlot == 'envelope-frequencyDomain':
		fcShow = p.fcF(fcPlot,xf,freq(fcEnvT))                    # Plotting untuk waveform deteksi selubung      
	elif fcPlot == 'demodulated-frequencyDomain':
		fcShow = p.fcF(fcPlot,xf,freq(fcDemodT))                  # Plotting untuk waveform isyarat demodulasi 
	elif fcPlot == 'dsbfc-frequencyDomain':
		fcShow = p.dsbfcF(xf,freq(mt),freq(ct),freq(fcModT),freq(fcEnvT),freq(fcDemodT))  																				# Plotting untuk waveform semua tahap        
	return fcShow
# -----------------------------------------------------------------------------------------------------------------------------
"""
Input AM DSBSC
  - message x amp a fs b freq c         # Generate isyarat pemodulasi m(t)
  - carrier x amp a fs b freq c         # Generate isyarat pembawa c(t)
  - mul(message,carrier) as modulated   # Modulasi DSBSC -- (mt*ct)                        
  - mul(message,carrier,carrier) as **  # Demodulasi DSBSC -- (mt*ct*ct)
  - div(**,carrier.amp)                 # Demodulasi DSBSC -- (mt*ct*ct)/Ac
  - add filter order y cutoff z         # Demodulasi DSBSC -- filtering
  - show plot                           # Menampilkan grafik hasil demodulasi
  a = Amplitudo                         c = Frekuensi isyarat
  b = Frekuensi sampling                x = jenis gelombang yang mau digunakan
  y = order dari filter                 z = Frekuensi cutoff filter""" 
def amDSBSC(mt, mtA, fs, mtF, ct, ctA, ctF, scPlot, orx, cut):
	mt = message(mt, mtA, fs, mtF)															# Fungsi isyarat message
	ct = carrier(ct, ctA, fs, ctF)															# Fungsi isyarat carrier
	xf = xProp(mt, fs)																					# Fungsi x axis properties untuk frekuensi
	scModT   = dsbsc_mod(mt,ct)                 								# Fungsi modulasi               
	scDemodT = dsbsc_demod(ct,scModT,ctA)       								# Fungsi demodulasi  
	scFiltT  = dsbsc_filter(orx,cut,scDemodT)   								# Fungsi demodulasi setelah filter (Filter masih mau diupdate)
	
	if scPlot == 'message-timeDomain':
		scShow = p.one(scPlot,mt)                             		# Plotting untuk waveform isyarat pemodulasi
	elif scPlot == 'carrier-timeDomain':
		scShow = p.one(scPlot,ct)                             		# Plotting untuk waveform isyarat pembawa   
	elif scPlot == 'modulated-timeDomain':
		scShow = p.one(scPlot,scModT)                         		# Plotting untuk waveform isyarat termodulas
	elif scPlot == 'demodulated-timeDomain':
		scShow = p.one(scPlot,scDemodT)                       		# Plotting untuk waveform isyarat demodulasi  
	elif scPlot == 'filtered-timeDomain':
		scShow = p.one(scPlot,scFiltT)                        		# Plotting untuk waveform isyarat demodulasi setelah filter
	elif scPlot == 'dsbsc-timeDomain':
		scShow = p.dsbscT(mt,ct,scModT,scDemodT,scFiltT)      		# Plotting untuk waveform semua tahap       

	if scPlot == 'message-frequencyDomain':
		scShow = p.scF(scPlot,xf,freq(mt))                        # Plotting untuk waveform isyarat pemodulasi
	elif scPlot == 'carrier-frequencyDomain':
		scShow = p.scF(scPlot,xf,freq(ct))                        # Plotting untuk waveform isyarat pembawa   
	elif scPlot == 'modulated-frequencyDomain':
		scShow = p.scF(scPlot,xf,freq(scModT))                    # Plotting untuk waveform isyarat termodulas
	elif scPlot == 'demodulated-frequencyDomain':
		scShow = p.scF(scPlot,xf,freq(scDemodT))                  # Plotting untuk waveform isyarat demodulasi  
	elif scPlot == 'filtered-frequencyDomain':
		scShow = p.scF(scPlot,xf,freq(scFiltT))                   # Plotting untuk waveform isyarat demodulasi setelah filter
	elif scPlot == 'dsbsc-frequencyDomain':
		scShow = p.dsbscF(
			xf,
			freq(mt),
			freq(ct),
			freq(scModT),
			freq(scDemodT),
			freq(scFiltT))    																			# Plotting untuk waveform semua tahap       
	return scShow
# -----------------------------------------------------------------------------------------------------------------------------
"""
Input AM SSB
  - message x amp a fs b freq c         # Generate isyarat pemodulasi m(t)
  - carrier x amp a fs b freq c         # Generate isyarat pembawa c(t) cos dan sin
  - hilbert x amp a fs b freq c         # Generate isyarat Hilbert(?)
  - mul(message,carrier.cos) as A       # Generate a = mt*ct(cos)
  - mul(hilbert,carrier.sin) as B       # Generate b = mt*ct(cos)
  - sub(A,B) as usb                     # Generate USB = a-b
  - add(A,B) as lsb                     # Generate LSB = a+b
  - mul(2,usb,carrier.cos)              # Demodulasi SSB -- (2*usb*ct(cos))
  - add filter order y cutoff z         # Demodulasi SSB -- filtering
  - show plot                           # Menampilkan grafik hasil demodulasi
  a = Amplitudo                         c = Frekuensi isyarat
  b = Frekuensi sampling                x = jenis gelombang yang mau digunakan """
def amSSB(mt, mtA, fs, mtF, ct, ctA, ctF, mh, mhA, mhF, ssPlot, orx, cut):
	if mt == 'sine':
		mh    = sine(mhA,fs,mhF)              										# Isyarat Hilbert Transform saat isyarat message sin
	elif mt == 'cosine':
		mh    = cosine(mhA,fs,mhF)              									# Isyarat Hilbert Transform saat isyarat message cos
	mt = message(mt, mtA, fs, mtF)															# Fungsi isyarat message
	ct = carrier(ct, ctA, fs, ctF)															# Fungsi isyarat carrier
	xf = xProp(mt, fs)																					# Fungsi x axis properties untuk frekuensi
	ctCos = cosine(ctA,fs,ctF)              										# Isyarat pembawa (cosinus)
	ctSin = sine(ctA,fs,ctF)                										# Isyarat pembawa (sinus)
	
	ssModT   = ssb_usb(mt,mh,ctCos,ctSin)   										# Fungsi modulasi               
	ssDemodT = ssb_demod(ssModT,ctCos)      										# Fungsi demodulasi  
	ssFiltT  = ssb_filter(orx,cut,ssDemodT) 										# Fungsi demodulasi setelah filter (Filter masih mau diupdate)
  
	if ssPlot == 'message-timeDomain':
		ssShow = p.ssT(ssPlot,mt)                             		# Plotting untuk waveform isyarat pemodulasi
	elif ssPlot == 'carrier-timeDomain':
		ssShow = p.ssT(ssPlot,ctCos)                          		# Plotting untuk waveform isyarat pembawa   
	elif ssPlot == 'modulated-timeDomain':
		ssShow = p.ssT(ssPlot,ssModT)                         		# Plotting untuk waveform isyarat termodulas
	elif ssPlot == 'demodulated-timeDomain':
		ssShow = p.ssT(ssPlot,ssDemodT)                       		# Plotting untuk waveform isyarat demodulasi  
	elif ssPlot == 'filtered-timeDomain':
		ssShow = p.ssT(ssPlot,ssFiltT)                        		# Plotting untuk waveform isyarat demodulasi setelah filter
	elif ssPlot == 'ssb-timeDomain':
		ssShow = p.ssbT(mt,ctCos,ssModT,ssDemodT,ssFiltT)     		# Plotting untuk waveform semua tahap       

	if ssPlot == 'message-frequencyDomain':
		ssShow = p.ssF(ssPlot,xf,freq(mt))                        # Plotting untuk waveform isyarat pemodulasi
	elif ssPlot == 'carrier-frequencyDomain':
		ssShow = p.ssF(ssPlot,xf,freq(ct))                        # Plotting untuk waveform isyarat pembawa   
	elif ssPlot == 'modulated-frequencyDomain':
		ssShow = p.ssF(ssPlot,xf,freq(ssModT))                    # Plotting untuk waveform isyarat termodulas
	elif ssPlot == 'demodulated-frequencyDomain':
		ssShow = p.ssF(ssPlot,xf,freq(ssDemodT))                  # Plotting untuk waveform isyarat demodulasi  
	elif ssPlot == 'filtered-frequencyDomain':
		ssShow = p.ssF(ssPlot,xf,freq(ssFiltT))                   # Plotting untuk waveform isyarat demodulasi setelah filter
	elif ssPlot == 'ssb-frequencyDomain':
		ssShow = p.ssbF(
			xf,
			freq(mt),
			freq(ct),
			freq(ssModT),
			freq(ssDemodT),
			freq(ssFiltT))      																		# Plotting untuk waveform semua tahap
	return ssShow
# -----------------------------------------------------------------------------------------------------------------------------
"""
Input FM Modulation
  - message x amp a fs b freq c         # Generate isyarat pemodulasi m(t)
  - carrier x amp a fs b freq c         # Generate isyarat pembawa c(t)
  - modulation-index d                  # Input indeks modulasi
  - add integrator                      # Modulasi FM -- Menambahkan integrator
  - add phase-modulator as modulated    # Modulasi FM -- Menambahkan phase modulator
  - add differentiator                  # Demodulasi FM -- diskriminasi frekuensi
  - add envelope as demodulated         # Demodulasi FM -- deteksi selubung
  - show plot                           # Menampilkan grafik hasil demodulasi
  a = Amplitudo                         c = Frekuensi isyarat, d = indeks modulasi
  b = Frekuensi sampling                x = jenis gelombang yang mau digunakan """
def fm(mt, mtA, fs, mtF, ct, ctA, ctF, idx, fmPlot):
	mt = message(mt, mtA, fs, mtF)															# Fungsi isyarat message
	ct = carrier(ct, ctA, fs, ctF)															# Fungsi isyarat carrier
	xf = xProp(mt, fs)																					# Fungsi x axis properties untuk frekuensi
	theta    = integ(fs,ctF,mt,idx)															#
	fmModT   = phaseMod(ctA,theta)															#
	fmDemodT = env(differ(fmModT))															#
	
	if fmPlot == 'message-timeDomain':
		fmShow = p.fmT(fmPlot,mt)                             		# Plotting untuk waveform isyarat pemodulasi
	elif fmPlot == 'carrier-timeDomain':
		fmShow = p.fmT(fmPlot,ct)                             		# Plotting untuk waveform isyarat pembawa   
	elif fmPlot == 'modulated-timeDomain':
		fmShow = p.fmT(fmPlot,fmModT)                         		# Plotting untuk waveform isyarat termodulas
	elif fmPlot == 'demodulated-timeDomain':
		fmShow = p.fmT(fmPlot,fmDemodT)                       		# Plotting untuk waveform isyarat demodulasi  
	elif fmPlot == 'fm-timeDomain':
		fmShow = p.fmAllT(mt,ct,fmModT,fmDemodT)              		# Plotting untuk waveform semua tahap       

	if fmPlot == 'message-frequencyDomain':
		fmShow = p.fmF(fmPlot,xf,ctF,freq(mt))                    # Plotting untuk waveform isyarat pemodulasi
	elif fmPlot == 'carrier-frequencyDomain':
		fmShow = p.fmF(fmPlot,xf,ctF,freq(ct))                    # Plotting untuk waveform isyarat pembawa   
	elif fmPlot == 'modulated-frequencyDomain':
		fmShow = p.fmF(fmPlot,xf,ctF,freq(fmModT))                # Plotting untuk waveform isyarat termodulas
	elif fmPlot == 'demodulated-frequencyDomain':
		fmShow = p.fmF(fmPlot,xf,ctF,freq(fmDemodT))              # Plotting untuk waveform isyarat demodulasi  
	elif fmPlot == 'fm-frequencyDomain':
		fmShow = p.fmAllF(xf,ctF,freq(mt),freq(ct),freq(fmModT),freq(fmDemodT)) # Plotting untuk waveform semua tahap
	return fmShow
# -----------------------------------------------------------------------------------------------------------------------------
