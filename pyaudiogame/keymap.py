"""
Manages the usage of keymaps
usage:
keymap = KeyMap()
keymap.add(keys=["f"], mods=["shift"], event="fligh)
"""

class KeyMap(object):
	def __init__(self, keymap=[]):
		self._keymap = []

		for mapping in keymap:
			self.add(mapping)

	def add(self, mapping={}, keys=[], mods=[], event=None, function=None):
		"""adds a key mapping to self._keymap. One can either pass in a dict of the keywords, or use the arguments to create the mapping. If one passes in both a dict and some keywords, note that the keywords will be over-ridden by the dict. either one or both of function or event need to be passed."""
		local_mapping = locals()
		# The next section keeps mapping from adding new key, which is what it would do if one used update.
		for k in local_mapping:
			local_mapping[k] = mapping.get(k, local_mapping[k])
		del local_mapping["mapping"] # so if it is empty in the next line, it doesn't trigger as false. One could also make it equal True, but this is more explicit
		if local_mapping["keys"] and (local_mapping["function"] or local_mapping["event"]):
			# make sure key and mods are sets (not lists because we check if set == set in the getEvent function and list == list doesn't work if the items are out of order)
			local_mapping["keys"] = set(list(local_mapping["keys"]))
			local_mapping["mods"] = set(list(local_mapping["mods"]))
			self._keymap.append(local_mapping)
		else:
			missing_items = [k for k in local_mapping if not local_mapping[k] and k != "mods"]
			missing_items = ', '.join(missing_items)
			raise Exception("KeymapError: KeyMap.add was passed a mapping without a value for: %s" % missing_items)

	def getEvent(self, keys, mods=[]):
		"""Gets the event that is triggered by the list of key and mods."""
		keys = set(list(keys))
		mods = set(list(mods))
		for mapping in self._keymap:
			if mapping['keys'] == keys and mapping['mods'] == mods:
				if mapping['function']:
					return mapping['function']()
				return mapping['event']
