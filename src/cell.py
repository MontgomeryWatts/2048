class Cell:

	def __init__(self, value, changed=False):
		"""Initializes Cell object with given integer value"""
		self.value = value
		self.changed = changed

	def __mul__(self, other):
		return Cell(self.value * other, True)

	def __rmul__(self, other):
		return self.__mul__(other)

	def __eq__(self, other):
		"""Returns True if two Cells hold the same value"""
		if isinstance(self, other.__class__):
			if self.value == other.value and self.changed is False and other.changed is False:
				return True

	def __str__(self):
		"""Returns the value held by the Cell as a string"""
		return str(self.value)

	def __repr__(self):
		return str(self)
