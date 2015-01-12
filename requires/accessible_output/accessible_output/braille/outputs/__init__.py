import platform

_system = platform.system()

if _system == 'Windows':
 from jaws import Jaws
 from nvda import NVDA
 from sa import SystemAccess
 from we import WindowEyes
 
 __all__ = ["Jaws", "NVDA", "SystemAccess", "WindowEyes"]
else:
 __all__ = []
