import plistlib
import json
from datetime import date, datetime
import sys

# 読み込むプロパティリストファイルのパス
args = sys.argv
PLIST_PATH = args[1]

# ディクショナリを作成
plist = {}

# plistを読み込む
with open(PLIST_PATH, 'rb') as fp:
    plist = plistlib.load(fp)

# date, datetimeの変換関数
def json_serial(obj):
    # 日付型の場合には、文字列に変換する
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    # 上記以外はサポート対象外
    raise TypeError ("Type %s not serializable" % type(obj))

# Tracksのデータのみ取得
tracks = plist.get('Tracks')

# 連想配列のキー名を変更する
ary = {'Tracks': []}

for trackID in tracks.keys():
    trackObj = tracks.get(trackID)

    # デフォルト値の設定
    trackObj.setdefault('Track ID')
    trackObj.setdefault('Size')
    trackObj.setdefault('Total Time')
    trackObj.setdefault('Disc Number')
    trackObj.setdefault('Disc Count')
    trackObj.setdefault('Track Number')
    trackObj.setdefault('Track Count')
    trackObj.setdefault('Date Added')
    trackObj.setdefault('Date Modified')
    trackObj.setdefault('Artwork Count')
    trackObj.setdefault('Album Artist')
    trackObj.setdefault('Play Count')

    # キー名の変更
    trackObj['TrackID'] = trackObj.pop('Track ID')
    trackObj['SizeByte'] = trackObj.pop('Size')
    trackObj['TotalTimeMs'] = trackObj.pop('Total Time')
    trackObj['DiscNumber'] = trackObj.pop('Disc Number')
    trackObj['DiscCount'] = trackObj.pop('Disc Count')
    trackObj['TrackNumber'] = trackObj.pop('Track Number')
    trackObj['TrackCount'] = trackObj.pop('Track Count')
    trackObj['DateAdded'] = trackObj.pop('Date Added')
    trackObj['DateModified'] = trackObj.pop('Date Modified')
    trackObj['ArtworkCount'] = trackObj.pop('Artwork Count')
    trackObj['AlbumArtist'] = trackObj.pop('Album Artist')
    trackObj['PlayCount'] = trackObj.pop('Play Count')

    # 配列への追加
    ary.get('Tracks').append(trackObj)

# TracksをJSONに変換する
jsonStr = json.dumps(ary, ensure_ascii=False, default=json_serial, indent=2)

# JSONを出力する
print(jsonStr)

