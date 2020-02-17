def decorator(func):
	def wrapper():
		# do something
		value = func()
		# do something
		return value
	return wrapper
