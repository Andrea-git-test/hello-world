def decorator(func):
	def wrapper():
		# do something
		value = func()
		# do something
		return value
	return wrapper

# just a test comment
# another comment