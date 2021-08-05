from io import BytesIO
import base64
import matplotlib.pyplot as plt

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format = 'png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot_one(plot, domain, time, x, xf, carrier_freq):
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
    if plot == 'message-waveform':
        plt.title('Message Signal')
    elif plot == 'carrier-waveform':
        plt.title('Carrier Signal')
    elif plot == 'modulated-waveform':
        plt.title('Modulated Signal')
    elif plot == 'demodulated-waveform':
        plt.title('Demodulated Signal')
    elif plot == 'filtered-waveform':
        plt.title('Filtered Signal')
    # Membedakan plot untuk time domain dan frequency domain
    if domain == 'time-domain':
        plt.plot(time, x, scalex=0.5, scaley=0.1, c='#004266')
        plt.ylabel('Amplitude (V)')
        plt.xlabel('Time (s)')
    elif domain == 'frequency-domain':
        plt.plot(xf, x, scalex=0.5, scaley=0.1, c='#004266')
        plt.ylabel('Amplitude')
        plt.xlim(0,2*carrier_freq)
        plt.xlabel('Frequency (Hz)')
    plt.grid(b=True, which='major', c='#666666')
    plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
    plt.minorticks_on()
    plt.tight_layout()
    return get_graph()

def get_plot_all(plot, time, message, carrier, modulated, demodulated, other, xf, carrier_freq, domain):
    plt.switch_backend('AGG')
    if domain == 'time-domain':
        plt.figure(figsize=(12,12))
        # Plot Isyarat Pemodulasi - Message Signal
        plt.subplot(4,1,1)
        plt.plot(time, message, scalex=0.5, scaley=0.1, c='#004266')
        if plot == 'signal':
            plt.title('Sinusoidal Wave')
        else:
            plt.title('Message Signal')
        plt.grid(b=True, which='major', c='#666666')
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.minorticks_on()
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude (V)')
        # Plot Isyarat Pembawa - Carrier Signal
        plt.subplot(4,1,2)
        plt.plot(time, carrier, scalex=0.5, scaley=0.1, c='#004266')
        if plot == 'signal':
            plt.title('Cosinus Wave')
        else:
            plt.title('Carrier Signal')
        plt.grid(b=True, which='major', c='#666666')
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.minorticks_on()
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude (V)')
        # Plot Isyarat Termodulasi - Modulated Signal
        plt.subplot(4,1,3)
        if plot == 'signal':
            plt.plot(time, modulated, scalex=0.5, scaley=0.1, c='#004266')
            plt.title('Square Wave')
        elif plot == 'fm-waveform':
            plt.plot(time, modulated, scalex=0.5, scaley=0.1, c='#004266')
            plt.title('Modulated Signal')
        else:
            plt.plot(time, modulated, label='Modulated Signal', scalex=0.5, scaley=0.1, c='#004266')
            if plot == 'dsbfc-waveform':
                plt.plot(time, other, label='Envelope', scalex=0.5, scaley=0.1, c='#D500FF')
                plt.title('Modulated Signal with Envelope')
            else:
                plt.plot(time, demodulated, label='Demodulated Signal', scalex=0.5, scaley=0.1, c='#D500FF')
                plt.title('Modulated and Demodulated Signal')
            plt.legend()
        plt.grid(b=True, which='major', c='#666666')
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.minorticks_on()
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude (V)')
        # Plot Isyarat Demodulasi - Demodulated Signal
        plt.subplot(4,1,4)
        if plot == 'signal':
            plt.plot(time, demodulated, scalex=0.5, scaley=0.1, c='#004266')
            plt.title('Sawtooth/Triangle Wave')
        elif plot == 'dsbfc-waveform':
            plt.plot(time, demodulated, scalex=0.5, scaley=0.1, c='#004266')
            plt.title('Demodulated Signal')
        elif plot == 'fm-waveform':
            plt.plot(demodulated, scalex=0.5, scaley=0.1, c='#004266')
            plt.title('Demodulated Signal')
        else:
            plt.plot(time, other, scalex=0.5, scaley=0.1, c='#004266')
            plt.title('Filtered Signal')
        plt.grid(b=True, which='major', c='#666666')
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.minorticks_on()
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude (V)')
    # Plotting untuk Frequency Domain
    elif domain == 'frequency-domain':
        plt.figure(figsize=(12,6))
        # Plot Isyarat Pemodulasi dan Pembawa
        plt.subplot(2,1,1)
        plt.plot(xf, message, label='Message Signal', scalex=0.5, scaley=0.1, c='#FF7700')
        plt.plot(xf, carrier, label='Carrier Signal', scalex=0.5, scaley=0.1, c='#004266')
        plt.title('Message and Carrier Signal')
        plt.grid(b=True, which='major', c='#666666',)
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.minorticks_on()
        plt.ylabel('Amplitude')
        plt.legend()
        plt.xlim(0,2*carrier_freq)
        # Plot Isyarat Termodulasi, Filter/Envelope, Demodulasi
        plt.subplot(2,1,2)
        if plot == 'dsbfc-waveform':
            plt.plot(xf, modulated, label='Modulated Signal', scalex=0.5, scaley=0.1, c='#FF7700')
            plt.plot(xf, demodulated, label='Demodulated Signal', scalex=0.5, scaley=0.1, c='#004266')
        elif plot == 'fm-waveform':
            plt.plot(modulated, label='Modulated Signal', scalex=0.5, scaley=0.1, c='#FF7700')
            plt.plot(demodulated, label='Demodulated Signal', scalex=0.5, scaley=0.1, c='#004266')
        else:
            plt.plot(xf, modulated, label='Modulated Signal', scalex=0.5, scaley=0.1, c='#FF7700')
            plt.plot(xf, demodulated, label='Demodulated Signal', scalex=0.5, scaley=0.1, c='#004266')
            plt.plot(xf, other, label='Filtered Signal', scalex=0.5, scaley=0.1, c='#00FF00')
        plt.title('Modulation and Demodulation')
        plt.grid(b=True, which='major', c='#666666')
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.minorticks_on()
        plt.xlabel('Frequency')
        plt.ylabel('Amplitude')
        plt.legend()
        plt.xlim(0,2*carrier_freq)
    plt.tight_layout()
    return get_graph()

def get_plot_digital(time, digital_plot, y1, y2, y3, xf, yf, message_signal, carrier_freq, carrier_signal, y1_demod):
    plt.switch_backend('AGG')
    if digital_plot == 'digital-modulation':
        plt.figure(figsize=(12,21))
        # Plot untuk Message Signal - Random Binary Sequence
        plt.subplot(7,1,1)
        plt.plot(message_signal, scalex=0.5, scaley=0.1, c='#FF7700')
        plt.title('Message Signal - Random Binary Sequence')
        plt.grid(b=True, which='major', c='#666666')
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.minorticks_on()
        plt.xlabel('Sampling Frequency (Hz)')
        plt.ylabel('Amplitude (V)')
        # Plot untuk Carrier Signal
        plt.subplot(7,1,2)
        plt.plot(time, carrier_signal, scalex=0.5, scaley=0.1, c='#004266')
        plt.title('Carrier Signal')
        plt.grid(b=True, which='major', c='#666666')
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.minorticks_on()
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude (V)')
        # Plot untuk output Modulasi Digital BASK
        plt.subplot(7,1,3)
        plt.plot(time, y1, scalex=0.5, scaley=0.1, c='#D500FF')
        plt.title('BASK Modulation Output')
        plt.grid(b=True, which='major', c='#666666')
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.minorticks_on()
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude (V)')
        # Plot untuk output Modulasi Digital BFSK
        plt.subplot(7,1,4)
        plt.plot(time, y2, scalex=0.5, scaley=0.1, c='#D500FF')
        plt.title('BFSK Modulation Output')
        plt.grid(b=True, which='major', c='#666666')
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.minorticks_on()
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude (V)')
        # Plot untuk output Modulasi Digital BPSK
        plt.subplot(7,1,5)
        plt.plot(time, y3, scalex=0.5, scaley=0.1, c='#D500FF')
        plt.title('BPSK Modulation Output')
        plt.grid(b=True, which='major', c='#666666')
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.minorticks_on()
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude (V)')
        # Plot untuk output Demodulasi Digital
        plt.subplot(7,1,6)
        plt.plot(y1_demod, scalex=0.5, scaley=0.1, c='#004266')
        plt.title('Demodulated Signal - Random Binary Sequence')
        plt.grid(b=True, which='major', c='#666666')
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.minorticks_on()
        plt.xlabel('Sampling Frequency (Hz)')
        plt.ylabel('Amplitude (V)')
        # Plot untuk output Ranah Frekuensi
        plt.subplot(7,1,7)
        plt.plot(xf, yf, scalex=0.5, scaley=0.1, c='#FF7700')
        plt.title('Frequency Domain Graph')
        plt.grid(b=True, which='major', c='#666666')
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.xlim(0, 2*carrier_freq)
        plt.minorticks_on()
    else:
        plt.figure(figsize=(12,15))
        # Plot untuk Message Signal - Random Binary Sequence
        plt.subplot(5,1,1)
        plt.plot(message_signal, scalex=0.5, scaley=0.1, c='#FF7700')
        plt.title(digital_plot + ' Random Binary Sequence')
        plt.grid(b=True, which='major', c='#666666')
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.minorticks_on()
        plt.xlabel('Sampling Frequency (Hz)')
        plt.ylabel('Amplitude (V)')
        # Plot untuk Carrier Signal
        plt.subplot(5,1,2)
        plt.plot(time, carrier_signal, scalex=0.5, scaley=0.1, c='#004266')
        plt.title(digital_plot + ' Random Binary Sequential')
        plt.grid(b=True, which='major', c='#666666')
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.minorticks_on()
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude (V)')
        # Plot untuk output Modulasi Digital
        plt.subplot(5,1,3)
        plt.plot(time, y1, scalex=0.5, scaley=0.1, c='#FF7700')
        plt.title(digital_plot + ' Modulation Output')
        plt.grid(b=True, which='major', c='#666666')
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.minorticks_on()
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude (V)')
        # Plot untuk output Demodulasi Digital
        plt.subplot(5,1,4)
        plt.plot(y1_demod, scalex=0.5, scaley=0.1, c='#004266')
        plt.title(digital_plot + ' Demodulation Output')
        plt.grid(b=True, which='major', c='#666666')
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.minorticks_on()
        plt.xlabel('Sampling Frequency (Hz)')
        plt.ylabel('Amplitude (V)')
        # Plot untuk output Ranah Frekuensi
        plt.subplot(5,1,5)
        plt.plot(xf, yf, scalex=0.5, scaley=0.1, c='#FF7700')
        plt.title(digital_plot + ' Frequency Domain Graph')
        plt.grid(b=True, which='major', c='#666666')
        plt.grid(b=True, which='minor', c='#999999', alpha=0.2)
        plt.xlim(0, 2*carrier_freq)
        plt.minorticks_on()
    plt.tight_layout()
    return get_graph()