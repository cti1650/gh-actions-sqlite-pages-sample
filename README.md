# gh-actions-sqlite-pages-sample

GitHub Actions (cron) で SQLite を1日1回更新し、SQLiteから生成した JSON を GitHub Pages で配信するサンプル。

## 動作
- Actions: `daily-update`
  - SQLite: `data/app.db` を更新
  - JSON: `frontend/data.json` を生成
  - Pages: `frontend/` をデプロイ

## セットアップ
1. このリポジトリを public で作成
2. Settings → Pages → Build and deployment
   - Source: GitHub Actions を選択
3. Actions → `daily-update` を `Run workflow` で手動実行（初回）
4. Pages URL にアクセスすると `data.json` の内容が表示される

