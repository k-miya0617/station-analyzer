# station-analyzer

## 目的
iTunesライブラリで用いられている iTunes Library.xml ファイルをパースする。  
stationアプリで用いるAPIが用いるstation/Tracksテーブルに直接格納できるように
iTunes Library.xmlファイルからJSONに変換する。

## 使い方
`$ python3 ConvertPListJson.py 'iTunes Library.xml' > output.json`