class Cell:

	def __init__(self, value, changed):
		"""Initializes Cell object with given integer value"""
		self.value = value
		self.ctt = changed

	def __mul__(self, other):
		return Cell(self.value * other, True)

	def __rmul__(self, other):
		return self.__mul__(other, True)

	def __eq__(self, other):
		"""Returns True if two Cells hold the same value"""
		if isinstance(self, other.__class__):
			if self.__dict__ == other.__dict__ and self.ctt == False and other.ctt == False:
				return True

	def __str__(self):
		"""Returns the value held by the Cell as a string"""
		return str(self.value)

	def __repr__(self):
		return str(self)
