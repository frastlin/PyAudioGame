#Speaks text in the way I wish without hard-coding accessible_output like normal.
#accessible_output2 has a compiling error and accessible_output2 and accessible_output are not compatible.
#import accessible_output2.outputs.auto
#spk = accessible_output2.outputs.auto.Auto().output

from accessible_output import speech
spk = speech.Speaker().output

current_text = "Hello to the world"
position = [0, 0]
speechOn = True

def speak(text, speech_dict=False):
	"""Is the leading function for speech"""
	global current_text
	position = [0, 0]
	if text in lexicon:
		text = lexicon.get(text, text)
	if speechOn:
		spk(text)
	current_text = text

def navigate(direction):
	"""use word_forward/back, letter_forward/back, top, bottom"""
	text = "nothin yet"
	word_list = current_text.split(' ')
	if direction == "letter_forward":
		position[0] = scroll("forward", position[0], len(current_text))
	elif direction == "letter_back":
		position[0] = scroll("back", position[0], len(current_text))
	elif direction == "word_forward":
		position[1] = scroll("forward", position[1], len(word_list))
	elif direction == "word_back":
		position[1] = scroll("back", position[1], len(word_list))
	if direction in ['letter_forward', 'letter_back']:
		text = current_text[position[0]]
	elif direction in ['word_back', 'word_forward']:
		text = word_list[position[1]]
		position[0] = current_text.index(word_list[position[1]])
	print(text)


def scroll(direction, current_position, length):
	if direction == "forward":
		current_position += 1
	if direction == "back":
		current_position -= 1
	if current_position > length - 1:
		return length - 1
	elif current_position < 0:
		return current_position + 1
	else:
		return current_position

lexicon = {' ': 'space', '\n': 'carriage return'}

def main():
	print(current_text)
	while True:
		c = raw_input("< direction?")
		navigate(c)

