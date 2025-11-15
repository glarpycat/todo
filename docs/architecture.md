# アーキテクチャ概要

このドキュメントでは Todo プロジェクトの構成要素、連携方法、拡張・デプロイ時に考慮すべきポイントを整理します。

## コンポーネント構成

- **フロントエンド (`frontend/`)**: Next.js 14（App Router）で実装された Todo UI。楽観的更新を行いつつ、REST 経由でバックエンドと通信します。
- **バックエンド (`backend/`)**: タスクの CRUD エンドポイントを公開する Flask サービス。JSON でデータをやり取りします。
- **ドキュメント (`docs/` と `mkdocs.yml`)**: MkDocs 用のソース。`site/` に静的サイトとしてビルドされ、ナレッジが公開されます。

単一リポジトリ構成により、フロントエンド・バックエンド・ドキュメントの変更をまとめて管理できます。

## 実行時フロー

1. フロントエンドがブラウザーの `fetch` API を使ってバックエンドへ HTTP リクエストを送信。
2. Flask のルートがリクエストを受け取り、メモリ上のタスクリストを操作して JSON 応答を返却。
3. フロントエンドが応答を状態に反映し、React UI を再描画。

```text
[React UI] --fetch--> [Flask API] --JSON--> [React UI]
```

## バックエンドサービス

- **フレームワーク**: Flask。`flask-cors` で Next.js 開発サーバーからのクロスオリジンアクセスを許可。
- **データ永続化**: デモ用データを保持するメモリ上のリスト (`tasks`)。再起動で初期化されるため、本番ではデータベース置換を推奨。
- **ルーティング**: `backend/app.py` に `GET /tasks`、`POST /tasks`、`PUT /tasks/<id>`、`DELETE /tasks/<id>` を定義。
- **バリデーション**: 作成時は `title` の必須チェック、更新時は `done` ブール値を必須化。
- **テスト**: `backend/tests/test_app.py` に `pytest` ベースの REST テストが配置されています。

### ローカル実行方法

```bash
# リポジトリルートから実行
source backend/.venv/bin/activate
flask --app backend.app run --port 5001
```

## フロントエンドアプリケーション

- **フレームワーク**: Next.js 14 + TypeScript。スタイリングは Tailwind CSS。
- **データアクセス**: `app/page.tsx` の `API_URL` 定数（`http://127.0.0.1:5001`）経由で Flask API を呼び出し。
- **状態管理**: React Hooks（`useState`、`useEffect`）でタスク一覧やフォーム入力を管理。
- **ユーザー操作**: タスクの追加、完了状態のトグル、削除を即時 UI 反映付きで提供。
- **スタイリング**: Tailwind クラスを `app/globals.css` や Tailwind 設定ファイルにて定義。

### ローカル実行方法

```bash
# リポジトリルートから実行
cd frontend
npm install
npm run dev
```

フロントエンドとバックエンドを同時に起動すると、`http://localhost:3000` にアクセスした際に UI が表示され、ポート `5001` の Flask API へリクエストがプロキシされます。

## 横断的な考慮事項

- **CORS**: 開発環境でのフロントエンド origin を許可するため `flask-cors` を利用。
- **エラーハンドリング**: バックエンドはバリデーションエラーや未検出リソースに対して HTTP ステータス（`400`、`404`）を返却。フロントエンドは失敗時にコンソールへログ出力。
- **テスト**: バックエンドは `pytest backend/` でテスト可能。フロントエンドは Playwright（`frontend/tests/todo.spec.ts`）による E2E テストをサポート。

## 今後の拡張案

- **永続化強化**: メモリリストではなく SQLite や PostgreSQL などのデータベース層を導入。
- **設定管理**: 環境変数で `API_URL` を外部化し、環境ごとの設定を分離。
- **デプロイ**: フロントエンド・バックエンドをコンテナ化、もしくは Vercel + マネージド API などのサービスを活用して本番展開。
