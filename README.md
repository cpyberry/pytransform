# pytransform

A library that applies arbitrary functions to each element of list type and dict type objects

Functions that defines the conversion process, which takes each element before conversion as an argument and returns each element after conversion, is called recursively, so it also supports nested list and dictionary.

## Requirements

* python 3.5, 3.6, 3.7, 3.8, 3.9

## Installation

```shell
pip install cpyberry-pytransform
```

## Usage

When you want to multiply each element of the list by 2, you can write:

```python
import pytransform


def operation_double(element: int, origin: list) -> int:
	# The first argument contains each element of the original list.
	# The original list is stored in the second argument.
	return element * 2


pytransform.transform_list([1, 2, 3], operation_double)
# return [2, 4, 6]

pytransform.transform_list(
	origin=[1, 2, 3],
	operation=operation_double
)
# return [2, 4, 6]
```

When you want to insert "_neko" at the end of each key in the dictionary and "_inu" at the end of each value, you can write:

```python
def operation_key(key: str, origin: dict, value: str):
	# The first argument contains each key of the original dictionary.
	# The original dictionary is stored in the second argument.
	# The third argument contains the value corresponding to each key in the original dictionary.
	return key + "_neko"


def operation_value(value: str, origin: dict, key: str):
	# The first argument contains each key of the original dictionary.
	# The original dictionary is stored in the second argument.
	# The third argument contains the value corresponding to each key in the original dictionary.
	return value + "_inu"


pytransform.transform_dictionary(
	origin={"meow": "woof"},
	operation_key=operation_key,
	operation_value=operation_value
)
# return {"meow_neko", "woof_inu"}
```

The above functions are called recursively, so they also support nested list and dictionary.

```python
pytransform.transform_list([1, 2, [3, 4, 5]], operation_double)
# return [2, 4, [6, 8, 10]]

pytransform.transform_dictionary(
	origin={"meow": {"pows": "woof"}},
	operation_key=operation_key,
	operation_value=operation_value
)
# return {"meow_neko": {"pows_neko": "woof_inu"}}
```

## Founder

* [cpyberry](https://github.com/cpyberry)

	email: cpyberry222@gmail.com
