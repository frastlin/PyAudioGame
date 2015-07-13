from direct.showbase.ShowBase import ShowBase
from direct.showbase import Audio3DManager
from panda3d.core import ConfigVariableString

#The module wide variables.

class App(ShowBase):
	"""
The master app for pyaudiogame. Call this like:
my_app = pyaudiogame.App("My App")
"""

	def __init__(self, title=None):
		self._title = ConfigVariableString('window-title', title, "Set title by pyaudiogame")
#		self._fullscreen = ConfigVariableString('fullscreen', False, 'Changes the size of the screen')
		self._graphics = ConfigVariableString('load-display', 'pandadx9', 'changes the display engine')

		ShowBase.__init__(self)


	def audio3d(self, player=None, manager=0):
		"""Enter an object for the first argument and a number of the audio manager for the second. Default player is camera and default audio manager is OpenAL"""
		if not player:player = self.camera
		return Audio3DManager.Audio3DManager(base.sfxManagerList[manager], player)


if __name__ == '__main__':
	my_app = App("My App")
	my_app.change_title("fred")


	my_app.run()
