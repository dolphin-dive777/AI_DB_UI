# AI_DB_UI セットアップ手順

## 💻 開発環境のセットアップ

### 1️⃣ 必要なソフトウェアをインストール
- [Python 3.10+](https://www.python.org/downloads/)
- [Node.js 18+](https://nodejs.org/ja/download/)
- [AWS CLI](https://aws.amazon.com/cli/)
- [Git](https://git-scm.com/downloads)

### 2️⃣ リポジトリをクローン
```bash
git clone https://github.com/dolphin-dive777/AI_DB_UI.git
cd AI_DB_UI
```

### 3️⃣ Python 環境のセットアップ
```bash
python -m venv venv
source venv/bin/activate  # Windows の場合: venv\Scripts\activate
pip install -r backend/requirements.txt
```

### 4️⃣ DynamoDB Local の起動
```bash
cd backend/DynamoDBLocal
nohup java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb > dynamodb.log 2>&1 &
```

### 5️⃣ FastAPI サーバーの起動
```bash
cd backend
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### 6️⃣ フロントエンドのセットアップと起動
```bash
cd frontend
npm install
npm run dev
```

## ✅ 動作確認
- API: `http://localhost:8000/docs`
- フロントエンド: `http://localhost:3000`

🚀 **これで開発環境が整いました！**
