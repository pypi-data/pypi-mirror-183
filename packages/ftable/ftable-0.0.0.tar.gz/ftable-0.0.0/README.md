# ftable

下の方に日本語の説明があります

## Overview
- A table that has had its filter/search function optimized for speed.
- A system that can quickly and easily perform complex feature generation for machine learning using simple descriptions
- discription is under construction

## Example usage
```python
under construction
```

## 概要
- フィルタ・検索機能が高速化されたテーブル
- 機械学習の複雑な特徴量生成を簡単な記述で高速に実行できる
- 説明は執筆中です

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
	lambda date: (date < "20450110"))
print(idx)
if idx == -1: idx = None
# 元データの直接参照
print(filtered_ft.data[idx])
```

## 注意
- 一度FTableとして初期化したデータは改変しないでください。 (検索の動作が保証されなくなります)
- sorted_keysの指定は現行バージョンでは1つのみです
- bfindは最初からFalseの場合は-1を返すので注意 (pythonの-1インデックス参照は最終要素になることに注意して前後の実装を行ってください)
