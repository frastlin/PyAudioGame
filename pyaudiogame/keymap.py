"""
Manages the usage of keymaps
usage:
keymap = KeyMap()
keymap.add(key=["f"], mods=["shift"], event="fligh)
"""

class KeyMap(object):
	def __init__(self, keymap=[]):
		self._keymap = []

		self.add(keymap)

	def _addSingle(self, mapping={}, key=[], mods=[], event=None, function=None, state=1):
		"""adds a key mapping to self._keymap. One can either pass in a dict of the keywords, or use the arguments to create the mapping. If one passes in both a dict and some keywords, note that the keywords will be over-ridden by the dict. either one or both of function or event need to be passed."""
		local_mapping = locals()
		# The next section keeps mapping from adding new key, which is what it would do if one used update.
		for k in local_mapping:
			local_mapping[k] = mapping.get(k, local_mapping[k])
		del local_mapping["mapping"] # so if it is empty in the next line, it doesn't trigger as false. One could also make it equal True, but this is more explicit
		if local_mapping["key"] and (local_mapping["function"] or local_mapping["event"]):
			# make sure key and mods are sets (not lists because we check if set == set in the getEvent function and list == list doesn't work if the items are out of order)
			local_mapping["key"] = set(list(local_mapping["key"]) if type(local_mapping["key"]) == list else [local_mapping["key"]])
			local_mapping["mods"] = set(list(local_mapping["mods"]) if type(local_mapping["mods"]) == list else [local_mapping["mods"]])
			self._keymap.append(local_mapping)
		else:
			missing_items = [k for k in local_mapping if not local_mapping[k] and k != "mods"]
			missing_items = ', '.join(missing_items)
			raise Exception("KeymapError: KeyMap.add was passed a mapping without a value for: %s" % missing_items)

	def add(self, mapping={}, key=[], mods=[], event=None, function=None, state=1):
		if type(mapping) == list:
			[self._addSingle(m, key, mods, event, function, state) for m in mapping]
		else:
			self._addSingle(mapping, key, mods, event, function, state)

	def getModsSets(self, mods):
		"""converts mods into a couple different sets and returns a list. That way users can use shift,and alt, rather than leftctrl and rightctrl."""
		nutral = set()
		with_alt = set()
		nutral_with_alt = set()
		for mod in mods:
			if "meta" in mod:
				alt = mod.replace("meta", "alt")
				with_alt.add(alt)
				nutral.add("meta")
				nutral_with_alt.add("alt")
			elif not mod in ['left', 'right'] and ('left' in mod or 'right' in mod):
				with_alt.add(mod)
				mod = mod.replace('left', '').replace('right', '').strip()
				nutral.add(mod)
				nutral_with_alt.add(mod)
			else:
				with_alt.add(mod)
				nutral.add(mod)
				nutral_with_alt.add(mod)
		return [with_alt, nutral, nutral_with_alt]

	def getEvent(self, key, mods=[], state=1):
		"""Gets the event that is triggered by the list of key and mods."""
		key = set(list(key) if type(key) == list else [key])
		key = {k.lower() for k in key}
		mods = set(list(mods if type(mods) == list else [mods]))
		mods = {str(k).lower() for k in mods}
		for mapping in self._keymap:
			if mapping['key'] == key and mapping['mods'] == mods and mapping['state'] == state:
				if mapping['function']:
					return mapping['function']()
				return mapping['event']
			elif mods:
				mod_sets = self.getModsSets(mods)
				for mod_set in mod_sets:
					if mapping['key'] == key and mapping['mods'] == mod_set and mapping['state'] == state:
						if mapping['function']:
							return mapping['function']()
						return mapping['event']


if __name__ == '__main__':
	keymap = KeyMap([
		{'key':['space'], 'event': "oranges", 'state':0},
		{'key':['f', 'a'], 'mods': ['ctrl','shift'], 'function': lambda: True},
	])
	print(keymap.getEvent(key='space', state=0))