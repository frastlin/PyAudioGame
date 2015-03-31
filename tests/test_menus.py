#tests the ui.menus module
from pyaudiogame.ui.menus import Menu


def run(item="default"):
	"""The function that is called when an item is chosen"""
	return item

function_menu = [("option1", run), ("option2", run, "cheese"), ("option3", run, "cake")]

def test