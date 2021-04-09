def _default_transform(element, origin, *args, **kwargs):
	"""The default function that is used as operation of transform function

	By default, each element is returned without doing anything
	Args and kwargs will store any additional information

	Args:
		element: each element
		origin: origin container
	"""
	return element
