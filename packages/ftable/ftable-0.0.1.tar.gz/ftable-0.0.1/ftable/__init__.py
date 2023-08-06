
# 高速テーブル [ftable]

import sys
from sout import sout, souts
from tqdm import tqdm

# cfilter_cacheの生成
def gen_cfilter_cache(ft, key):
	print("[ftable] generating cache (key = %s)..."%key)
	# 情報を分割格納
	prepare_dic = {}
	for rec in tqdm(ft.data):
		value = rec[key]
		if value not in prepare_dic: prepare_dic[value] = []
		prepare_dic[value].append(rec)
	# cacheの値をFTabel型として格納
	one_cache = {
		value: FTable(
			prepare_dic[value],
			ft.sorted_keys,
			_already_sorted = True
		)
		for value in tqdm(prepare_dic)
	}
	return one_cache

# 高速テーブル型 [ftable]
class FTable:
	# 初期化処理
	def __init__(self,
		raw_data,	# 原型となるテーブルデータ
		sorted_keys = [],	# 整序軸の指定
		_already_sorted = False	# (内部機能) すでにソートされている場合
	):
		# 整序軸の処理
		self.sorted_keys = sorted_keys
		if len(self.sorted_keys) == 0:
			pass
		elif len(self.sorted_keys) == 1:
			if _already_sorted is False:
				# 外側のリストのみ新たに生成される (シャローコピーに対応)
				raw_data = sorted(raw_data,
					key = lambda rec: rec[self.sorted_keys[0]])
		else:
			# 未実装の機能
			raise Exception("[ftable error] The current version does not allow more than two sorted_keys to be specified.")
		# データ登録
		self.data = raw_data	# データ登録
		# cfilterのキャッシュ
		self.cfilter_cache = {}
	# cacheされたフィルタ機能 [ftable]
	def cfilter(self, key, value):
		if key not in self.cfilter_cache:
			# cfilter_cacheの生成
			self.cfilter_cache[key] = gen_cfilter_cache(self, key)
		# filterした結果を返す
		filtered_ft = self.cfilter_cache[key][value]
		return filtered_ft
	# 二分探索 (条件を満たす最後のインデックスを見つける; 最初からFalseの場合は-1を返す) [ftable]
	def bfind(self, key, cond):
		# keyの適格性判断
		if key not in self.sorted_keys: raise Exception("[ftable error] The bfind function can only compute on keys specified in sorted_keys.")
		# 二分探索
		left = 0
		right = len(self.data) - 1
		while left <= right:
			mid = (left + right) // 2
			if cond(self.data[mid][key]) is True:
				left = mid + 1
			else:
				right = mid - 1
		idx = right
		if idx < 0: return -1
		return idx
	# 文字列化
	def __str__(self):
		return "<ftable %s>"%souts(self.data, 10)
	# 文字列化その2
	def __repr__(self):
		return str(self)
