# ETLポートフォリオ

## 概要

本プロジェクトは、OpenWeather APIから天気データを取得し、
Pythonで前処理を行ったうえでMySQLに保存するETLパイプラインです。
APIデータ取得からDB格納までの一連の流れを通して、
データエンジニアリングの基礎を学ぶことを目的としています。

※MySQLの認証情報・APIキーは環境変数で管理しています。

## 使用技術

- Python
- MySQL
- OpenWeather API
- pandas
- requests

## ETL構成

本ETLは以下の流れで処理を行います。

1. Extract  
   OpenWeather APIから都市ごとの天気データを取得

2. Transform  
   JSONデータから必要な項目を抽出し、
   日時変換・型整形を実施

3. Load  
   整形済みデータをMySQLのweatherテーブルに保存
   （city + date_time の重複は更新）

## 処理イメージ

OpenWeather API
      ↓
   Python（ETL）
      ↓
     MySQL
