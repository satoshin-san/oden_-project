import pandas as pd
import matplotlib.pyplot as plt
from japanmap import picture, pref_names
import matplotlib
from matplotlib.colors import Normalize, to_hex
import matplotlib.cm as cm

# 日本語フォント設定（例：メイリオ）
matplotlib.rcParams['font.family'] = 'Meiryo'

# データ読み込み
file_path = 'oden_data.csv'  # データファイルのパス
data = pd.read_csv(file_path)

# 都道府県ごとの集計
top_items_by_prefecture = (
    data.groupby(['出身都道府県', '好きなおでんの具'])
    .size()
    .reset_index(name='件数')
)

# 「にんじん」の件数だけを抽出
carrot_data = top_items_by_prefecture[top_items_by_prefecture['好きなおでんの具'] == 'にんじん']

# pref_namesリストから都道府県名とコードの辞書を作成
prefecture_codes = {pref: index for index, pref in enumerate(pref_names) if index != 0}

# カラーマップの設定
norm = Normalize(vmin=0, vmax=carrot_data['件数'].max())
cmap = cm.Oranges  # オレンジ系のカラーマップ

# 都道府県名をコードにマッピング
carrot_map_data = {
    prefecture_codes[pref]: to_hex(cmap(norm(count)))  # 色を16進数コードに変換
    for pref, count in zip(carrot_data['出身都道府県'], carrot_data['件数'])
    if pref in prefecture_codes
}

# 地図描画（にんじん分布図）
fig, ax = plt.subplots(figsize=(12, 8))
ax.imshow(picture(carrot_map_data))
ax.axis('off')
ax.set_title('にんじんが好きな都道府県の分布図（グラデーション）', fontsize=16)

# カラーバーを追加
sm = cm.ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])
fig.colorbar(sm, ax=ax, label='にんじんの件数', orientation='vertical')

plt.show()
