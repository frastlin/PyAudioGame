#Speaks text in the way I wish without hard-coding accessible_output like normal.

# here are the dependencies for the below packages:
# libloader:
# http://hg.q-continuum.net/libloader/
# platform_utils:
# http://hg.q-continuum.net/platform_utils/

#Here is the link to the below package:
# http://hg.q-continuum.net/accessible_output2/

from .accessible_output2.outputs import auto
spk = auto.Auto().output

"""
try:
	from .accessible_output2.outputs import auto
	spk = accessible_output2.outputs.auto.Auto().output
except:
	try:
		#here is the link for the below package:
		# http://hg.q-continuum.net/accessible_output/
		from accessible_output import speech
		spk = speech.Speaker().output
	except:
		print("No speech package installed, using print")
		spk = lambda text: print(text)
"""

speechOn = True
always_print = False
lexicon = {' ': 'space', '\n': 'carriage return'}

def speak(text, silent=False, also_print=False):
	"""Is the leading function for speech"""
	text = str(text)
	if text in lexicon:
		text = lexicon.get(text, text)
	if speechOn and not silent:
		spk(text)
	if always_print or also_print:
		print(text)
	return Text(text)

class Text(object):
	"""Deals with processing of text"""
	def __init__(self, text):
		self.text = text
		self.word_position = 0
		self.letter_position = 0
		self.current_word = None
		self.current_letter = text[0]
		self.word_list = text.split(' ')
		for i in self.word_list:
			if i != self.word_list[-1]:
				i = " " + i

	def letter_to_word(self):
		"""Will look at the number of the letter and figure out where in the string it is and return the current word"""
		number_list = []
		n = 0
		for i in self.word_list:
			number_list.append([n, n + len(i)])
			n += len(i)
		for i in number_list:
			if self.letter_position in range(i[0], i[1]):
				self.current_word = self.word_list[number_list.index(i)]
		return self.current_word

	def word_to_letter(self):
		"""Run this and all the current letter and position will be updated"""
		f = self.text.index(self.current_word)
		self.letter_position = f
		self.current_letter = self.text[f]
		return self.current_letter

	def change_letter(self, number, speak=True):
		"""Add or subtract to this to change the current letter"""
		f = self.letter_position + number
		if f < 0:
			self.letter_position = 0
		elif f < len(self.text):
			self.letter_position = f
		else:
			self.letter_position = len(self.text)-1
		self.letter_to_word()
		self.word_position = self.word_list.index(self.current_word)
		self.current_letter = self.text[self.letter_position]
		if speak:
			self.speak(self.current_letter)
		return self.current_letter

	def change_word(self, number, speak=True):
		"""Will move word by word"""
		f = self.word_position + number
		if f < 0:
			self.word_position = 0
		elif f < len(self.word_list):
			self.word_position = f
		else:
			self.word_position = len(self.word_list)-1
		self.current_word = self.word_list[self.word_position]
		self.word_to_letter()
		if speak:
			self.speak(self.current_word)
		return self.current_word

	def navigate(self, command, speak=True):
		"""Call this with the commands: start, end, word_forward, word_back, letter_forward, letter_back"""
		text = self.text
		if command == "start":
			self.letter_position = 0
			self.word_position = 0
			self.letter_to_word()
		elif command == "end":
			self.letter_position = len(text)-1
			self.word_position = len(self.word_list)-1
			self.letter_to_word()
		elif command == "word_back":
			text = self.change_word(-1, False)
		elif command == "word_forward":
			text = self.change_word(1, False)
		elif command == "letter_back":
			text = self.change_letter(-1, False)
		elif command == "letter_forward":
			text = self.change_letter(1, False)
		if speak:
			self.speak(text)
		return text

	def speak(self, text=None):
		"""Will either speak the current text or the text that it is passed"""
		if not text:
			text = self.text
		if text in lexicon:
			text = lexicon.get(text, text)
		spk(text)

	def move(self, actions, speak=True):
		"""Will speak letters and words in a normal windows setting with right and left arrowing through the letters and ctrl+right and left arrow moving through words"""
		key = actions['key']
		mods = actions['mods']
		text = ""
		if key == "left" and not "ctrl" in mods:
			text = self.navigate("letter_back", False)
		elif key == "right" and not "ctrl" in mods:
			text = self.navigate("letter_forward", False)
		elif key == "left" and "ctrl" in mods:
			text = self.navigate("word_back", False)
		elif key == "right" and "ctrl" in mods:
			text = self.navigate("word_forward", False)
		elif key in ["up", "down"]:
			text = self.text
		elif key in "end":
			text = self.navigate("end", False)
		elif key == "home":
			text = self.navigate("start", False)
		if speak and text:
			self.speak(text)
		return text

def main():
	print(current_text)
	while True:
		c = raw_input("< direction?")
		navigate(c)

if __name__ == '__main__':
	f = Text("I like to dance")

	import pyaudiogame
	my_app = pyaudiogame.App("Letters and words")
	storage = pyaudiogame.cash
	storage.text = Text("I like to dance")
	def logic(actions):
		"""This is using the more basic change_letter and change_word functions from the word class"""
		k = actions['key']
		mods = actions['mods']
		if k == "right" and not mods:
			f.change_letter(1)
		elif k == "left" and not mods:
			f.change_letter(-1)
		elif k == "left" and "ctrl" in mods:
			f.change_word(-1)
		elif k == "right" and "ctrl" in mods:
			f.change_word(1)
		elif k == "up":
			f.speak()

	def logic(actions):
		"""This is the most simple way of using actions. You need key and mods keys in the actions dict for this to work. built for use with pyaudiogame"""
		key = actions['key']
		if key == "space":
			storage.text.speak()
		elif key:
			storage.text.move(actions)

	my_app.logic = logic
	my_app.run()
