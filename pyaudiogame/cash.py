#Use this module to store variables and settings
try:
	import cPickle as _pickle
except:
	import pickle as _pickle

def save(file="save.sav", simulation=False):
	"""Call this function with the location of the file where you wish to save the info in this module."""
	g = globals()
	cash_dict = {}
	[cash_dict.update({i: g[i]}) for i in g if not i.startswith("_")]
	del(cash_dict['save'])
	del(cash_dict['load'])
	if not simulation:
		with open(file, 'wb') as f:
			_pickle.dump(cash_dict, f, protocol=_pickle.HIGHEST_PROTOCOL)
	return cash_dict

def load(file="save.sav", in_cash=True, overwrite=True):
	"""This will return the dict of all the variables in the cash module. If in_cash is True, then it will also populate the cash module with all the saved variables, and if overwrite, it will overwrite the current variables of the same name."""
	with open(file, "rb") as f:
		loaded_file = _pickle.load(f)
	if in_cash:
		if overwrite:
			[globals().update({i: loaded_file[i]}) for i in loaded_file]
		else:
			g = globals()
			[globals().update({i: loaded_file[i]}) for i in loaded_file if i not in g]
	return loaded_file

