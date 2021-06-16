from io import BytesIO
import base64
import matplotlib.pyplot as plt
# Base untuk semua output matplotlib ke website, Proses modul ditampung di "module.py"
""" FUNGSI : Generate Graph """
def getGraph():
  buffer = BytesIO()
  plt.savefig(buffer, format = 'png')
  buffer.seek(0)
  image_png = buffer.getvalue()
  graph = base64.b64encode(image_png)
  graph = graph.decode('utf-8')
  buffer.close()
  return graph
# ---------------------------------------------------------------------------------------------
""" FUNGSI : One Waveform """
def one(plot,dom,x,xf,ctF):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,3))
  # Plot untuk Signal Generator
  if plot == 'sine':
    plt.title('Sinusoidal Wave')
  elif plot == 'cosine':
    plt.title('Cosinus Wave')
  elif plot == 'square':
    plt.title('Square Wave')
  elif plot == 'sawtooth':
    plt.title('Sawtooth/Triangle Wave')
  # Plot untuk Modulasi Analog (AM dan FM)
  if plot == 'message':
    plt.title('Message Signal')
  elif plot == 'carrier':
    plt.title('Carrier Signal')
  elif plot == 'modulated':
    plt.title('Modulated Signal')
  elif plot == 'demodulated':
    plt.title('Demodulated Signal')
  elif plot == 'filtered':
    plt.title('Demodulated and Filtered Signal')
  elif plot == 'envelope':
    plt.title('Envelope on Modulated Signal')
  # Membedakan plot untuk time domain dan frequency domain
  if dom == 'timeDomain':
    plt.plot(x, scalex=0.5, scaley=0.1, c='#004266')
    plt.xlabel('Time (s)')
  elif dom == 'frequencyDomain':
    plt.plot(xf,x, scalex=0.5, scaley=0.1, c='#004266')
    plt.xlim(0,2*ctF)
    plt.xlabel('Frequency (Hz)')
  plt.ylabel('Amplitude')
  plt.grid(b=True, which='major', c='#666666')
  plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
  plt.minorticks_on()
  plt.tight_layout()
  return getGraph()
# ---------------------------------------------------------------------------------------------
""" FUNGSI : All Waveform """
def all(plot,mt,ct,mod,dmd,x,xf,ctF,dom):
  plt.switch_backend('AGG')
  if dom == 'timeDomain':
    plt.figure(figsize=(12,12))
    # Plot Isyarat Pemodulasi
    plt.subplot(4,1,1)
    plt.plot(mt, scalex=0.5, scaley=0.1, c='#004266')
    if plot == 'signal':
      plt.title('Sinusoidal Wave')
    else:
      plt.title('Message Signal')  
    plt.grid(b=True, which='major', c='#666666')
    plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
    plt.minorticks_on()
    plt.ylabel('Amplitude')
    # Plot Isyarat Pembawa
    plt.subplot(4,1,2)
    plt.plot(ct, scalex=0.5, scaley=0.1, c='#FF7700')
    if plot == 'signal':
      plt.title('Cosinus Wave')
    else:
      plt.title('Carrier Signal')
    plt.grid(b=True, which='major', c='#666666')
    plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
    plt.minorticks_on()
    plt.ylabel('Amplitude')
    # Plot Isyarat Termodulasi
    plt.subplot(4,1,3)
    if plot == 'signal':
      plt.plot(mod, scalex=0.5, scaley=0.1, c='#004266')
      if plot == 'signal':
        plt.title('Square Wave')
      else:
        plt.title('Modulated Signal')
    elif plot == 'fm':
      plt.plot(mod, scalex=0.5, scaley=0.1, c='#004266')
      plt.title('Modulated Signal')
    else:
      plt.plot(mod, label='Modulated Signal', scalex=0.5, scaley=0.1, c='#004266')
      if plot == 'dsbfc':
        plt.plot(x, label='Envelope', scalex=0.5, scaley=0.1, c='#D500FF')
        plt.title('Modulated Signal with Envelope')
      else:
        plt.plot(dmd, label='Demodulated Signal', scalex=0.5, scaley=0.1, c='#D500FF')
        plt.title('Modulated and Demodulated Signal')
      plt.legend()
    plt.grid(b=True, which='major', c='#666666')
    plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
    plt.minorticks_on()
    plt.ylabel('Amplitude')
    # Plot Isyarat Demodulasi
    plt.subplot(4,1,4)
    if plot == 'signal':
      plt.plot(dmd, scalex=0.5, scaley=0.1, c='#D500FF')
      plt.title('Sawtooth/Triangle Wave')
    elif plot == 'dsbfc':
      plt.plot(dmd, scalex=0.5, scaley=0.1, c='#004266')
      plt.title('Demodulated Signal')
    else:
      plt.plot(x, scalex=0.5, scaley=0.1, c='#004266')
      if plot == 'fm':
        plt.title('Demodulated Signal')
      else:
        plt.title('Filtered Signal')
    plt.grid(b=True, which='major', c='#666666')
    plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
    plt.minorticks_on()
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
  # Plotting untuk Frequency Domain
  elif dom == 'frequencyDomain':
    plt.figure(figsize=(12,6))
    # Plot Isyarat Pemodulasi dan Pembawa
    plt.subplot(2,1,1)
    plt.plot(xf,mt,label='Message Signal', scalex=0.5, scaley=0.1, c='#FF7700')
    plt.plot(xf,ct,label='Carrier Signal', scalex=0.5, scaley=0.1, c='#004266')
    plt.title('Message and Carrier Signal')
    plt.grid(b=True, which='major', c='#666666',)
    plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
    plt.minorticks_on()
    plt.ylabel('Amplitude')
    plt.legend()
    plt.xlim(0,2*ctF)
    # Plot Isyarat Termodulasi, FIlter/Env, Demodulasi
    plt.subplot(2,1,2)
    if plot != 'dsbfc':
      plt.plot(xf,x,label='Filtered Signal', scalex=0.5, scaley=0.1, c='#00FF00')
    plt.plot(xf,mod,label='Modulated Signal', scalex=0.5, scaley=0.1, c='#FF7700')
    plt.plot(xf,dmd,label='Demodulated Signal', scalex=0.5, scaley=0.1, c='#004266')
    plt.title('Modulation and Demodulation')
    plt.grid(b=True, which='major', c='#666666')
    plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
    plt.minorticks_on()
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.xlim(0,2*ctF)  
  plt.tight_layout()
  return getGraph()
# ---------------------------------------------------------------------------------------------
""" FUNGSI : Digital Modulation """
def dig(t,plot,y1,y2,y3,xf,yf,sign):
  plt.switch_backend('AGG')
  if plot == 'digitalModulation':
    plt.figure(figsize=(12,15))
    # Plot untuk random binary sequence
    plt.subplot(5,1,1)
    plt.plot(sign, scalex=0.5, scaley=0.1, c='#FF7700')
    plt.title('Random Binary Sequential')
    plt.grid(b=True, which='major', c='#666666')
    plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
    plt.minorticks_on()
    plt.ylabel('Amplitude')
    # Plot untuk output Modulasi Digital
    plt.subplot(5,1,2)
    plt.plot(t,y1, scalex=0.5, scaley=0.1, c='#004266')
    plt.title('BASK Modulation Output')
    plt.grid(b=True, which='major', c='#666666')
    plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
    plt.minorticks_on()
    # Plot untuk output Modulasi Digital
    plt.subplot(5,1,3)
    plt.plot(t,y2, scalex=0.5, scaley=0.1, c='#004266')
    plt.title('BFSK Modulation Output')
    plt.grid(b=True, which='major', c='#666666')
    plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
    plt.minorticks_on()
    # Plot untuk output Modulasi Digital
    plt.subplot(5,1,4)
    plt.plot(t,y3, scalex=0.5, scaley=0.1, c='#004266')
    plt.title('BPSK Modulation Output')
    plt.grid(b=True, which='major', c='#666666')
    plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
    plt.minorticks_on()
    # Plot untuk grafik wutt
    plt.ylabel('Amplitude')
    plt.subplot(5,1,5)
    plt.plot(xf,yf, scalex=0.5, scaley=0.1) 
    plt.title('Graph')
    plt.grid(b=True, which='major', c='#666666')
    plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
    plt.minorticks_on()
    plt.ylabel('Amplitude')
  else:
    plt.figure(figsize=(12,9))
    # Plot untuk random binary sequence
    plt.subplot(3,1,1)
    plt.plot(sign, scalex=0.5, scaley=0.1, c='#FF7700')
    plt.title(plot + ' Random Binary Sequential')
    plt.grid(b=True, which='major', c='#666666')
    plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
    plt.minorticks_on()
    plt.ylabel('Amplitude')
    # Plot untuk output Modulasi Digital
    plt.subplot(3,1,2)
    plt.plot(t,y1, scalex=0.5, scaley=0.1, c='#004266')
    plt.title(plot + ' Modulation Output')
    plt.grid(b=True, which='major', c='#666666')
    plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
    plt.minorticks_on()
    # Plot untuk grafik wutt
    plt.ylabel('Amplitude')
    plt.subplot(3,1,3)
    plt.plot(xf,yf, scalex=0.5, scaley=0.1) 
    plt.title(plot + ' Graph')
    plt.grid(b=True, which='major', c='#666666')
    plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
    plt.minorticks_on()
    plt.ylabel('Amplitude')
  plt.tight_layout()
  return getGraph()
# ---------------------------------------------------------------------------------------------
