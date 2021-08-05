from io import BytesIO
import numpy as np

import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Sementara "plot.py" dijadiin base untuk semua output matplotlib - Signalgen
# Proses modul sementara ditampung di "views.py"

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

# Generates signal generator - sinus wave
def get_plot_sin(sinWave):
    plt.switch_backend('AGG')
    plt.figure(figsize=(6,3))
    plt.title('Sinusoidal Wave')
    plt.plot(sinWave)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(b=True, which = 'major', color = '#666666', linestyle = '-')
    plt.minorticks_on()
    plt.grid(b=True, which = 'minor', color = '#999999', linestyle = '-', alpha = 0.2)
    plt.tight_layout()
    graph = get_graph()
    return graph

# Generates signal generator - square wave
def get_plot_sq(sqWave):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,4))
    plt.title('Square Wave')
    plt.plot(sqWave)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.tight_layout()
    graph = get_graph()
    return graph

# Generates signal generator - sawtooth wave
def get_plot_saw(sawWave):
    plt.switch_backend('AGG')
    plt.figure(figsize=(8,4))
    plt.title('Triangle/Sawtooth Wave')
    plt.plot(sawWave)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.tight_layout()
    graph = get_graph()
    return graph

# Generates signal generator - all three waves
def get_plot_signalgen(sinWave, sqWave, sawWave):
    plt.switch_backend('AGG')
    plt.figure(figsize=(12,9))

    plt.subplot(3,1,1)
    plt.plot(sinWave, scalex=0.5, scaley=0.1)
    plt.title('Sinusoidal Wave')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(3,1,2)
    plt.plot(sqWave, scalex=0.5, scaley=0.1)
    plt.title('Square Wave')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(3,1,3)
    plt.plot(sawWave, scalex=0.5, scaley=0.1)
    plt.title('Sawtooth Wave')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.tight_layout()
    graph = get_graph()
    return graph

# Generates AM Modulation - DSBFC
def get_plot_fc(t, xf, mt, mf, ct, cf, dsbfc_mod, envelope, dsbfc_demod, dsbfc_modFreq, dsbfc_demodFreq):
    plt.switch_backend('AGG')
    plt.figure(figsize=(24,24))

    plt.subplot(6,1,1)
    plt.plot(t, mt)
    plt.title('Message m(t) Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(6,1,2)
    plt.plot(t, ct)
    plt.title('Carrier c(t) Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(6,1,3)
    plt.plot(t, dsbfc_mod, t, envelope)
    plt.title('Modulated Signal with Envelope')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(6,1,4)
    plt.plot(t, dsbfc_demod)
    plt.title('Demodulated Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(6,1,5)
    plt.plot(xf, np.abs(mf), xf, np.abs(cf))
    plt.title('Message and Carrier Signal - Frequency Domain')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')

    plt.subplot(6,1,6)
    plt.plot(xf, dsbfc_modFreq, xf, dsbfc_demodFreq)
    plt.title('Modulated and Demodulated Signal - Frequency Domain')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.tight_layout()
    graph = get_graph()
    return graph

# Generates AM Modulation - DSBSC
def get_plot_sc(t, xf, mt, mf, ct, cf, dsbsc_mod, dsbsc_demod, dsbsc_modFreq, dsbsc_demodFreq):
    plt.switch_backend('AGG')
    plt.figure(figsize=(24,24))

    plt.subplot(6,1,1)
    plt.plot(t, mt)
    plt.title('Message m(t) Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(6,1,2)
    plt.plot(t, ct)
    plt.title('Carrier c(t) Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(6,1,3)
    plt.plot(t, dsbsc_mod)
    plt.title('Modulated Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(6,1,4)
    plt.plot(t, dsbsc_demod)
    plt.title('Demodulated Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(6,1,5)
    plt.plot(xf, np.abs(mf), xf, np.abs(cf))
    plt.title('Message and Carrier Signal - Frequency Domain')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')

    plt.subplot(6,1,6)
    plt.plot(xf, dsbsc_modFreq, xf, dsbsc_demodFreq)
    plt.title('Modulated and Demodulated Signal - Frequency Domain')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.tight_layout()
    graph = get_graph()
    return graph

# Generates AM Modulation - SSB
def get_plot_ssb(t, xf, mt, mf, ct, cf, ssb_mod, ssb_demod, ssb_modFreq, ssb_demodFreq):
    plt.switch_backend('AGG')
    plt.figure(figsize=(24,24))

    plt.subplot(6,1,1)
    plt.plot(t, mt)
    plt.title('Message m(t) Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(6,1,2)
    plt.plot(t, ct)
    plt.title('Carrier c(t) Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(6,1,3)
    plt.plot(t, ssb_mod)
    plt.title('Modulated Signal - USB side')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(6,1,4)
    plt.plot(t, ssb_demod)
    plt.title('Demodulated Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(6,1,5)
    plt.plot(xf, np.abs(mf), xf, np.abs(cf))
    plt.title('Message and Carrier Signal - Frequency Domain')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')

    plt.subplot(6,1,6)
    plt.plot(xf, ssb_modFreq, xf, ssb_demodFreq)
    plt.title('Modulated and Demodulated Signal - Frequency Domain')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.tight_layout()
    graph = get_graph()
    return graph

# Generates FM Modulation and Demodulation - Time domain
def get_plot_fm_timeResult(mt, ct, fm_mod, fm_demod):
    plt.switch_backend('AGG')
    plt.figure(figsize=(24,24))

    plt.subplot(4,1,1)
    plt.plot(mt)
    plt.title('Message m(t) Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(4,1,2)
    plt.plot(ct)
    plt.title('Carrier c(t) Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(4,1,3)
    plt.plot(fm_mod)
    plt.title('FM Modulated Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')

    plt.subplot(4,1,4)
    plt.plot(fm_demod)
    plt.title('FM Demodulated Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    
    plt.tight_layout()
    graph = get_graph()
    return graph

# Generates FM Modulation and Demodulation - Freq domain
def get_plot_fm_freqResult(xf, fc, mf, cf, fm_modFreq, fm_demodFreq):
    plt.switch_backend('AGG')
    plt.figure(figsize=(24,24))

    plt.subplot(4,1,1)
    plt.plot(xf, abs(mf))
    plt.xlim(0,2*fc)
    plt.title('Message Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')

    plt.subplot(4,1,2)
    plt.plot(xf, abs(cf))
    plt.xlim(0,2*fc)
    plt.title('Carrier Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')

    plt.subplot(4,1,3)
    plt.plot(xf, abs(fm_modFreq))
    plt.xlim(0,2*fc)
    plt.title('FM Modulated Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')

    plt.subplot(4,1,4)
    plt.plot(abs(fm_demodFreq))
    plt.xlim(0,2*fc)
    plt.ylim(0,0.5)
    plt.title('FM Demodulated Signal')
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    
    plt.tight_layout()
    graph = get_graph()
    return graph

# ---------------------------------------------------------------------------------------------
