"""Simple example showing how to get keyboard events.
print(event.ev_type, event.code, event.state)
"""
import sys

from inputs import get_key

pressed = set()

def main():
	"""Just print out some event infomation when keys are pressed."""
	while 1:
		events = get_key()
		for event in events:
			code = event.code.split("_")[-1].lower()
			if event.state == 1:
				pressed.add(code)
			elif code in pressed:
				pressed.remove(code)

			if code == "space" and "leftctrl" in pressed:
				print("You pressed ctrl+space!")
			

 
if __name__ == "__main__":
	main()