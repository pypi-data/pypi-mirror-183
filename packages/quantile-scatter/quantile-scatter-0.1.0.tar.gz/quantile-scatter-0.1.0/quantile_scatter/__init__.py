
# 分位点散布図 [quantile_scatter]
# 【動作確認 / 使用例】

import sys
import numpy as np
from sout import sout

# グループに分割
def grouping(arg_ls, group_n):
	ret_ls = [[] for _ in range(group_n)]
	for i, e in enumerate(arg_ls):
		th = i / len(arg_ls)	# 無次元化インデックス
		group_idx = int(th * group_n)
		# 格納
		ret_ls[group_idx].append(e)
	return ret_ls

# matplotlibで可視化 [quantile_scatter]
def visualize(arg_data):
	from matplotlib import pyplot as plt
	for one_data in arg_data:
		# 描画
		plt.plot(
			one_data["x"], one_data["y"],
			label = one_data["label"],
			marker = ".", markersize = 8
		)
	# 描画処理
	plt.legend()
	plt.show()

# 1ラベル分のグラフデータ生成
def one_label_sum(
	grouped_zip_ls,	# グループ化されたデータ
	sum_func,	# データ集計関数
	label	# 凡例に掲載するデータ説明
):
	# xの取り出し
	show_x_ls = [np.mean([x for x, y in group])
		for group in grouped_zip_ls]
	# yの計算 (sum_funcでgroup内y値を集計)
	show_y_ls = [
		sum_func([y for x, y in group])
		for group in grouped_zip_ls
	]
	# データをパッケージングして返却
	return {
		"label": label,
		"x": show_x_ls,
		"y": show_y_ls,
	}

# 分位点散布図の描画 [quantile_scatter]
def plot(
	x,	# 横軸数値リスト
	y,	# 縦軸数値リスト
	group_n = 20,	# 分割グループ数
	ile_ls = [0.25, 0.5, 0.75],	# どこの分位点を出すか
	mean = False,	# 平均も出力する
	show = True,	# False指定でグラフを出力しない (データ集計のみ)
):
	# x昇順に整序
	zip_ls = list(zip(x, y))
	zip_ls.sort(key = lambda e: e[0])
	# グループに分割
	grouped_zip_ls = grouping(zip_ls, group_n)
	# 返却するデータ
	ret_data = []
	# 各分位点を集計
	for ile in ile_ls:
		# 今回のデータ集計方法
		sum_func = lambda arg_y_ls: np.quantile(arg_y_ls, ile)
		# 1ラベル分のグラフデータ生成
		ret_data.append(one_label_sum(
			grouped_zip_ls,	# グループ化されたデータ
			sum_func,	# データ集計関数
			label = str(ile)	# 凡例に掲載するデータ説明
		))
	# 平均を集計
	if mean is True:
		# 1ラベル分のグラフデータ生成
		ret_data.append(one_label_sum(
			grouped_zip_ls,	# グループ化されたデータ
			sum_func = lambda arg_y_ls: np.mean(arg_y_ls),	# データ集計関数
			label = "mean"	# 凡例に掲載するデータ説明
		))
	# matplotlibで可視化 [quantile_scatter]
	if show is True:
		visualize(ret_data)
	return ret_data
