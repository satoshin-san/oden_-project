import pandas as pd
import matplotlib.pyplot as plt
from japanmap import picture, pref_names
import random


# 日本語フォント設定（例：メイリオ）
plt.rcParams['font.family'] = 'Meiryo'

# データ読み込み
file_path = r'C:\python_study\oden_kaigi\oden_data.csv'
data = pd.read_csv(file_path)

# 都道府県ごとの集計
top_items_by_prefecture = (
    data.groupby(['出身都道府県', '好きなおでんの具'])
    .size()
    .reset_index(name='件数')
    .sort_values(['出身都道府県', '件数'], ascending=[True, False])
)

# 各都道府県で件数が最も多いおでんの具を抽出
top_ranking = top_items_by_prefecture.groupby('出身都道府県').first().reset_index()

# おでんの具材の色分け
unique_items = top_ranking['好きなおでんの具'].unique()
random.seed(42)
colors = {item: f"#{''.join([random.choice('0123456789ABCDEF') for _ in range(6)])}" for item in unique_items}
top_ranking['色'] = top_ranking['好きなおでんの具'].map(colors)

# pref_namesリストから都道府県名とコードの辞書を作成
prefecture_codes = {pref: index for index, pref in enumerate(pref_names) if index != 0}

# 都道府県名をコードにマッピング
data_for_map_color = {
    prefecture_codes[pref]: colors[val]
    for pref, val in zip(top_ranking['出身都道府県'], top_ranking['好きなおでんの具'])
    if pref in prefecture_codes
}

# 地図描画
plt.figure(figsize=(12, 8))
plt.imshow(picture(data_for_map_color))
plt.axis('off')
plt.title('都道府県ごとのおでんランキング1位（色分け）', fontsize=16)

# 凡例作成
handles = [plt.Line2D([0], [0], color=color, lw=4, label=item) for item, color in colors.items()]
plt.legend(handles=handles, bbox_to_anchor=(1.05, 1), loc='upper left', title='おでんの具材')

plt.show()
