"""Simple example showing how to get keyboard events.
print(event.ev_type, event.code, event.state)
"""
import sys

from inputs import get_key


def main():
	"""Just print out some event infomation when keys are pressed."""
	while 1:
		events = get_key()
		for event in events:
			if event.state == 1:
				if event.code == "KEY_SPACE":
					print("Hello!")
					sys.exit()
				elif event.code == "KEY_Q":
					print("This is q")

 
if __name__ == "__main__":
	main()