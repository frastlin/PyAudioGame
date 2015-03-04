#dict out
import pyaudiogame
spk = pyaudiogame.speak
MyApp = pyaudiogame.App("My Application")

clothes_dict = {"1": "head", "2": "body", "3": "hands", "4": "leggs", "5": "feet", "6": "other random thing"}
color_dict = {"1": "red", "2": "green", "3": "orange", "4": "blue", "5": "yellow", "9": "Kind of a muddy brown and yellow together, although they make kind of a blueish green if you put them against a window"}



def logic(actions):
	key = actions['key']

MyApp.logic = logic
MyApp.run()
