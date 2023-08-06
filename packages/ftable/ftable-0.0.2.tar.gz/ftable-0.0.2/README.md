# ftable

下の方に日本語の説明があります

## Overview
- A table that has had its filter/search function optimized for speed.
- A system that can quickly and easily perform complex feature generation for machine learning using simple descriptions

## Example usage
```python
import ftable

raw_data = [
	{"date": "20450105", "name": "taro", "score": 22.5},
	{"date": "20450206", "name": "hanako", "score": 12.6},
	{"date": "20450206", "name": "taro", "score": 3.5},
]

# Fast table type [ftable]
ft = ftable.FTable(
	raw_data,	# The raw table data
	sorted_keys = ["date"]	# Specifying the sorting axis
)

# Cached filter function [ftable]
filtered_ft = ft.cfilter("name", "taro")
# Display filter result
print(filtered_ft)

# Binary search (find the last index that meets the condition; if False from the beginning, return -1) [ftable]
idx = filtered_ft.bfind("date",
	cond = lambda date: (date < "20450110"))

# Direct reference to original data
print(idx)
if idx == -1: idx = None
print(filtered_ft.data[idx])

# Select a random record (with fixed seed) [ftable]
print(ft.rget(2))
```

## Note
- Please do not modify the data once it has been initialized as an FTable. (This may cause search functionality to be unreliable)
- In the current version, only 1 or 0 sorted_keys can be specified
- Note that bfind returns -1 if the result of cond() is False for the first element (be aware of this when implementing previous and next, taking into account that Python's -1 index reference refers to the last element)


## 概要
- フィルタ・検索機能が高速化されたテーブル
- 機械学習の複雑な特徴量生成を簡単な記述で高速に実行できる

## 使用例
```python
import ftable

raw_data = [
	{"date": "20450105", "name": "taro", "score": 22.5},
	{"date": "20450206", "name": "hanako", "score": 12.6},
	{"date": "20450206", "name": "taro", "score": 3.5},
]

# 高速テーブル型 [ftable]
ft = ftable.FTable(
	raw_data,	# 原型となるテーブルデータ
	sorted_keys = ["date"]	# 整序軸の指定
)

# cacheされたフィルタ機能 [ftable]
filtered_ft = ft.cfilter("name", "taro")
# フィルタ結果の表示
print(filtered_ft)

# 二分探索 (条件を満たす最後のインデックスを見つける; 最初からFalseの場合は-1を返す) [ftable]
idx = filtered_ft.bfind("date",
	cond = lambda date: (date < "20450110"))
print(idx)

# 元データの直接参照
if idx == -1: idx = None
print(filtered_ft.data[idx])

# ランダムなレコードを選定 (seed固定) [ftable]
print(ft.rget(2))
```

## 注意
- 一度FTableとして初期化したデータは改変しないでください。 (検索の動作が保証されなくなります)
- sorted_keysの指定は現行バージョンでは1または0個のみです
- bfindは、先頭要素からcond()の結果がFalseの場合は-1を返すので注意 (pythonの-1インデックス参照は最終要素を指定することに注意して前後の実装を行ってください)
