# AI_DB_UI 仕様リファレンス
## 最終更新: 2025-03-20
---

## 📌 プロジェクト概要
- **プロジェクト名:** AI Database Management System (AI_DB_UI)
- **目的:** AIモデルの情報をDynamoDBで管理し、Web UIで閲覧・更新する
- **開発環境:** AWS EC2, DynamoDB Local, FastAPI, React
- **フロントエンド:** Next.js + Tailwind CSS
- **バックエンド:** FastAPI (Python) + DynamoDB
- **ホスティング:** AWS EC2

---

## 📌 バックエンド仕様
### 🔹 言語・フレームワーク
- **Python 3.10**
- **FastAPI**（APIフレームワーク）
- **DynamoDB (AWS / Local)**（データ管理）
- **Boto3**（AWS SDK）

### 🔹 API エンドポイント一覧
| **エンドポイント** | **メソッド** | **説明** |
|-----------------|----------|-----------------------------|
| `/get-ai-models` | `GET` | AIモデルの一覧を取得 |
| `/get-ai-model/{model_name}` | `GET` | 指定したAIモデルの詳細情報を取得 |
| `/update-ai-model` | `POST` | AIモデルの情報を更新 |

### 🔹 DynamoDB テーブル構成
- **テーブル名:** `AI_Models_DB`
- **パーティションキー:** `AI_Name (String)`
- **項目一覧:**
  - `AI_Name (String)` → モデル名
  - `Version (String)` → バージョン
  - `Developer (String)` → 開発元
  - `Release_Date (String)` → リリース日
  - `Max_Input_Tokens (Number)` → 最大入力トークン数
  - `Max_Output_Tokens (Number)` → 最大出力トークン数
  - `Strengths (List<String>)` → 得意なタスク
  - `Weaknesses (List<String>)` → 不得意なタスク
  - `API_Endpoint (String)` → APIエンドポイント
  - `Pricing (String)` → 料金体系
  - `Response_Time (String)` → レスポンスタイム
  - `Usage_Limits (String)` → 利用制限
  - `Customization (String)` → カスタマイズ性
  - `Supported_Languages (List<String>)` → 対応言語
  - `Comparison (String)` → 競合モデルとの比較
  - `Notes (String)` → その他の特記事項

---

## 📌 フロントエンド仕様
### 🔹 技術スタック
- **Next.js 14**（フレームワーク）
- **React (useState, useEffect, SWR)**（状態管理・API通信）
- **Tailwind CSS**（スタイリング）

### 🔹 主要コンポーネント
| **コンポーネント** | **説明** |
|----------------|------------------------------|
| `Sidebar.tsx` | AIモデル一覧を表示するサイドバー |
| `MainContent.tsx` | 選択したモデルの詳細情報を表示 |
| `UpdateForm.tsx` | AIモデル情報を編集するフォーム |
| `Header.tsx` | ナビゲーションバー |

### 🔹 UI 要件
- サイドメニューの **開閉アニメーション** を追加
- メインエリアの **コンテンツ配置を調整**
- ボタンのデザインを **統一・改善**
- フォント & カラーを統一
- **スマホレスポンシブ対応**（横スクロール回避 & メニュー操作）
- 「情報収集」ボタンのレイアウトを修正

---

## 📌 AWS 環境設定
### 🔹 使用サービス
- **EC2 (Amazon Linux 2023) - アプリサーバー**
- **DynamoDB Local**（開発環境用）
- **DynamoDB (AWS)**（本番環境用）

### 🔹 セキュリティ設定
- **SSH接続:** `Port 22`（特定IPのみ許可）
- **アプリ通信:** `Port 5000`（外部アクセス許可）
- **DynamoDB Local:** `Port 8000`（ローカル環境専用）
- **IAM ロール:** `DynamoDBFullAccess` を付与

---

## 📌 変更履歴
✅ `2025-03-18` - UIデザイン仕様を更新
✅ `2025-03-19` - APIレスポンスフォーマットを修正
✅ `2025-03-20` - UIのスマホ対応を強化

---

✅ **この仕様を基準に、開発・デザインを進める！**

