import platform

_system = platform.system()

if _system == 'Windows':
 from jaws import Jaws
 from nvda import NVDA
 from sa import SystemAccess
 from sapi5 import Sapi5
 from we import WindowEyes
 from dolphin import Dolphin
 __all__ = ["Dolphin", "Jaws", "NVDA", "Sapi5", "SystemAccess", "WindowEyes"]
elif _system == 'Darwin':
 from voiceover import VoiceOver
 __all__ = ["VoiceOver"]
elif _system == 'Linux':
 from speech_d import SpeechDispatcherOutput
 __all__ = ['SpeechDispatcherOutput']
