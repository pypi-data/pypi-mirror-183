# ffeature

下の方に日本語の説明があります

## Overview
- Tools to easily generate features using ftable

## Example usage
```python
import ffeature

# Feature definition [ffeature]
@ffeature.add_feature("player_score")
def player_score_feature(rec, ftable_dic):
	one_player = ftable_dic["player_ft"].cfilter("name", rec["name"])
	if len(one_player.data) != 1: raise Exception("[error] player unique constraint error")
	return one_player.data[0]["player_score"]

# Feature definition [ffeature]
@ffeature.add_feature("field")
def field_feature(rec, ftable_dic):
	return rec["field"]

# List of tables used to create features
ftable_dic = {
	"game_ft": ftable.FTable([
		{"name": "taro", "game_difficulty": 1.2, "field": "A"},
		{"name": "yusuke", "game_difficulty": 1.5, "field": "A"},
		{"name": "yusuke", "game_difficulty": 1.3, "field": "B"},
		{"name": "taro", "game_difficulty": 1.3, "field": "B"},
		{"name": "taro", "game_difficulty": 1.0, "field": None},
	]),
	"player_ft": ftable.FTable([
		{"name": "taro", "player_score": 120},
		{"name": "yusuke", "player_score": 150},
	])
}

# Create a feature table for the entire dataset (created according to the add_feature decorator) [ffeature]
feature_ft = ffeature.gen_feature_table(
	ftable_dic = ftable_dic,	# List of tables used to create features
	rec_table = ftable_dic["game_ft"],	# Table representing the records unit of the output ftable
	sorted_keys = []	# Specification of ftable's sorted_keys
)
print(feature_ft)

# Process missing values [ffeature]
feature_ft = ffeature.handle_missing(
	feature_ft,
	mode = "delete",	# delete: Skip rows with any missing values
	missing_values = [None]	# Values to be treated as missing values
)
print(feature_ft)

# Split data
rec_filter = lambda rec: (rec["field"] == "A")
partial_ft = ffeature.data_filter(feature_ft, rec_filter)	# Extract records from ft that meet the condition [ffeature]
print(partial_ft)
```

## 概要
- ftableを使って特徴量を簡単に生成できるツール

## 使用例
```python
import ffeature

# 特徴量定義 [ffeature]
@ffeature.add_feature("player_score")
def player_score_feature(rec, ftable_dic):
	one_player = ftable_dic["player_ft"].cfilter("name", rec["name"])
	if len(one_player.data) != 1: raise Exception("[error] player unique constraint error")
	return one_player.data[0]["player_score"]

# 特徴量定義 [ffeature]
@ffeature.add_feature("field")
def field_feature(rec, ftable_dic):
	return rec["field"]

# 特徴量作成に利用するテーブルの一覧
ftable_dic = {
	"game_ft": ftable.FTable([
		{"name": "taro", "game_difficulty": 1.2, "field": "A"},
		{"name": "yusuke", "game_difficulty": 1.5, "field": "A"},
		{"name": "yusuke", "game_difficulty": 1.3, "field": "B"},
		{"name": "taro", "game_difficulty": 1.3, "field": "B"},
		{"name": "taro", "game_difficulty": 1.0, "field": None},
	]),
	"player_ft": ftable.FTable([
		{"name": "taro", "player_score": 120},
		{"name": "yusuke", "player_score": 150},
	])
}

# 全量に対する特徴量テーブルを作成 (add_feature デコレータに従って作成) [ffeature]
feature_ft = ffeature.gen_feature_table(
	ftable_dic = ftable_dic,	# 特徴量作成に利用するテーブルの一覧
	rec_table = ftable_dic["game_ft"],	# 作成するデータのレコード単位を規定するテーブル
	sorted_keys = []	# ftableのsorted_keysの指定
)
print(feature_ft)

# 欠損値を処理 [ffeature]
feature_ft = ffeature.handle_missing(
	feature_ft,
	mode = "delete",	# delete: 1つでも欠損値がある行をスキップする
	missing_values = [None]	# 欠損値として扱う値
)
print(feature_ft)

# データの分割
rec_filter = lambda rec: (rec["field"] == "A")
partial_ft = ffeature.data_filter(feature_ft, rec_filter)	# ftから条件を満たすレコードを抽出 [ffeature]
print(partial_ft)
```
