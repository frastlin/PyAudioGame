from direct.showbase.ShowBase import ShowBase
from direct.showbase import Audio3DManager
from pandac.PandaModules import WindowProperties
#The module wide variables.

class App(ShowBase):
	"""
The master app for pyaudiogame. Call this like:
my_app = pyaudiogame.App("My App")
"""

	def __init__(self, title="Pyaudiogame App", disable_mouse=True, cursor_hidden=False, fullscreen=False):
		ShowBase.__init__(self)
		#Controlls the window setting. Call self.window_settings.functionName to change this directly. Then call change_settings with no arguments. For more advanced operations than found in self.change_settings, read: https://www.panda3d.org/reference/1.8.1/python/classpanda3d.core.WindowProperties.php
		self.window_settings = WindowProperties()
		self.change_settings(title=title, disable_mouse=disable_mouse, cursor_hidden=cursor_hidden, fullscreen=fullscreen)

	def change_settings(self, title=None, disable_mouse=None, cursor_hidden=None, fullscreen=None):
		if title:self.window_settings.setTitle(title)
		if disable_mouse != None:self.disableMouse()
		if cursor_hidden != None:self.window_settings.setCursorHidden(cursor_hidden)
		if fullscreen != None:self.window_settings.setFullscreen(fullscreen)
		self.win.requestProperties(self.window_settings)

	def get_settings(self, setting=None):
		"""Pass a string of the setting name if you wish just that item to be returned. Otherwise, just leave it blank and a dict of all settings will be returned"""
		w = self.window_settings
		sd = {'title': w.getTitle(), 'fullscreen': w.getFullscreen(), 'cursor_hidden': w.getCursorHidden()}
		if setting:return sd.get(setting)



	def audio3d(self, player=None, manager=0, listener=None):
		"""Enter an object for the first argument and a number of the audio manager for the second. Default player and listener is camera and default audio manager is OpenAL"""
		if not player:player = self.camera
		if not listener:listener = self.camera
		a3d = Audio3DManager.Audio3DManager(base.sfxManagerList[manager], player)
		a3d.attachListener(listener)
		return a3d

	def new_object(self, *args, **kwargs):
		"""Shortens the create node operation"""
		return self.render.attachNewNode(*args, **kwargs)

if __name__ == '__main__':
	my_app = App("My App")
	my_app.change_settings(title="fred")

	print(my_app.get_settings('title'))
	my_app.run()
