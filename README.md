# pytransform

Easily achieve functional conversion of container elements.

You can apply recursively specified functions to various containers.

## Usage

If you want to multiply each element of the list by 2, you can write:

```python
import pytransform


def operation_double(element: int, origin: list) -> int:
	# Each element is stored in element argument
	# [1, 2, 3] is stored in origin argument in this case
	return element * 2


pytransform.transform_list([1, 2, 3], operation_double)
# return [2, 4, 6]

pytransform.transform_list(
	origin=[1, 2, 3],
	operation=operation_double
)
# return [2, 4, 6]
```

If you want to insert "_neko" at the end of each key in the dictionary and "_inu" at the end of each value, you can write:

```python
def operation_key(key: str, origin: dict, value: str):
	# Each key is stored in key argument
	# {"meow": "woof"} is stored in origin argument in this case
	# Each value is stored in value argument
	return key + "_neko"


def operation_value(value: str, origin: dict, key: str):
	# Each value is stored in value argument
	# {"meow": "woof"} is stored in origin argument in this case
	# Each key is stored in key argument
	return value + "_inu"


pytransform.transform_dictionary(
	origin={"meow": "woof"},
	operation_key=operation_key,
	operation_value=operation_value
)
# return {"meow_neko", "woof_inu"}
```

Nested list and dictionary can also recursively apply specified functions.

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
