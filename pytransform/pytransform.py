"""
Copyright 2021 cpyberry
https://github.com/cpyberry/pytransform

cpyberry
email: cpyberry222@gmail.com
github: https://github.com/cpyberry
"""


def _default_transform(element, origin, *args, **kwargs):
	"""The default function that is used as operation of transform function

	By default, each element is returned without doing anything
	Args and kwargs will store any additional information

	Args:
		element: each element
		origin: origin container
		*args: additional information
		**kwargs: additional information
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


def transform_dictionary(origin: dict, operation_key=_default_transform, operation_value=_default_transform) -> dict:
	"""Apply the specified function to each key and value of dictionary

	This function is called recursively, so it can also be applied to nested dictionary

	Args:
		origin (dict): origin container
		operation_key (function, optional): function you want to apply to each key. Defaults to _default_transform.
		operation_value (function, optional): function you want to apply to each value. Defaults to _default_transform.

	Returns:
		dict: dictionary to which the specified function is applied
	"""
	result = {}

	for key in origin:
		value = origin[key]

		if type(key) == dict:
			transformed_key = transform_dictionary(key, operation_key, operation_value)
		else:
			transformed_key = operation_key(key, origin, value)

		if type(value) == dict:
			transformed_value = transform_dictionary(value, operation_key, operation_value)
		else:
			transformed_value = operation_value(value, origin, key)

		result.update({transformed_key: transformed_value})

	return result
