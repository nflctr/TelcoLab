from matplotlib import pyplot as plt
from scipy import signal as sg
import numpy as np
import sys


freq = 5
freq_samp = 50
amp = 1
t = np.linspace(0, 1, 5 * freq_samp, endpoint = False)

a = amp * np.sin(freq * 2 * np.pi * t)
b = amp * sg.square(2 * np.pi * freq * t, duty=0.3)
c = amp * sg.sawtooth(2 * np.pi * freq * t, width=0.5)

fig, ax = plt.subplots(3)
fig.suptitle('Signal Generator')
#plot gelombang sinus
ax[0].plot(t, a)
ax[0].set_title('Sine Wave')
ax[0].set_ylabel('Signal Amplitude')

#plot gelombang kotak
ax[1].plot(t,b)
ax[1].set_title('Square Wave')

ax[1].set_ylabel('Signal Amplitude')

#plot gelombang segitiga
#plt.figure(figsize=(10,4))
ax[2].plot(t,c)
ax[2].set_title('Triangle Wave')
ax[2].set_xlabel('Time (s)')
ax[2].set_ylabel('Signal Amplitude')
plt.show()

