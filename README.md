# Todo App

シンプルで使いやすいTodoアプリケーションです。FlaskをバックエンドAPI、Next.jsをフロントエンドUIとして構築されています。

## 🚀 機能

- ✅ タスクの追加
- ✅ タスクの完了/未完了切り替え
- ✅ タスクの削除
- ✅ リアルタイムでのUI更新
- ✅ レスポンシブデザイン

## 🛠️ 技術スタック

### バックエンド

- **Flask** - Pythonウェブフレームワーク
- **Flask-CORS** - Cross-Origin Resource Sharing対応
- **pytest** - テスティングフレームワーク

### フロントエンド

- **Next.js 14** - Reactベースのフレームワーク
- **TypeScript** - 型安全な開発
- **Tailwind CSS** - ユーティリティファーストなCSSフレームワーク
- **Playwright** - E2Eテスティング

## 📁 プロジェクト構造

```text
todo/
├── README.md
├── backend/
│   ├── app.py              # Flask API サーバー
│   ├── requirements.txt    # Python依存関係
│   ├── test_app.py        # バックエンドテスト
│   └── __pycache__/
└── frontend/
    ├── package.json        # Node.js依存関係
    ├── next.config.mjs     # Next.js設定
    ├── tailwind.config.ts  # Tailwind CSS設定
    ├── playwright.config.ts # Playwright設定
    ├── app/
    │   ├── globals.css     # グローバルスタイル
    │   ├── layout.tsx      # レイアウトコンポーネント
    │   └── page.tsx        # メインページコンポーネント
    └── tests/
        └── todo.spec.ts    # E2Eテスト
```

## ⚡ クイックスタート

### 前提条件

- Python 3.8+
- Node.js 18+
- npm または yarn

### インストールと実行

1. **リポジトリをクローン**

   ```bash
   git clone <repository-url>
   cd todo
   ```

2. **バックエンドの設定**

   ```bash
   # Python仮想環境の作成（推奨）
   python -m venv venv
   # Windows
   .\venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   
   # 依存関係のインストール
   pip install -r backend/requirements.txt
   
   # Flask サーバーの起動
   cd backend
   python app.py
   ```

   バックエンドAPIは `http://localhost:5001` で起動します。

3. **フロントエンドの設定**

   ```bash
   # 新しいターミナルで
   cd frontend
   
   # 依存関係のインストール
   npm install
   
   # 開発サーバーの起動
   npm run dev
   ```

   フロントエンドは `http://localhost:3000` で起動します。

## 🧪 テスト実行

### バックエンドテスト

```bash
cd backend
python -m pytest
```

### フロントエンド E2Eテスト

```bash
cd frontend
npx playwright test
```

## 📚 API エンドポイント

| メソッド | エンドポイント | 説明 |
|---------|---------------|------|
| GET     | `/tasks`      | 全てのタスクを取得 |
| POST    | `/tasks`      | 新しいタスクを作成 |
| PUT     | `/tasks/<id>` | 指定したタスクを更新 |
| DELETE  | `/tasks/<id>` | 指定したタスクを削除 |

### レスポンス例

#### GET /tasks

```json
[
  {
    "id": 1,
    "title": "Learn Flask",
    "done": true
  },
  {
    "id": 2,
    "title": "Build a Todo App",
    "done": false
  }
]
```

#### POST /tasks

```json
{
  "title": "新しいタスク"
}
```

## 🔧 開発

### バックエンド開発

- `backend/app.py` - メインのFlaskアプリケーション
- インメモリデータベース使用（本格運用時はPostgreSQL等を推奨）
- CORS設定済み

### フロントエンド開発

- React Hooks (useState, useEffect) を使用
- TypeScript による型安全性
- Tailwind CSS によるスタイリング
- フォーム送信とAPI通信

## 🚀 本番環境へのデプロイ

### バックエンドのデプロイ

- Gunicorn + Nginx の組み合わせを推奨
- 環境変数での設定管理
- データベースの導入 (PostgreSQL, MySQL等)

### フロントエンドのデプロイ

- `npm run build` でビルド
- Vercel, Netlify等での静的ホスティング
- 環境変数でAPIエンドポイントを設定

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 🤝 貢献

1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/AmazingFeature`)
3. 変更をコミット (`git commit -m 'Add some AmazingFeature'`)
4. ブランチをプッシュ (`git push origin feature/AmazingFeature`)
5. Pull Requestを作成

## 📞 サポート

問題や質問がある場合は、GitHubのIssuesページでお気軽にお知らせください。
