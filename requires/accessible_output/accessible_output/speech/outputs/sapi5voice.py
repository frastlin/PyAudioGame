from collections import OrderedDict
import win32com.client

sapi5 = win32com.client.Dispatch("SAPI.SPVoice")

def available_voices():
 _voices = OrderedDict()
 for v in sapi5.GetVoices():
  _voices[v.GetDescription()] = v
 return _voices

def list_voices():
 return available_voices().keys()
