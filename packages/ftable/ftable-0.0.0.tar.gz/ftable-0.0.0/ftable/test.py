
# 高速テーブル [ftable]
# 【動作確認 / 使用例】

import sys
from sout import sout
from ezpip import load_develop
# 深層分位点回帰 [deep_q_reg]
ftable = load_develop("ftable", "../", develop_flag = True)

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
sout(filtered_ft.data[idx])
