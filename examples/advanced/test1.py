import pyaudiogame
from pyaudiogame import mixer
from pyaudiogame.ui.menus import add_menu
from pyaudiogame.ui.typer import add_typer
from pyaudiogame import cash
from pyaudiogame.speech import speak as spk

sound = mixer.Sound("menu_change.ogg")
cash.menus = {}

def game(self, actions):
	if actions['key'] == "space":
		spk("This is accessible_output talking to you")

def game2(self, actions):
	#s = add_menu(actions=actions, title="Test menu from test1", options=["Yes", "No", "Maybe"], dict=cash.menus)
	add_typer(actions, name="name", title="User name:")

def game1(self, actions):
	if actions['key'] == "f":
		sound.play()
	elif actions['key'] == "d":
		self.key_repeat(on=True, delay=200)
	elif actions['key'] == "space":
		self.key_repeat(on=False)

if __name__ == '__main__':
	class MyApp(pyaudiogame.App):
		def set_defaults(self):
			self.exit_key = 2
		def logic(self, actions):
			return game(self, actions)

	MyApp().run()