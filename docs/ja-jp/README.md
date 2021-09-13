# pytransform

list型やdict型のオブジェクトの各要素に任意の関数を適応するライブラリ

変換する過程を定義した関数（変換前の各要素を引数にとり変換後の各要素を返す関数）は再帰的に呼び出されるため、入れ子になったリストや辞書にも対応しています。

## 必要環境

* python 3.5, 3.6, 3.7, 3.8, 3.9

## インストール方法

```shell
pip install cpyberry-pytransform
```

## 使い方

リストの各要素を2倍したい時、以下のように書きます。

```python
import pytransform


def operation_double(element: int, origin: list) -> int:
	# 第一引数には元のリストの各要素が格納されています。
	# 第二引数には元のリストが格納されています。
	return element * 2


pytransform.transform_list([1, 2, 3], operation_double)
# return [2, 4, 6]

pytransform.transform_list(
	origin=[1, 2, 3],
	operation=operation_double
)
# return [2, 4, 6]
```

辞書の各keyの最後に"_neko"、各valueの最後に"_inu"を挿入したい時、以下のように書きます。

```python
def operation_key(key: str, origin: dict, value: str):
	# 第一引数には元の辞書の各keyが格納されています。
	# 第二引数には元の辞書が格納されています。
	# 第三引数には元の辞書の各keyに対応したvalueが格納されています。
	return key + "_neko"


def operation_value(value: str, origin: dict, key: str):
	# 第一引数には元の辞書の各keyに対応したvalueが格納されています。
	# 第二引数には元の辞書が格納されています。
	# 第三引数には元の辞書の各valueが格納されています。
	return value + "_inu"


pytransform.transform_dictionary(
	origin={"meow": "woof"},
	operation_key=operation_key,
	operation_value=operation_value
)
# return {"meow_neko", "woof_inu"}
```

上記の関数は再帰的に呼び出されるため、入れ子になったリストや辞書にもこれらの関数は対応しています。

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

## 創始者

* [cpyberry](https://github.com/cpyberry)

	email: cpyberry222@gmail.com
