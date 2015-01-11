import pyaudiogame as pag
from pag import mixer

if __name__ == '__main__':
	class MyApp(pag.App):
		def set_defaults(self):
			self.exit_key = 2

		sound = mixer.Sound("menu_change.ogg")
		def logic(self, actions):
			if actions['key'] == "f":
				self.sound.play()
			elif actions['key'] == "d":
				self.key_repeat(on=True, delay=200)
			elif actions['key'] == "space":
				self.key_repeat(on=False)

	MyApp().run()