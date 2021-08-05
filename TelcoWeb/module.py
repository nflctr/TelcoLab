import numpy as np
import scipy.signal as sg
import scipy.fftpack as fr
import cmath as c
import TelcoWeb.plot as p

""" Error Handling dari Input User """
# Fungsi untuk cek data parameter
def inputData(data):
    # Dictionary dari kata untuk input kode
    dictSG = ['amplitude','freq-sampling','frequency','show','signal-generator']
    dictFC = ['am-dsbfc', 'amplitude', 'as', 'carrier-signal', 'demodulated-signal', 'envelope-detection', 'freq-sampling', 'frequency', 'in', 'message-signal', 'message-signal*carrier-signal+carrier-signal', 'modulated-signal', 'show']
    dictSC = ['am-dsbsc', 'amplitude', 'as', 'carrier-signal', 'coherent-demodulation', 'cutoff-frequency', 'demodulated-signal', 'filter', 'filtered-signal', 'freq-sampling', 'frequency', 'in', 'message-signal', 'message-signal*carrier-signal', 'modulated-signal', 'order', 'show']
    dictSS = ['am-ssb', 'amplitude', 'as', 'carrier-signal', 'coherent-demodulation', 'cutoff-frequency', 'demodulated-signal', 'filter', 'filtered-signal', 'freq-sampling', 'frequency', 'in', 'message-signal', 'modulated-signal', 'order', 'show', 'usb-signal']
    dictFM = ['amplitude', 'as', 'carrier-signal', 'demodulated-signal', 'differentiator,envelope', 'fm-modulation', 'freq-sampling', 'frequency', 'in', 'integrator,phase-modulator', 'message-signal', 'modulated-signal', 'modulation-index', 'show']
    dictDG = ['as', 'carrier-signal', 'digital-modulation', 'freq-sampling', 'frequency', 'message-signal', 'random-data', 'show']
    # Error handling modul Signal Generator
    # signal-generator amplitude 1 frequency 1000 freq-sampling 100
    # show signal
    if data[0] == 'signal-generator':
        amplitude           = float(data[2])
        freq_sampling       = float(data[4])
        frequency           = float(data[6])
        signal_plot         = data[8]
        show                = signal_generator(signal_plot, amplitude, freq_sampling, frequency)
        data.pop()
        data.sort()
        del data[0:3]
        cek_kata            = (data == dictSG)
    # Error handling modul AM DSBFC Modulation
    elif data[0] == 'am-dsbfc':
        message_wave        = data[4] #4
        message_amplitude   = float(data[6]) #6
        freq_sampling       = float(data[2]) #2
        message_freq        = float(data[8]) #8
        carrier_wave        = data[10] #10
        carrier_amplitude   = float(data[12]) #12
        carrier_freq        = float(data[14]) #14
        dsbfc_plot          = data[22] #22
        dsbfc_domain        = data[24] #24
        show                = am_dsbfc(message_wave, message_amplitude, freq_sampling, message_freq, carrier_wave, carrier_amplitude, carrier_freq, dsbfc_plot, dsbfc_domain)
        remove              = [data[4], data[6], data[2], data[8], data[10], data[12], data[14], data[22], data[24]]
        final_list          = list(set(data) - set(remove))
        final_list.sort()
        cek_kata            = (final_list == dictFC)
    # Error handling modul AM DSBSC Modulation
    elif data[0] == 'am-dsbsc':
        message_wave        = data[4] #4
        message_amplitude   = float(data[6]) #6
        freq_sampling       = float(data[2]) #2
        message_freq        = float(data[8]) #8
        carrier_wave        = data[10] #10
        carrier_amplitude   = float(data[12]) #12
        carrier_freq        = float(data[14]) #14
        filter_order        = float(data[23]) #23
        cutoff_freq         = float(data[25]) #25
        dsbsc_plot          = data[29] #29
        dsbsc_domain        = data[31] #31
        show                = am_dsbsc(message_wave, message_amplitude, freq_sampling, message_freq, carrier_wave, carrier_amplitude, carrier_freq, filter_order, cutoff_freq, dsbsc_plot, dsbsc_domain)
        remove              = [data[4], data[6], data[2], data[8], data[10], data[12], data[14], data[23], data[25], data[29], data[31]]
        final_list          = list(set(data) - set(remove))
        final_list.sort()
        cek_kata            = (final_list == dictSC)
    # Error handling modul AM SSB Modulation
    elif data[0] == 'am-ssb':
        message_wave        = data[4] #4
        message_amplitude   = float(data[6]) #6
        freq_sampling       = float(data[2]) #2
        message_freq        = float(data[8]) #8
        carrier_wave        = data[10] #10
        carrier_amplitude   = float(data[12]) #12
        carrier_freq        = float(data[14]) #14
        filter_order        = float(data[23]) #23
        cutoff_freq         = float(data[25]) #25
        ssb_plot            = data[29] #29
        ssb_domain          = data[31] #31
        show                = am_ssb(message_wave, message_amplitude, freq_sampling, message_freq, carrier_wave, carrier_amplitude, carrier_freq, filter_order, cutoff_freq, ssb_plot, ssb_domain)
        remove              = [data[4], data[6], data[2], data[8], data[10], data[12], data[14], data[23], data[25], data[29], data[31]]
        final_list          = list(set(data) - set(remove))
        final_list.sort()
        cek_kata            = (final_list == dictSS)
    # Error handling modul Frequency Modulation
    elif data[0] == 'fm-modulation':
        message_wave        = data[4] #4
        message_amplitude   = float(data[6]) #6
        freq_sampling       = float(data[2]) #2
        message_freq        = float(data[8]) #8
        carrier_wave        = data[10] #10
        carrier_amplitude   = float(data[12]) #12
        carrier_freq        = float(data[14]) #14
        modulation_index    = float(data[16]) #16
        fm_plot             = data[24] #24
        fm_domain           = data[26] #26
        show                = fm_mod(message_wave, message_amplitude, freq_sampling, message_freq, carrier_wave, carrier_amplitude, carrier_freq, modulation_index, fm_plot, fm_domain)
        remove              = [data[4], data[6], data[2], data[8], data[10], data[12], data[14], data[16], data[24], data[26]]
        final_list          = list(set(data) - set(remove))
        final_list.sort()
        cek_kata            = (final_list == dictFM)
    # Error handling modul Digital Modulation
    elif data[0] == 'digital-modulation':
        freq_sampling       = float(data[2])
        carrier_freq        = float(data[5])
        random_data_sum     = int(data[7])
        digital_plot        = data[11]
        show                = digital(freq_sampling, carrier_freq, random_data_sum, digital_plot)
        data.pop()
        data.sort()
        del data[0:3]
        cek_kata            = (data == dictDG)
    return cek_kata, show

""" Modul Fungsi Matematika """
# Fungsi Adder
def add(a, b):
    return (a+b)
# Fungsi sub
def sub(a, b):
    return (a-b)
# Fungsi multiplier
def mul(a, b):
    return (a*b)
# Fungsi division
def div(a, b):
    return (a/b)

""" Modul Signal Generator """
# Fungsi gelombang cosinus
def cosine(amplitude, freq_sampling, frequency):
    time = np.arange(0, 1, (1/freq_sampling))
    cos = amplitude*np.cos(2*np.pi*frequency*time)
    return time, cos
# Fungsi gelombang sinus
def sine(amplitude, freq_sampling, frequency):
    time = np.arange(0, 1, (1/freq_sampling))
    sin = amplitude*np.sin(2*np.pi*frequency*time)
    return time, sin
# Fungsi gelombang kotak
def square(amplitude, freq_sampling, frequency):
    time = np.arange(0, 1, (1/freq_sampling))
    sqr = amplitude*sg.square(2*np.pi*frequency*time, duty=0.3)
    return time, sqr
# Fungsi gelombang segitiga
def sawtooth(amplitude, freq_sampling, frequency):
    time = np.arange(0, 1, (1/freq_sampling))
    saw = amplitude*sg.sawtooth(2*np.pi*frequency*time, width=0.5)
    return time, saw
# Fungsi Isyarat Hilbert Transform Cosine
def hilbert_cosine(amplitude, freq_sampling, frequency):
    time = np.arange(0, 1, (1/freq_sampling))
    hilbert_cos = amplitude*np.sin(2*np.pi*frequency*time)
    # hilbert_cos = amplitude*np.cos(2*np.pi*frequency*time-np.pi/2)
    return time, hilbert_cos
# Fungsi Isyarat Hilbert Transform Sine
def hilbert_sine(amplitude, freq_sampling, frequency):
    time = np.arange(0, 1, (1/freq_sampling))
    hilbert_sin = (-amplitude)*np.cos(2*np.pi*frequency*time)
    # hilbert_sin = amplitude*np.sin(2*np.pi*frequency*time-np.pi/2)
    return time, hilbert_sin

""" Modul untuk Frequency Domain """
# Frequency Domain
def freq(signal):
    signal_freq_domain = div(fr.fft(signal), len(signal))
    signal_freq_domain = mul(signal_freq_domain[range(int(div(len(signal), 2)))], 2)
    return np.abs(signal_freq_domain)
# Frequency Domain - X axis Properties
def x_prop(message, freq_sampling):
    tp_count = len(message)
    values = np.arange(int(tp_count/2))
    time_period = tp_count/freq_sampling
    xf = values/time_period
    return xf

""" Fungsi Filter Butterworth dan Filter IRT """
# Fungsi Filter IRT
def filter_IRT(filter_order, cutoff_freq, freq_sampling, demodulation_signal):
    n = np.arange(0, filter_order)
    theta = 2*np.pi*cutoff_freq/freq_sampling
    h_lpf = (theta/np.pi)*(np.sinc((theta/np.pi)*(n-0.5*filter_order)))
    return sg.convolve(demodulation_signal, h_lpf, mode='same')
# Fungsi Filter Butterworth
def filter_butterworth(filter_order, cutoff_freq, freq_sampling, demodulation_signal):
    b, a = sg.butter(filter_order, cutoff_freq, 'low', analog=False, fs=freq_sampling)
    return sg.filtfilt(b, a, demodulation_signal, method='gust')

""" Modul simulasi AM DSBFC (Full Carrier) """
# Modulasi AM DSBFC
def dsbfc_mod(message_signal, carrier_signal, carrier_amplitude):
    modulated = add(carrier_amplitude, message_signal)
    return mul(modulated, carrier_signal)
# Deteksi Envelope AM DSBFC
def dsbfc_env(dsbfc_modulation):
    return np.abs(sg.hilbert(dsbfc_modulation))
# Demodulasi AM DSBFC
def dsbfc_demod(dsbfc_envelope, carrier_amplitude):
    return sub(dsbfc_envelope, carrier_amplitude)

""" Modul simulasi AM DSBSC (Suppressed Carrier) """
# Modulasi AM DSBSC
def dsbsc_mod(message_signal, carrier_cos):
    return mul(message_signal, carrier_cos)
# Demodulasi AM DSBSC
def dsbsc_demod(dsbsc_modulation, carrier_cos):
    return mul(dsbsc_modulation, carrier_cos)

""" Modul simulasi AM SSB (Single Side Band) """
# Fungsi USB (dijadikan hasil modulasi)
def ssb_usb(message_signal, hilbert_signal, carrier_cos, carrier_sin):
    a = message_signal*carrier_cos
    b = hilbert_signal*carrier_sin
    return sub(a,b)
# Fungsi LSB
def ssb_lsb(message_signal, hilbert_signal, carrier_cos, carrier_sin):
    a = message_signal*carrier_cos
    b = hilbert_signal*carrier_sin
    return add(a, b)
# Fungsi Demodulasi
def ssb_demod(ssb_usb, carrier_cos):
    return mul(ssb_usb, carrier_cos)

""" Modul Modulasi Frekuensi (FM) """
# Fungsi Integrator
def integrator(freq_sampling, carrier_freq, message_signal, modulation_index):
    time = np.arange(0, 1, (1/freq_sampling))
    theta = np.zeros_like(message_signal)
    for i, time in enumerate(time):
        theta[i] = 2*np.pi*((carrier_freq*time) + (message_signal[i]*modulation_index))
    return theta
# Fungsi Phase Modulator - output isyarat termodulasi
def phase_modulator(amplitude, theta):
    return mul(amplitude, np.sin(theta))
# Fungsi Differentiator - FM Demodulation
def differentiator(fm_modulation):
    return np.diff(fm_modulation)
# Fungsi Deteksi selubung
def fm_envelope(differentiator):
    demod = abs(sg.hilbert(differentiator))
    demod_FFT = np.fft.rfft(demod) * c.rect(-1., np.pi/2)
    return np.fft.irfft(demod_FFT)*100

""" Modul Modulasi Digital """
# Fungsi untuk menghasilkan random data dengan jumlah data sebanyak x
def random_data_generator(random_data_sum):
    return np.random.randint(0, 2, random_data_sum)
# Fungsi untuk melakukan modulasi digital
def digital_modulation(freq_sampling, carrier_freq, random_data, random_data_sum, digital_plot):
    time = np.arange(0, 2, (1/freq_sampling))
    freq_deviasi = np.array(random_data)
    if digital_plot == 'BASK':
        freq_deviasi[freq_deviasi > 0] = 40
        freq_deviasi[freq_deviasi == 0] = 10
    elif digital_plot == 'BFSK':
        freq_deviasi[freq_deviasi > 0] = 5
        freq_deviasi[freq_deviasi == 0] = -5
    elif digital_plot == 'BPSK':
        freq_deviasi[freq_deviasi == 0] = 180
    samples_per_bit = 2*freq_sampling/random_data_sum
    dd = np.repeat(freq_deviasi, samples_per_bit)
    if digital_plot == 'BASK':
        y = dd*np.sin(2*np.pi*carrier_freq*time)
        carrier_signal = 10*np.sin(2*np.pi*carrier_freq*time)
    elif digital_plot == 'BFSK':
        y = 10*np.sin(2*np.pi*(carrier_freq+dd)*time)
        carrier_signal = 10*np.sin(2*np.pi*carrier_freq*time)
    elif digital_plot == 'BPSK':
        y = np.sin(2*np.pi*carrier_freq*time+(np.pi*dd/180))
        carrier_signal = np.sin(2*np.pi*carrier_freq*time)
    random_data_arr = np.array(random_data)
    sym_duration = 100
    message_signal = np.zeros(mul(sym_duration, random_data_sum))
    id_n = np.where(random_data_arr == 1)
    for i in id_n[0]:
        temp = int(mul(i, sym_duration))
        message_signal[temp:temp+sym_duration] = 1
    return y, message_signal, carrier_signal
# Fungsi untuk menghasilkan demodulasi digital
def digital_demodulation(freq_sampling, random_data, random_data_sum, y, carrier_signal, digital_plot):
    step = 2*freq_sampling/random_data_sum
    max_value = len(y)
    y2 = np.zeros(len(random_data)+1)
    j = 0
    for i in range(0, int(max_value), int(step)):
        if digital_plot == 'BASK':
            if sum(y[i:(i+int(step)-1)]) > sum(carrier_signal[i:(i+int(step)-1)]):
                y2 [j] = 1
            else:
                y2 [j] = 0
            j += 1
        elif digital_plot == 'BFSK':
            if sum(y[i:(i+int(step)-1)]) > sum(carrier_signal[i:(i+int(step)-1)]):
                y2 [j] = 1
            else:
                y2 [j] = 0
            j += 1
        elif digital_plot == 'BPSK':
            if sum(y[i:(i+int(step)-1)]) > 0:
                y2 [j] = 1
            else:
                y2 [j] = 0
            j += 1
    data_y2 = y2[0:len(random_data)]
    y2_arr = np.array(data_y2)
    sym_duration = 100
    y_demod = np.zeros(sym_duration*random_data_sum)
    id_n2 = np.where(y2_arr == 1)
    for i in id_n2[0]:
        inp2 = int(i*sym_duration)
        y_demod[inp2:inp2+sym_duration] = 1
    return y_demod

""" Fungsi Option untuk Isyarat Pemodulasi (message) dan Pembawa (carrier) """
# Fungsi untuk opsi isyarat pemodulasi/signal generator m(t)
def message(plot, amplitude, freq_sampling, frequency):
    if plot == 'sine':
        time, message = sine(amplitude, freq_sampling, frequency)
    elif plot == 'cosine':
        time, message = cosine(amplitude, freq_sampling, frequency)
    elif plot == 'square':
        time, message = square(amplitude, freq_sampling, frequency)
    elif plot == 'sawtooth':
        time, message = sawtooth(amplitude, freq_sampling, frequency)
    return time, message
# Fungsi untuk opsi isyarat pembawa/signal generator c(t)
def carrier(plot, amplitude, freq_sampling, frequency):
    if plot == 'sine':
        time, carrier = sine(amplitude, freq_sampling, frequency)
    elif plot == 'cosine':
        time, carrier = cosine(amplitude, freq_sampling, frequency)
    elif plot == 'square':
        time, carrier = square(amplitude, freq_sampling, frequency)
    elif plot == 'sawtooth':
        time, carrier = sawtooth(amplitude, freq_sampling, frequency)
    return time, carrier

""" Input Signal Generator """
def signal_generator(signal_plot, amplitude, freq_sampling, frequency):
    if signal_plot == 'signal':
        time, sin = sine(amplitude, freq_sampling, frequency)
        time, cos = cosine(amplitude, freq_sampling, frequency)
        time, squ = square(amplitude, freq_sampling, frequency)
        time, saw = sawtooth(amplitude, freq_sampling, frequency)
        show = p.get_plot_all(signal_plot, time, sin, cos, squ, saw, 'pass', 0, 0, 'time-domain')
    else:
        time, signal_wave = message(signal_plot, amplitude, freq_sampling, frequency)
        show = p.get_plot_one(signal_plot, 'time-domain', time, signal_wave, 0, 0)
    return show

""" Input AM DSBFC """
def am_dsbfc(message_wave, message_amplitude, freq_sampling, message_freq, carrier_wave, carrier_amplitude, carrier_freq, dsbfc_plot, dsbfc_domain):
    time, message_signal = message(message_wave, message_amplitude, freq_sampling, message_freq)
    time, carrier_signal = cosine(carrier_amplitude, freq_sampling, carrier_freq)
    time, carrier_cos = cosine(1, freq_sampling, carrier_freq)
    xf = x_prop(message_signal, freq_sampling)
    dsbfc_modulation = dsbfc_mod(message_signal, carrier_cos, carrier_amplitude)
    dsbfc_envelope = dsbfc_env(dsbfc_modulation)
    dsbfc_demodulation = dsbfc_demod(dsbfc_envelope, carrier_amplitude)
    if dsbfc_domain == 'frequency-domain':
        dsbfc_modulation = freq(dsbfc_modulation)
        dsbfc_envelope = freq(dsbfc_envelope)
        dsbfc_demodulation = freq(dsbfc_demodulation)
        message_signal = freq(message_signal)
        carrier_signal = freq(carrier_signal)
    # Fungsi Plotting
    if dsbfc_plot == 'message-waveform':
        show = p.get_plot_one(dsbfc_plot, dsbfc_domain, time, message_signal, xf, carrier_freq)
    elif dsbfc_plot == 'carrier-waveform':
        show = p.get_plot_one(dsbfc_plot, dsbfc_domain, time, carrier_signal, xf, carrier_freq)
    elif dsbfc_plot == 'modulated-waveform':
        show = p.get_plot_one(dsbfc_plot, dsbfc_domain, time, dsbfc_modulation, xf, carrier_freq)
    elif dsbfc_plot == 'envelope-waveform':
        show = p.get_plot_one(dsbfc_plot, dsbfc_domain, time, dsbfc_envelope, xf, carrier_freq)
    elif dsbfc_plot == 'demodulated-waveform':
        show = p.get_plot_one(dsbfc_plot, dsbfc_domain, time, dsbfc_demodulation, xf, carrier_freq)
    elif dsbfc_plot == 'dsbfc-waveform':
        show = p.get_plot_all(dsbfc_plot, time, message_signal, carrier_signal, dsbfc_modulation, dsbfc_demodulation, dsbfc_envelope, xf, carrier_freq, dsbfc_domain)
    return show

""" Input AM DSBSC """
def am_dsbsc(message_wave, message_amplitude, freq_sampling, message_freq, carrier_wave, carrier_amplitude, carrier_freq, filter_order, cutoff_freq, dsbsc_plot, dsbsc_domain):
    time, message_signal = message(message_wave, message_amplitude, freq_sampling, message_freq)
    time, carrier_signal = cosine(carrier_amplitude, freq_sampling, carrier_freq)
    time, carrier_cos = cosine(1, freq_sampling, carrier_freq)
    xf = x_prop(message_signal, freq_sampling)
    dsbsc_modulation = dsbsc_mod(message_signal, carrier_cos)
    dsbsc_demodulation = dsbsc_demod(dsbsc_modulation, carrier_cos)
    dsbsc_filter = filter_IRT(filter_order, cutoff_freq, freq_sampling, dsbsc_demodulation)
    if dsbsc_domain == 'frequency-domain':
        dsbsc_modulation = freq(dsbsc_modulation)
        dsbsc_demodulation = freq(dsbsc_demodulation)
        dsbsc_filter = freq(dsbsc_filter)
        message_signal = freq(message_signal)
        carrier_signal = freq(carrier_signal)
    # Fungsi Plotting
    if dsbsc_plot == 'message-waveform':
        show = p.get_plot_one(dsbsc_plot, dsbsc_domain, time, message_signal, xf, carrier_freq)
    elif dsbsc_plot == 'carrier-waveform':
        show = p.get_plot_one(dsbsc_plot, dsbsc_domain, time, carrier_signal, xf, carrier_freq)
    elif dsbsc_plot == 'modulated-waveform':
        show = p.get_plot_one(dsbsc_plot, dsbsc_domain, time, dsbsc_modulation, xf, carrier_freq)
    elif dsbsc_plot == 'demodulated-waveform':
        show = p.get_plot_one(dsbsc_plot, dsbsc_domain, time, dsbsc_demodulation, xf, carrier_freq)
    elif dsbsc_plot == 'filtered-waveform':
        show = p.get_plot_one(dsbsc_plot, dsbsc_domain, time, dsbsc_filter, xf, carrier_freq)
    elif dsbsc_plot == 'dsbsc-waveform':
        show = p.get_plot_all(dsbsc_plot, time, message_signal, carrier_signal, dsbsc_modulation, dsbsc_demodulation, dsbsc_filter, xf, carrier_freq, dsbsc_domain)
    return show

""" Input AM SSB """
def am_ssb(message_wave, message_amplitude, freq_sampling, message_freq, carrier_wave, carrier_amplitude, carrier_freq, filter_order, cutoff_freq, ssb_plot, ssb_domain):
    time, carrier_signal = cosine(carrier_amplitude, freq_sampling, carrier_freq)
    if message_wave == 'sine':
        time, message_signal = sine(message_amplitude, freq_sampling, message_freq)
        time, hilbert_signal = hilbert_sine(message_amplitude, freq_sampling, message_freq)
    elif message_wave == 'cosine':
        time, message_signal = cosine(message_amplitude, freq_sampling, message_freq)
        time, hilbert_signal = hilbert_cosine(message_amplitude, freq_sampling, message_freq)
    xf = x_prop(message_signal, freq_sampling)
    carrier_cos = np.cos(2*np.pi*carrier_freq*(np.arange(0,1,(1/freq_sampling))))
    carrier_sin = np.sin(2*np.pi*carrier_freq*(np.arange(0,1,(1/freq_sampling))))
    ssb_modulation = ssb_usb(message_signal, hilbert_signal, carrier_cos, carrier_sin)                                          # ssb_lsb(message_signal, hilbert_signal, carrier_cos, carrier_sin)
    ssb_demodulation = ssb_demod(ssb_modulation, carrier_cos)
    ssb_filter = filter_IRT(filter_order, cutoff_freq, freq_sampling, ssb_demodulation)
    if ssb_domain == 'frequency-domain':
        ssb_modulation = freq(ssb_modulation)
        ssb_demodulation = freq(ssb_demodulation)
        ssb_filter = freq(ssb_filter)
        message_signal = freq(message_signal)
        carrier_signal = freq(carrier_signal)
    # Fungsi Plotting
    if ssb_plot == 'message-waveform':
        show = p.get_plot_one(ssb_plot, ssb_domain, time, message_signal, xf, carrier_freq)
    elif ssb_plot == 'carrier-waveform':
        show = p.get_plot_one(ssb_plot, ssb_domain, time, carrier_signal, xf, carrier_freq)
    elif ssb_plot == 'modulated-waveform':
        show = p.get_plot_one(ssb_plot, ssb_domain, time, ssb_modulation, xf, carrier_freq)
    elif ssb_plot == 'demodulated-waveform':
        show = p.get_plot_one(ssb_plot, ssb_domain, time, ssb_demodulation, xf, carrier_freq)
    elif ssb_plot == 'filtered-waveform':
        show = p.get_plot_one(ssb_plot, ssb_domain, time, ssb_filter, xf, carrier_freq)
    elif ssb_plot == 'ssb-waveform':
        show = p.get_plot_all(ssb_plot, time, message_signal, carrier_signal, ssb_modulation, ssb_demodulation, ssb_filter, xf, carrier_freq, ssb_domain)
    return show

""" Input FM Modulation """
def fm_mod(message_wave, message_amplitude, freq_sampling, message_freq, carrier_wave, carrier_amplitude, carrier_freq, modulation_index, fm_plot, fm_domain):
    time, message_signal = message(message_wave, message_amplitude, freq_sampling, message_freq)
    time, carrier_signal = carrier(carrier_wave, carrier_amplitude, freq_sampling, carrier_freq)
    xf = x_prop(message_signal, freq_sampling)
    theta = integrator(freq_sampling, carrier_freq, message_signal, modulation_index)
    fm_modulation = phase_modulator(carrier_amplitude, theta)
    fm_differentiator = differentiator(fm_modulation)
    fm_demodulation = fm_envelope(fm_differentiator)
    if fm_domain == 'frequency-domain':
        fm_modulation = freq(fm_modulation)
        fm_demodulation = freq(fm_demodulation)
        message_signal = freq(message_signal)
        carrier_signal = freq(carrier_signal)
    # Fungsi Plotting
    if fm_plot == 'message-waveform':
        show = p.get_plot_one(fm_plot, fm_domain, time, message_signal, xf, carrier_freq)
    elif fm_plot == 'carrier-waveform':
        show = p.get_plot_one(fm_plot, fm_domain, time, carrier_signal, xf, carrier_freq)
    elif fm_plot == 'modulated-waveform':
        show = p.get_plot_one(fm_plot, fm_domain, time, fm_modulation, xf, carrier_freq)
    elif fm_plot == 'demodulated-waveform':
        show = p.get_plot_one(fm_plot, fm_domain, time, fm_demodulation, xf, carrier_freq)
    elif fm_plot == 'fm-waveform':
        show = p.get_plot_all(fm_plot, time, message_signal, carrier_signal, fm_modulation, fm_demodulation, 0, xf, carrier_freq, fm_domain)
    return show

""" Input Modulasi Digital """
def digital(freq_sampling, carrier_freq, random_data_sum, digital_plot):
    time = np.arange(0, 2, (1/freq_sampling))
    random_data = random_data_generator(random_data_sum)
    if digital_plot == 'digital-modulation':
        y1, message_signal, carrier_signal = digital_modulation(freq_sampling, carrier_freq, random_data, random_data_sum, 'BASK')
        y2, message_signal, carrier_signal = digital_modulation(freq_sampling, carrier_freq, random_data, random_data_sum, 'BFSK')
        y3, message_signal, carrier_signal = digital_modulation(freq_sampling, carrier_freq, random_data, random_data_sum, 'BPSK')
        y3_demod = digital_demodulation(freq_sampling, random_data, random_data_sum, y3, carrier_signal, 'BPSK')
        xf = x_prop(y1,freq_sampling)
        yf = freq(y1)
        show  = p.get_plot_digital(time, digital_plot, y1, y2, y3, xf, yf, message_signal, carrier_freq, carrier_signal, y3_demod)
    else:
        y1, message_signal, carrier_signal = digital_modulation(freq_sampling, carrier_freq, random_data, random_data_sum, digital_plot)
        y1_demod = digital_demodulation(freq_sampling, random_data, random_data_sum, y1, carrier_signal, digital_plot)
        xf = x_prop(y1,freq_sampling)
        yf = freq(y1)
        show = p.get_plot_digital(time, digital_plot, y1, 0, 0, xf, yf, message_signal, carrier_freq, carrier_signal, y1_demod)
    return show
