import pandas as pd

# データを読み込む
oden_data = pd.read_csv(r'C:\python_study\oden_kaigi\oden_data.csv')#ここを対象データのパスに変更

# 好きなおでんの具を集計
ranking = oden_data['好きなおでんの具'].value_counts()

# 結果をCSVに保存
ranking.to_csv('oden_ranking.csv', index_label='具材', header=['票数'])

print("ランキング結果を 'oden_ranking.csv' に保存しました。")
