from io import BytesIO
import base64
import matplotlib.pyplot as plt
# Base untuk semua output matplotlib ke website, Proses modul ditampung di "module.py"
# Generate Graph
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
""" SIGNAL GENERATOR """
# Plot for Signal Generator - one waveform
def sigOne(plot,x):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,3))
  if plot == 'sine':
    plt.title('Sinusoidal Wave')
  elif plot == 'cosine':
    plt.title('Cosinus Wave')
  elif plot == 'square':
    plt.title('Square Wave')
  elif plot == 'sawtooth':
    plt.title('Sawtooth/Triangle Wave')
  plt.plot(x, scalex=0.5, scaley=0.1)
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Time (s)')
  plt.ylabel('Amplitude')
  plt.tight_layout()
  graph = getGraph()
  return graph
# Plot for Signal Generator - all waveform
def sigAll(sin,cos,squ,saw):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,12))
  plt.ylabel('Amplitude')
  # 
  plt.subplot(4,1,1)
  plt.plot(sin, scalex=0.5, scaley=0.1)
  plt.title('Sinusoidal Wave')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  # 
  plt.subplot(4,1,2)
  plt.plot(cos, scalex=0.5, scaley=0.1)
  plt.title('Cosinus Wave')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')
  # 
  plt.subplot(4,1,3)
  plt.plot(squ, scalex=0.5, scaley=0.1)
  plt.title('Square Wave')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')
  # 
  plt.subplot(4,1,4)
  plt.plot(saw, scalex=0.5, scaley=0.1)
  plt.title('Sawtooth Wave')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Time (s)')
  plt.ylabel('Amplitude')
  plt.tight_layout()
  graph = getGraph()
  return graph
# ---------------------------------------------------------------------------------------------
""" AM DSBFC """
# Plot for AM DSBFC - Time Domain
def fcT(fcPlot,x):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,3))

  if fcPlot == 'message-timeDomain':
    plt.title('Message Signal m(t)')
  elif fcPlot == 'carrier-timeDomain':
    plt.title('Carrier Signal c(t)')
  elif fcPlot == 'modulated-timeDomain':
    plt.title('Modulated Signal')
  elif fcPlot == 'envelope-timeDomain':
    plt.title('Envelope on Modulated Signal')
  elif fcPlot == 'demodulated-timeDomain':
    plt.title('Demodulated Signal')

  plt.plot(x, scalex=0.5, scaley=0.1)
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Time (s)')
  plt.ylabel('Amplitude')
  plt.tight_layout()
  graph = getGraph()
  return graph
# Plot for DSBFC All - Time Domain
def dsbfcT(mt,ct,fcModT,fcEnvT,fcDemodT):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,12))
  # 
  plt.subplot(4,1,1)
  plt.plot(mt, scalex=0.5, scaley=0.1)
  plt.title('Message Signal m(t)')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')
  # 
  plt.subplot(4,1,2)
  plt.plot(ct, scalex=0.5, scaley=0.1)
  plt.title('Carrier Signal c(t)')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')
  # 
  plt.subplot(4,1,3)
  plt.plot(fcModT, label='Modulated Signal', scalex=0.5, scaley=0.1)
  plt.plot(fcEnvT, label='Envelope', scalex=0.5, scaley=0.1)
  plt.title('Modulated Signal with Envelope')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')
  plt.legend()
  # 
  plt.subplot(4,1,4)
  plt.plot(fcDemodT, scalex=0.5, scaley=0.1)
  plt.title('Demodulated Signal')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Time (s)')
  plt.ylabel('Amplitude')
  plt.tight_layout()
  graph = getGraph()
  return graph
# Plot for AM DSBFC - Frequency Domain
def fcF(fcPlot,xf,x):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,3))
  # 
  if fcPlot == 'message-frequencyDomain':
    plt.title('Message Signal')
  elif fcPlot == 'carrier-frequencyDomain':
    plt.title('Carrier Signal')
  elif fcPlot == 'modulated-frequencyDomain':
    plt.title('Modulated Signal')
  elif fcPlot == 'envelope-frequencyDomain':
    plt.title('Envelope on Modulated Signal')
  elif fcPlot == 'demodulated-frequencyDomain':
    plt.title('Demodulated Signal')
  # 
  plt.plot(xf,x, scalex=0.5, scaley=0.1)
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Frequency (Hz)')
  plt.ylabel('Amplitude')
  plt.xlim(0,200)         # Sementara dibatasi segitu dulu
  plt.tight_layout()
  graph = getGraph()
  return graph
# Plot for DSBFC All - Frequency Domain
def dsbfcF(xf,mf,cf,fcModF,fcEnvF,fcDemodF):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,6))
  # 
  plt.subplot(2,1,1)
  plt.plot(xf,mf,label='Message Signal', scalex=0.5, scaley=0.1)
  plt.plot(xf,cf,label='Carrier Signal', scalex=0.5, scaley=0.1)
  plt.title('Message and Carrier Signal')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')
  plt.legend()
  plt.xlim(0,200)         # Sementara dibatasi segitu dulu
  # 
  plt.subplot(2,1,2)
  plt.plot(xf,fcModF,label='Modulated Signal', scalex=0.5, scaley=0.1)
  plt.plot(xf,fcEnvF,label='Envelope', scalex=0.5, scaley=0.1)
  plt.plot(xf,fcDemodF,label='Demodulated Signal', scalex=0.5, scaley=0.1)
  plt.title('DSBFC Modulation and Demodulation')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Frequency (Hz)')
  plt.ylabel('Amplitude')
  plt.legend()
  plt.xlim(0,200)         # Sementara dibatasi segitu dulu
  plt.tight_layout()
  graph = getGraph()
  return graph
# ---------------------------------------------------------------------------------------------
""" AM DSBSC """
# Plot for AM DSBSC - Time Domain
def scT(scPlot,x):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,3))

  if scPlot == 'message-timeDomain':
    plt.title('Message Signal m(t)')
  elif scPlot == 'carrier-timeDomain':
    plt.title('Carrier Signal c(t)')
  elif scPlot == 'modulated-timeDomain':
    plt.title('Modulated Signal')
  elif scPlot == 'demodulated-timeDomain':
    plt.title('Demodulated Signal')
  elif scPlot == 'filtered-timeDomain':
    plt.title('Demodulated and Filtered Signal')

  plt.plot(x, scalex=0.5, scaley=0.1)
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Time (s)')
  plt.ylabel('Amplitude')

  plt.tight_layout()
  graph = getGraph()
  return graph
# Plot for DSBSC All - Time Domain
def dsbscT(mt,ct,scModT,scDemodT,scFiltT):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,12))
  # 
  plt.subplot(4,1,1)
  plt.plot(mt, scalex=0.5, scaley=0.1)
  plt.title('Message Signal m(t)')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')
  # 
  plt.subplot(4,1,2)
  plt.plot(ct, scalex=0.5, scaley=0.1)
  plt.title('Carrier Signal c(t)')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')
  # 
  plt.subplot(4,1,3)
  plt.plot(scModT,label='Modulated Signal', scalex=0.5, scaley=0.1)
  plt.plot(scDemodT,label='Demodulated Signal', scalex=0.5, scaley=0.1)
  plt.title('Modulated and Demodulated Signal')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')
  plt.legend()
  # 
  plt.subplot(4,1,4)
  plt.plot(scFiltT, scalex=0.5, scaley=0.1)
  plt.title('Filtered Signal')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Time (s)')
  plt.ylabel('Amplitude')
  plt.tight_layout()
  graph = getGraph()
  return graph
# Plot for AM DSBSC - Frequency Domain
def scF(scPlot,xf,x):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,3))

  if scPlot == 'message-frequencyDomain':
    plt.title('Message Signal')
  elif scPlot == 'carrier-frequencyDomain':
    plt.title('Carrier Signal')
  elif scPlot == 'modulated-frequencyDomain':
    plt.title('Modulated Signal')
  elif scPlot == 'demodulated-frequencyDomain':
    plt.title('Demodulated Signal')
  elif scPlot == 'filtered-frequencyDomain':
    plt.title('Demodulated and Filtered Signal')
  
  plt.plot(xf,x, scalex=0.5, scaley=0.1)
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Frequency (Hz)')
  plt.ylabel('Amplitude')
  plt.xlim(0,200)         # Sementara dibatasi segini dulu
  plt.tight_layout()
  graph = getGraph()
  return graph
# Plot for DSBSC All - Frequency Domain
def dsbscF(xf,mf,cf,scModF,scDemodF,scFiltF):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,6))

  plt.subplot(2,1,1)
  plt.plot(xf,mf,label='Message Signal', scalex=0.5, scaley=0.1)
  plt.plot(xf,cf,label='Carrier Signal', scalex=0.5, scaley=0.1)
  plt.title('Message and Carrier Signal')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')
  plt.legend()
  plt.xlim(0,200)         # Sementara dibatasi segini dulu

  plt.subplot(2,1,2)
  plt.plot(xf,scModF,label='Modulated Signal', scalex=0.5, scaley=0.1)
  plt.plot(xf,scDemodF,label='Demodulated Signal', scalex=0.5, scaley=0.1)
  plt.plot(xf,scFiltF,label='Filtered Signal', scalex=0.5, scaley=0.1)
  plt.title('DSBSC Modulation and Demodulation')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Frequency (Hz)')
  plt.ylabel('Amplitude')
  plt.legend()
  plt.xlim(0,200)         # Sementara dibatasi segini dulu
  plt.tight_layout()
  graph = getGraph()
  return graph
# ---------------------------------------------------------------------------------------------
""" AM SSB """
# Plot for AM SSB - Time Domain
def ssT(ssPlot,x):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,3))

  if ssPlot == 'message-timeDomain':
    plt.title('Message Signal m(t)')
  elif ssPlot == 'carrier-timeDomain':
    plt.title('Carrier Signal c(t)')
  elif ssPlot == 'modulated-timeDomain':
    plt.title('Modulated Signal')
  elif ssPlot == 'demodulated-timeDomain':
    plt.title('Demodulated Signal')
  elif ssPlot == 'filtered-timeDomain':
    plt.title('Demodulated and Filtered Signal')
  
  plt.plot(x, scalex=0.5, scaley=0.1)
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Time (s)')
  plt.ylabel('Amplitude')
  plt.tight_layout()
  graph = getGraph()
  return graph
# Plot for SSB All - Time Domain
def ssbT(mt,ct,ssModT,ssDemodT,ssFiltT):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,12))

  plt.subplot(4,1,1)
  plt.plot(mt, scalex=0.5, scaley=0.1)
  plt.title('Message Signal m(t)')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')

  plt.subplot(4,1,2)
  plt.plot(ct, scalex=0.5, scaley=0.1)
  plt.title('Carrier Signal c(t)')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')

  plt.subplot(4,1,3)
  plt.plot(ssModT,label='Modulated Signal', scalex=0.5, scaley=0.1)
  plt.plot(ssDemodT,label='Demodulated Signal', scalex=0.5, scaley=0.1)
  plt.title('Modulated and Demodulated Signal')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')
  plt.legend()

  plt.subplot(4,1,4)
  plt.plot(ssFiltT, scalex=0.5, scaley=0.1)
  plt.title('Filtered Signal')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Time (s)')
  plt.ylabel('Amplitude')
  plt.tight_layout()
  graph = getGraph()
  return graph
# Plot for AM SSB - Frequency Domain
def ssF(ssPlot,xf,x):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,3))

  if ssPlot == 'message-frequencyDomain':
    plt.title('Message Signal')
  elif ssPlot == 'carrier-frequencyDomain':
    plt.title('Carrier Signal')
  elif ssPlot == 'modulated-frequencyDomain':
    plt.title('Modulated Signal')
  elif ssPlot == 'demodulated-frequencyDomain':
    plt.title('Demodulated Signal')
  elif ssPlot == 'filtered-frequencyDomain':
    plt.title('Demodulated and Filtered Signal')
  
  plt.plot(xf,x, scalex=0.5, scaley=0.1)
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Frequency (Hz)')
  plt.ylabel('Amplitude')
  plt.xlim(0,200)         # Sementara dibatasi segitu dulu

  plt.tight_layout()
  graph = getGraph()
  return graph
# Plot for SSB All - Frequency Domain
def ssbF(xf,mf,cf,ssModF,ssDemodF,ssFiltF):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,6))

  plt.subplot(2,1,1)
  plt.plot(xf,mf,label='Message Signal', scalex=0.5, scaley=0.1)
  plt.plot(xf,cf,label='Carrier Signal', scalex=0.5, scaley=0.1)
  plt.title('Message and Carrier Signal')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')
  plt.legend()
  plt.xlim(0,200)         # Sementara dibatasi segitu dulu

  plt.subplot(2,1,2)
  plt.plot(xf,ssModF,label='Modulated Signal', scalex=0.5, scaley=0.1)
  plt.plot(xf,ssDemodF,label='Demodulated Signal', scalex=0.5, scaley=0.1)
  plt.plot(xf,ssFiltF,label='Filtered Signal', scalex=0.5, scaley=0.1)
  plt.title('SSB Modulation and Demodulation')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Frequency (Hz)')
  plt.ylabel('Amplitude')
  plt.legend()
  plt.xlim(0,200)         # Sementara dibatasi segitu dulu

  plt.tight_layout()
  graph = getGraph()
  return graph
# ---------------------------------------------------------------------------------------------
""" FM MODULATION """
# Plot for FM Modulation - Time Domain
def fmT(fmPlot,x):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,3))

  if fmPlot == 'message-timeDomain':
    plt.title('Message Signal m(t)')
  elif fmPlot == 'carrier-timeDomain':
    plt.title('Carrier Signal c(t)')
  elif fmPlot == 'modulated-timeDomain':
    plt.title('Modulated Signal')
  elif fmPlot == 'demodulated-timeDomain':
    plt.title('Demodulated Signal')

  plt.plot(x, scalex=0.5, scaley=0.1)
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Time (s)')
  plt.ylabel('Amplitude')

  plt.tight_layout()
  graph = getGraph()
  return graph
# Plot for FM Modulation All - Time Domain
def fmAllT(mt,ct,fmModT,fmDemodT):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,12))

  plt.subplot(4,1,1)
  plt.plot(mt, scalex=0.5, scaley=0.1)
  plt.title('Message Signal m(t)')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')

  plt.subplot(4,1,2)
  plt.plot(ct, scalex=0.5, scaley=0.1)
  plt.title('Carrier Signal c(t)')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')

  plt.subplot(4,1,3)
  plt.plot(fmModT, scalex=0.5, scaley=0.1) 
  plt.title('Modulated Signal')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')

  plt.subplot(4,1,4)
  plt.plot(fmDemodT, scalex=0.5, scaley=0.1)
  plt.title('Demodulated  Signal')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Time (s)')
  plt.ylabel('Amplitude')

  plt.tight_layout()
  graph = getGraph()
  return graph
# Plot for FM Modulation - Frequency Domain
def fmF(fmPlot,ctF,xf,x):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,3))

  if fmPlot == 'message-frequencyDomain':
    plt.title('Message Signal')
  elif fmPlot == 'carrier-frequencyDomain':
    plt.title('Carrier Signal')
  elif fmPlot == 'modulated-frequencyDomain':
    plt.title('Modulated Signal')
  elif fmPlot == 'demodulated-frequencyDomain':
    plt.title('Demodulated Signal')
  
  plt.plot(xf,x, scalex=0.5, scaley=0.1)
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Frequency (Hz)')
  plt.ylabel('Amplitude')
  plt.xlim(0,2*ctF)

  plt.tight_layout()
  graph = getGraph()
  return graph
# Plot for FM Modulation All - Frequency Domain
def fmAllF(xf,ctF,mf,cf,fmModF,fmDemodF):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,6))

  plt.subplot(2,1,1)
  plt.plot(xf,mf,label='Message Signal', scalex=0.5, scaley=0.1)
  plt.plot(xf,cf,label='Carrier Signal', scalex=0.5, scaley=0.1)
  plt.title('Message and Carrier Signal')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')
  plt.legend()
  plt.xlim(0,2*ctF)

  plt.subplot(2,1,2)
  plt.plot(xf,fmModF,label='Modulated Signal', scalex=0.5, scaley=0.1)
  plt.plot(fmDemodF,label='Demodulated Signal', scalex=0.5, scaley=0.1)                # Masih ada masalah diemensi array di demodulasi FM - Freq. Domain, di Time Domain gaada masalah
  plt.title('DSBSC Modulation and Demodulation')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.xlabel('Frequency (Hz)')
  plt.ylabel('Amplitude')
  plt.legend()
  plt.xlim(0,2*ctF)

  plt.tight_layout()
  graph = getGraph()
  return graph
# ---------------------------------------------------------------------------------------------
def diOne(plot, x):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,3))

  if plot == 'message':
    plt.title('Message Signal')
  elif plot == 'modulated-timeDomain':
    plt.title('Modulated Signal in Time Domain')
  elif plot == 'modulated-frequencyDomain':
    plt.title('Modulated Signal in Frequency Domain')

  plt.plot(x, scalex=0.5, scaley=0.1)
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')

  plt.tight_layout()
  graph = getGraph()
  return graph

def diAll(mt, mod, modF, modZ):
  plt.switch_backend('AGG')
  plt.figure(figsize=(12,9))

  plt.subplot(3,1,1)
  plt.plot(mt)
  plt.title('Message Signal')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')

  plt.subplot(3,1,2)
  plt.plot(mod, scalex=0.5, scaley=0.1)
  plt.title('Modulated Signal - Time Domain')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')

  plt.subplot(3,1,3)
  plt.plot(modF, modZ, scalex=0.5, scaley=0.1) 
  plt.title('Modulated Signal')
  plt.grid(b=True, which='major', color='#666666', linestyle='-')
  plt.minorticks_on()
  plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
  plt.ylabel('Amplitude')

  plt.tight_layout()
  graph = getGraph()
  return graph



# def amDSBFC(mt, mtA, fs, mtF, ct, ctA, ctF, fcPlot, fcDom):
# 	mt = message(mt, mtA, fs, mtF)															# Fungsi isyarat message
# 	ct = carrier(ct, ctA, fs, ctF)															# Fungsi isyarat carrier
# 	fcMod   = dsbfc_mod(mt,ct)             										# Fungsi modulasi        
# 	fcEnv   = envelope(fcMod)             										# Fungsi deteksi selubung
# 	fcDemod = dsbfc_demod(fcEnv, ctA)     										# Fungsi demodulasi
# 	if fcDom == 'frequencyDomain':
# 		xf = xProp(mt, fs)																					# Fungsi x axis properties untuk frekuensi
# 		fcMod   = freq(fcMod)             										# Fungsi modulasi        
# 		fcEnv   = freq(fcEnv)             										# Fungsi deteksi selubung
# 		fcDemod = freq(fcDemod)     										# Fungsi demodulasi
# 		mt = freq(mt)
# 		ct = freq(ct)
# 	# Fungsi Plotting
# 	if fcPlot == 'message':
# 		fcShow = p.one(fcPlot,fcDom,mt,xf,ctF)																	# Plotting untuk waveform isyarat pemodulasi 
# 	elif fcPlot == 'carrier':
# 		fcShow = p.one(fcPlot,fcDom,ct,xf,ctF)																	# Plotting untuk waveform isyarat pembawa    
# 	elif fcPlot == 'modulated':
# 		fcShow = p.one(fcPlot,fcDom,fcMod,xf,ctF)															# Plotting untuk waveform isyarat termodulasi
# 	elif fcPlot == 'envelope':
# 		fcShow = p.one(fcPlot,fcDom,fcEnv,xf,ctF)															# Plotting untuk waveform deteksi selubung   
# 	elif fcPlot == 'demodulated':
# 		fcShow = p.one(fcPlot,fcDom,fcDemod,xf,ctF)														# Plotting untuk waveform isyarat demodulasi
# 	elif fcPlot == 'dsbfc':
# 		fcShow = p.dsbfc(mt, ct, fcMod, fcEnv, fcDemod, xf)				# Plotting untuk waveform semua tahap        
# 	return fcShow
