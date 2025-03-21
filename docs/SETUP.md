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


---

## 🔐 GitHub 連携 & SSHキー設定

### 7️⃣ GitHub に SSHキーを登録
```bash
ssh-keygen -t ed25519 -C "your-email@example.com"
cat ~/.ssh/id_ed25519.pub
# → GitHub アカウントに公開鍵を登録
```

### 8️⃣ GitHub へ push
```bash
git remote set-url origin git@github.com:<ユーザー名>/<リポジトリ名>.git
git add .
git commit -m "任意のコメント"
git push origin main
```

---

## 🌐 Nginx による静的配信設定

### 9️⃣ フロントエンドファイルを EC2 にアップロード
```powershell
scp -i "your-key.pem" index.html styles.css app.js ec2-user@<EC2-IP>:/home/ec2-user/AI_DB_UI/frontend/
```

### 🔟 Nginx を起動・確認
```bash
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl status nginx
```

📄 ブラウザで `http://<EC2-IP>/index.html` にアクセス
