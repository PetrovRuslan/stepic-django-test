class hotels:
	"""docstring for hotels"""
	def __init__(self, name, stars, price):
		super(hotels, self).__init__()
		self.name = name
		self.stars = stars
		self.price = price

	def showAll(self):
		print(self.name, self.stars, self.price)

	def showName(self):
		print(self.name)

	def showStars(self):
		print(self.stars)

	def showPrice(self):
		print(self.price)

	# def __repr__(self):
		# return '(name={}, stars={}, price={})'.format(self.name, self.stars, self.price)
		