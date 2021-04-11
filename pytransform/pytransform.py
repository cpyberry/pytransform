def _default_transform(element, origin, *args, **kwargs):
	"""The default function that is used as operation of transform function

	By default, each element is returned without doing anything
	Args and kwargs will store any additional information

	Args:
		element: each element
		origin: origin container
	"""
	return element


def transform_list(origin: list, operation=_default_transform) -> list:
	"""Apply the specified function to each element of list

	This function is called recursively, so it can also be applied to nested elements

	Args:
		origin (list): origin container
		operation (function, optional): function you want to apply to each element. Defaults to _default_transform.

	Returns:
		list: list to which the specified function is applied
	"""
	result = []

	for element in origin:
		if type(element) == list:
			transformed_element = transform_list(element, operation)
		else:
			transformed_element = operation(element, origin)
		result.append(transformed_element)

	return result
