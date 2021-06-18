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
	a = mul(mt, ctCos)																						#
	b = mul(mh, ctSin)																						#
	return sub(a, b)																							#
# Fungsi LSB
def ssb_lsb(mt, mh, ctCos, ctSin):
	a = mul(mt, ctCos)																						#
	b = mul(mh, ctSin)																						#
	return add(a, b)																							#
# Fungsi Demodulasi
def ssb_demod(ssb_usb, ctCos):
	return 2*ssb_usb*ctCos																				# Update Nanda : (2*ssb_usb*ctCos)*3 tapi hasilnya semakin tidak sesuai
# Fungsi Filter SSB
def ssb_filter(order, cutoff, ssb_demod):
	n = np.arange(0, order)																				#
	theta = 2*np.pi*cutoff																				#
	h_lpf = (theta/np.pi)*np.sinc(theta*(n-0.5*order/np.pi))			#
	return np.convolve(ssb_demod, h_lpf, 'same')*4									#
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
	return newDemod																								#
# -----------------------------------------------------------------------------------------------------------------------------
""" Modul Modulasi Digital """
# Fungsi untuk menghasilkan random data dengan jumlah data sebanyak x
def randomData(x):
	# z = np.array([0, 1, 0, 0, 0, 1, 0, 0, 1, 0])
	z = np.random.rand(x)																# Menghasilkan random data (dari 0 ke 1) sejumlah x, hasilnya array
	z[np.where(z >= 0.5)] = 1														# Seleksi random data (suku array ke berapa), kalau >= 0.5 diconvert ke 1
	z[np.where(z < 0.5)]  = 0														# Seleksi random data (suku array ke berapa), kalau < 0.5 diconvert ke 0
	return z
# Fungsi untuk melakukan modulasi digital
def digMod(fs,ctF,x,xSum,plot):
	t = np.arange(0, 2, 1/fs)														# Range waktu
	n = np.array(x)																			# n Array Data
	if plot == 'BFSK':
		n[n > 0] = 5																			# Mengubah nilai bit sesuai dengan modulasi
		n[n < 0] = -5																			# Mengubah nilai bit sesuai dengan modulasi
	elif plot == 'BPSK':
		n[n > 0] = 180																		# Mengubah nilai bit sesuai dengan modulasi
	s = 2*fs/n.size  																		# samples per bit
	d = np.repeat(n, s)  																# Perulangan nilai n sebanyak sampel p
	if plot == 'BASK':
		y = d*np.sin(2*np.pi*ctF*t)												# Persamaan modulasi sesuai tipe
	elif plot == 'BFSK':
		y = np.sin(2*np.pi*(ctF+d)*t)											# Persamaan modulasi sesuai tipe
	elif plot == 'BPSK':
		y= np.sin(2*np.pi*ctF*t+(np.pi*d/180))						# Persamaan modulasi sesuai tipe
	symD = 100																					# Symduration = durasi isyarat
	sign = np.zeros(mul(symD,xSum)) 										# 
	id_n = np.where(x == 1)															# mencari nilai data untuk kondisi ketika bernilai sama
	for i in id_n[0]:																		# sama sampe bawah
		temp = int(mul(i,symD))														# 
		sign[temp:temp+symD] = 1													#
	return y,sign
# Ranah frekuensi (?)
def digFreq(y,fs):
	tpCount = len(y)                        						# Hasil panjang isyarat input
	values = np.arange(tpCount)      										#
	timePeriod = tpCount/fs															# Periode -> hasil bagi 'tpCount' dengan frekuensi sampling
	xf = div(values,timePeriod)[range(tpCount//2)]      # Hasil plot sumbu x pada freq. domain
	return xf
# -----------------------------------------------------------------------------------------------------------------------------
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
""" Input Signal Generator """
def signalGenerator(plot,Am,fs,fm):
	if plot == 'signal':																										# Khusus kalau plot = signal, semua gelombang digenerate dan direturn ke plot
		sin = sine(Am,fs,fm)																									# Membangkitkan gelombang sinus
		cos = cosine(Am,fs,fm)																								# Membangkitkan gelombang cosinus
		squ = square(Am,fs,fm)																								# Membangkitkan gelombang kotak
		saw = sawtooth(Am,fs,fm)																							# Membangkitkan gelombang segitiga
		Sho = p.all(plot,sin,cos,squ,saw,'pass',0,0,'timeDomain')							# Plotting seluruh gelombang 
	else:																																		# Kalau plot cuma satu jenis gelombang, masuk ke fungsi message di atas
		x = message(plot,Am,fs,fm)																						# Membangkitkan gelombang
		Sho = p.one(plot,'timeDomain',x,0,0)																	# Plotting Gelombang
	return Sho
# -----------------------------------------------------------------------------------------------------------------------------
""" Input AM DSBFC """
def amDSBFC(mt,mtA,fs,mtF,ct,ctA,ctF,fcPlot,fcDom):
	mt = message(mt,mtA,fs,mtF)												# Fungsi isyarat message
	ct = carrier(ct,ctA,fs,ctF)												# Fungsi isyarat carrier
	xf = xProp(mt, fs)																# Fungsi x axis properties untuk frekuensi
	fcMod = dsbfc_mod(mt,ct)             							# Fungsi modulasi        
	fcEnv = envelope(fcMod)             							# Fungsi deteksi selubung
	fcDmd = dsbfc_demod(fcEnv,ctA)     								# Fungsi demodulasi
	if fcDom == 'frequencyDomain':
		fcMod = freq(fcMod)             								# Fungsi modulasi        
		fcEnv = freq(fcEnv)             								# Fungsi deteksi selubung
		fcDmd = freq(fcDmd)     												# Fungsi demodulasi
		mt = freq(mt)
		ct = freq(ct)
	# Fungsi Plotting
	if fcPlot == 'message':
		fcShow = p.one(fcPlot,fcDom,mt,xf,ctF)										# Plotting untuk waveform isyarat pemodulasi 
	elif fcPlot == 'carrier':
		fcShow = p.one(fcPlot,fcDom,ct,xf,ctF)										# Plotting untuk waveform isyarat pembawa    
	elif fcPlot == 'modulated':
		fcShow = p.one(fcPlot,fcDom,fcMod,xf,ctF)									# Plotting untuk waveform isyarat termodulasi
	elif fcPlot == 'envelope':
		fcShow = p.one(fcPlot,fcDom,fcEnv,xf,ctF)									# Plotting untuk waveform deteksi selubung   
	elif fcPlot == 'demodulated':
		fcShow = p.one(fcPlot,fcDom,fcDmd,xf,ctF)									# Plotting untuk waveform isyarat demodulasi
	elif fcPlot == 'dsbfc':
		fcShow = p.all(fcPlot,mt,ct,fcMod,fcDmd,fcEnv,xf,ctF,fcDom)		# Plotting untuk waveform semua tahap        
	return fcShow
# -----------------------------------------------------------------------------------------------------------------------------
""" Input AM DSBSC """ 
def amDSBSC(mt, mtA, fs, mtF, ct, ctA, ctF, orx, cut, scPlot, scDom):
	mt = message(mt,mtA,fs,mtF)												# Fungsi isyarat message
	ct = carrier(ct,ctA,fs,ctF)												# Fungsi isyarat carrier
	xf = xProp(mt, fs)																# Fungsi x axis properties untuk frekuensi
	scMod = dsbsc_mod(mt,ct)                 					# Fungsi modulasi               
	scDmd = dsbsc_demod(ct,scMod,ctA)       					# Fungsi demodulasi  
	scFil = dsbsc_filter(orx,cut,scDmd)   						# Fungsi demodulasi setelah filter (Filter masih mau diupdate)
	if scDom == 'frequencyDomain':
		scMod = freq(scMod)             								# Fungsi modulasi        
		scDmd = freq(scDmd)     												# Fungsi demodulasi
		scFil = freq(scFil)															# Fungsi demodulasi setelah filter (Filter masih mau diupdate)
		mt = freq(mt)
		ct = freq(ct)
	if scPlot == 'message':
		scShow = p.one(scPlot,scDom,mt,xf,ctF)                    # Plotting untuk waveform isyarat pemodulasi
	elif scPlot == 'carrier':
		scShow = p.one(scPlot,scDom,ct,xf,ctF)                    # Plotting untuk waveform isyarat pembawa   
	elif scPlot == 'modulated':
		scShow = p.one(scPlot,scDom,scMod,xf,ctF)                 # Plotting untuk waveform isyarat termodulas
	elif scPlot == 'demodulated':
		scShow = p.one(scPlot,scDom,scDmd,xf,ctF)                	# Plotting untuk waveform isyarat demodulasi  
	elif scPlot == 'filtered':
		scShow = p.one(scPlot,scDom,scFil,xf,ctF)                 # Plotting untuk waveform isyarat demodulasi setelah filter
	elif scPlot == 'dsbsc':
		scShow = p.all(scPlot,mt,ct,scMod,scDmd,scFil,xf,ctF,scDom)   # Plotting untuk waveform semua tahap        
	return scShow
# -----------------------------------------------------------------------------------------------------------------------------
""" Input AM SSB """
def amSSB(mt,mtA,fs,mtF,ct,ctA,ctF,mh,mhA,mhF,orx,cut,ssPlot,ssDom):
	if mt == 'sine':
		mh = sine(mhA,fs,mhF)              							# Isyarat Hilbert Transform saat isyarat message sin
	elif mt == 'cosine':
		mh = cosine(mhA,fs,mhF)              						# Isyarat Hilbert Transform saat isyarat message cos
	mt = message(mt,mtA,fs,mtF)												# Fungsi isyarat message
	ct = carrier(ct,ctA,fs,ctF)												# Fungsi isyarat carrier
	xf = xProp(mt,fs)																	# Fungsi x axis properties untuk frekuensi
	ctCos = cosine(ctA,fs,ctF)              					# Isyarat pembawa (cosinus)
	ctSin = sine(ctA,fs,ctF)                					# Isyarat pembawa (sinus)
	ssMod = ssb_usb(mt,mh,ctCos,ctSin)   							# Fungsi modulasi               
	ssDmd = ssb_demod(ssMod,ctCos)      							# Fungsi demodulasi  
	ssFil = ssb_filter(orx,cut,ssDmd) 								# Fungsi demodulasi setelah filter (Filter masih mau diupdate)
	if ssDom == 'frequencyDomain':
		ssMod = freq(ssMod)             								# Fungsi modulasi        
		ssDmd = freq(ssDmd)     												# Fungsi demodulasi
		ssFil = freq(ssFil)															# Fungsi demodulasi setelah filter (Filter masih mau diupdate)
		mt = freq(mt)
		ct = freq(ct)
	if ssPlot == 'message':
		ssShow = p.one(ssPlot,ssDom,mt,xf,ctF)          					# Plotting untuk waveform isyarat pemodulasi
	elif ssPlot == 'carrier':
		ssShow = p.one(ssPlot,ssDom,ct,xf,ctF)      							# Plotting untuk waveform isyarat pembawa   
	elif ssPlot == 'modulated':
		ssShow = p.one(ssPlot,ssDom,ssMod,xf,ctF)       					# Plotting untuk waveform isyarat termodulas
	elif ssPlot == 'demodulated':
		ssShow = p.one(ssPlot,ssDom,ssDmd,xf,ctF)       					# Plotting untuk waveform isyarat demodulasi  
	elif ssPlot == 'filtered':
		ssShow = p.one(ssPlot,ssDom,ssFil,xf,ctF)       					# Plotting untuk waveform isyarat demodulasi setelah filter
	elif ssPlot == 'ssb':
		ssShow = p.all(ssPlot,mt,ct,ssMod,ssDmd,ssFil,xf,ctF,ssDom)  # Plotting untuk waveform semua tahap       
	return ssShow
# -----------------------------------------------------------------------------------------------------------------------------
""" Input FM Modulation """
def fm(mt,mtA,fs,mtF,ct,ctA,ctF,idx,fmPlot,fmDom):
	mt = message(mt,mtA,fs,mtF)												# Fungsi isyarat message
	ct = carrier(ct,ctA,fs,ctF)												# Fungsi isyarat carrier
	xf = xProp(mt,fs)																	# Fungsi x axis properties untuk frekuensi
	theta = integ(fs,ctF,mt,idx)											#
	fmMod = phaseMod(ctA,theta)												#
	fmDmd = env(differ(fmMod))												#
	if fmDom == 'frequencyDomain':
		fmMod = freq(fmMod)             								# Fungsi modulasi        
		fmDmd = freq(fmDmd)     												# Fungsi demodulasi
		mt = freq(mt)
		ct = freq(ct)
	if fmPlot == 'message':
		fmShow = p.one(fmPlot,fmDom,mt,xf,ctF)                      # Plotting untuk waveform isyarat pemodulasi
	elif fmPlot == 'carrier':
		fmShow = p.one(fmPlot,fmDom,ct,xf,ctF)                      # Plotting untuk waveform isyarat pembawa   
	elif fmPlot == 'modulated':
		fmShow = p.one(fmPlot,fmDom,fmMod,xf,ctF)                   # Plotting untuk waveform isyarat termodulas
	elif fmPlot == 'demodulated':
		fmShow = p.one(fmPlot,fmDom,fmDmd,xf,ctF)										# Plotting untuk waveform isyarat demodulasi  
	elif fmPlot == 'fm':
		fmShow = p.all(fmPlot,mt,ct,fmMod,fmDmd,fmDmd,xf,ctF,fmDom)    # Plotting untuk waveform semua tahap       
	return fmShow
# -----------------------------------------------------------------------------------------------------------------------------
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
# -----------------------------------------------------------------------------------------------------------------------------