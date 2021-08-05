from collections import ChainMap
from django.shortcuts import render
import TelcoWeb.module as m
from .models import Information

txt = {
    'po' : Information.objects.filter(Title='Headline'),
    'sg' : Information.objects.filter(Title='Signal Generator - Materi'),
    'fc' : Information.objects.filter(Title='AM DSBFC - Materi'),
    'sc' : Information.objects.filter(Title='AM DSBSC - Materi'),
    'sb' : Information.objects.filter(Title='AM SSB - Materi'),
    'fm' : Information.objects.filter(Title='FM - Materi'),
    'dg' : Information.objects.filter(Title='Digital - Materi'),}

def telcolab(request):
    txt_home = {'active_tab':'nav-sg-tab'}
    return render(request, 'telcolab/new.html', dict(ChainMap(txt_home,txt)))

def new(request):
    txt_home = {'active_tab':'nav-sg-tab'}
    return render(request, 'telcolab/new.html', dict(ChainMap(txt_home,txt)))
# signal-generator sine
def signalGenerator(request):
    input_signal = request.POST.get('inputSignalGenerator')
    data_signal = input_signal.split()
    try:
        kata,show = m.inputData(data_signal)
        txt_signal = {
            'sgShow' : show,
            'active_tab':'nav-sg-tab'}
        if kata is False:
            raise ValueError('Salah memasukkan kata dalam kode')
    except Exception as e:
        print(e)
        txt_signal = {
            'typoCodeSignalGenerator': e,
            'active_tab':'nav-sg-tab'}
    return render(request, 'telcolab/new.html', dict(ChainMap(txt_signal,txt)))

def dsbfcModulation(request):
    input_dsbfc = request.POST.get('inputDSBFC')
    data_dsbfc = input_dsbfc.split()
    try:
        kata,show = m.inputData(data_dsbfc)
        txt_dsbfc = {
            'fcShow' : show,
            'active_tab':'nav-fc-tab'}
        if kata is False:
            raise ValueError('Salah memasukkan kata dalam kode')
    except Exception as e:
        print(e)
        txt_dsbfc = {
            'typoCodeDSBFC': e,
            'active_tab':'nav-fc-tab'}
    return render(request, 'telcolab/new.html', dict(ChainMap(txt_dsbfc,txt)))

def dsbscModulation(request):
    input_dsbsc = request.POST.get('inputDSBSC')
    data_dsbsc = input_dsbsc.split()
    try:
        kata,show = m.inputData(data_dsbsc)
        txt_dsbsc = {
            'scShow' : show,
            'active_tab':'nav-sc-tab'}
        if kata is False:
            raise ValueError('Salah memasukkan kata dalam kode')
    except Exception as e:
        print(e)
        txt_dsbsc = {
            'typoCodeDSBSC': e,
            'active_tab':'nav-sc-tab'}
    return render(request, 'telcolab/new.html', dict(ChainMap(txt_dsbsc,txt)))

def ssbModulation(request):
    input_ssb = request.POST.get('inputSSB')
    data_ssb = input_ssb.split()
    try:
        kata,show = m.inputData(data_ssb)
        txt_ssb = {
            'ssShow' : show,
            'active_tab':'nav-ss-tab'}
        if kata is False:
            raise ValueError('Salah memasukkan kata dalam kode')
    except Exception as e:
        print(e)
        txt_ssb = {
            'typoCodeSSB': e,
            'active_tab':'nav-ss-tab'}
    return render(request, 'telcolab/new.html', dict(ChainMap(txt_ssb,txt)))

def frequencyModulation(request):
    input_fm = request.POST.get('inputFM')
    data_fm = input_fm.split()
    try:
        kata,show = m.inputData(data_fm)
        txt_fm = {
            'fmShow' : show,
            'active_tab':'nav-fm-tab'}
        if kata is False:
            raise ValueError('Salah memasukkan kata dalam kode')
    except Exception as e:
        print(e)
        txt_fm = {
            'typoCodeFM': e,
            'active_tab':'nav-fm-tab'}
    return render(request, 'telcolab/new.html', dict(ChainMap(txt_fm,txt)))

def digitalModulation(request):
    input_digital = request.POST.get('inputDigitalModulation')
    data_digital = input_digital.split()
    try:
        kata,show = m.inputData(data_digital)
        txt_digital = {
            'diShow' : show,
            'active_tab':'nav-dg-tab'}
        if kata is False:
            raise ValueError('Salah memasukkan kata dalam kode')
    except Exception as e:
        print(e)
        txt_digital = {
            'typoCodeDigital': e,
            'active_tab':'nav-dg-tab'}
    return render(request, 'telcolab/new.html', dict(ChainMap(txt_digital,txt)))
