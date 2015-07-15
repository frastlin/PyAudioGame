from app import App as _App
app = _App(title="Pyaudiogame", disable_mouse=True)
import storage
import ui.__init__
from speech import speak
audio3d = app.audio3d()
load_sfx = app.loader.loadSfx
loadSfx = app.loader.loadSfx

