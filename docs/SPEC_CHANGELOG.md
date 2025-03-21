# SPEC_CHANGELOG.md

## 変更履歴

### Ver.2025-03-20-01
**初版作成**
- 仕様の全体構成を `SPECIFICATIONS.md` に記載
- 各モジュールの機能要件を整理
- AI-DB のデータ構造を明確化
- AWS 環境でのデプロイ方法を記述

### Ver.2025-03-21-01
**UIデザイン仕様の更新**
- サイドメニューの開閉アニメーションを追加
- メインエリアのコンテンツ配置を調整
- ボタンのデザインを統一
- フォント & カラーの統一
- スマホレスポンシブ対応を考慮
- 「情報収集」ボタンのレイアウト修正

### Ver.2025-03-22-01
**フォルダ構成の整理**
- `AI_Projects/` 以下に `GPT_Qualifications/` と `AI_NoCode_Builder/` を追加
- `backend/` と `frontend/` のディレクトリ構成を整理
- `shared/` フォルダを作成し、共通ライブラリを格納

### Ver.2025-03-23-01
**AWS デプロイ手順の追加**
- `app.py` の FastAPI / Flask バージョンを明確化
- DynamoDB Local の環境設定を記録
- S3 や API Gateway との連携を考慮した設計に変更
- `Dockerfile` を整理し、ECS でのデプロイも視野に

### Ver.2025-03-24-01
**データ管理 & セキュリティ強化**
- `history.json` のデータ保存形式を最適化
- ユーザーごとのアクセス制限機能を追加
- IAM ロール設定の見直し
- セキュリティグループのルールを整理（SSH制限など）

---

⚠ **仕様変更の際のルール**
- **変更が発生したら必ず `Ver.YYYY-MM-DD-XX` 形式で記録**
- **過去バージョンとの差分を明確に記述**
- **影響範囲を記載し、どのモジュールが影響を受けるかを明確化**



### Ver.2025-03-25-01
**仮想環境・UI構成の整備とNginxの導入**
- `requirements.txt` を Git に追加し運用ルールを整備
- `.gitignore` に venv とキャッシュを追加
- EC2 環境で nginx を起動し、静的ファイルを `/frontend/` に配置
- ChatGPT風 UI にて `/get-ai-models` API を連携
