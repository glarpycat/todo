# 技術スタック

Todo プロジェクトで採用している主要技術と選定理由、関連する設定場所を整理します。

## 言語・ランタイム

- **Python 3.12**: バックエンド API を実装。`backend/pyproject.toml` で依存関係とツールチェーンを管理。
- **TypeScript 5.x**: フロントエンド実装の型安全性と開発体験を向上。`frontend/tsconfig.json` に設定。
- **Node.js 22+**: Next.js アプリのビルド・実行環境。`frontend/package.json` に対応バージョンを指定。

## バックエンド

- **Flask**: シンプルな REST API を迅速に構築。`backend/app.py` にルーティングとビジネスロジックを定義。
- **Flask-CORS**: Next.js 開発サーバーからのクロスオリジンアクセスを許可。
- **Pytest**: API の回帰を防ぐテストフレームワーク。`backend/tests/test_app.py` にテストケースを配置。

### 依存管理

- `uv`（Python パッケージマネージャー）: `uv sync` でロックファイルに従って依存を導入し、`uv run` で仮想環境経由のコマンド実行を統合。
- `backend/pyproject.toml`: ランタイム・開発依存、ツール設定を一元管理。`uv.lock` はリポジトリルートに生成されます。

#### uv 運用メモ

- **インストール**: `curl -LsSf https://astral.sh/uv/install.sh | sh` などでグローバルに導入（詳細は公式ドキュメント参照）。
- **Python バージョン管理**: `uv python install 3.11` で必要なランタイムを取得し、`uv python pin 3.11` で `pyproject.toml` と同期。
- **依存の追加**: ランタイム依存は `uv add flask`、開発依存は `uv add --group dev pytest` のようにグループ別に管理。
- **ロック更新**: `uv lock` でバージョン差分を反映し、CI で同じ環境を再現。
- **仮想環境**: `uv sync` 実行時に `backend/.venv/` が生成される（存在する場合は再利用）。手動アクティベーションが必要な場合は `source backend/.venv/bin/activate`。

## フロントエンド

- **Next.js 14 App Router**: React ベースのフルスタックフレームワーク。ページ構成は `frontend/app/` 配下。
- **React 18**: コンポーネントベースの UI レイヤー。`frontend/app/page.tsx` に主要ロジックを実装。
- **Tailwind CSS**: ユーティリティファーストのスタイリング。`frontend/tailwind.config.ts` と `frontend/app/globals.css` を利用。
- **Playwright**: E2E テストツール。`frontend/tests/todo.spec.ts` で UI 振る舞いを検証。

### 依存管理

- `frontend/package.json`: npm 依存関係とスクリプト定義。
- `frontend/postcss.config.mjs` / `frontend/tailwind.config.ts`: ビルドパイプラインとスタイル設定。

## ドキュメント・ビルド

- **MkDocs + Material テーマ (導入予定)**: `mkdocs.yml` と `docs/` 配下の Markdown から静的サイトを生成。`mkdocs build` で `site/` に出力。
- **GitHub**: 単一リポジトリでバックエンド・フロントエンド・ドキュメントを一元管理。

## 開発フロー

1. `uv sync --frozen` を実行して Python 依存をセットアップ（`uv sync --dev` で開発依存も同期）。必要に応じて `uv run <command>` で仮想環境を手動で有効化せずにコマンド実行。
2. `frontend` ディレクトリで `npm install` を実行し、`npm run dev` でホットリロードを開始。
3. バックエンドは `flask --app backend.app run --port 5001` で起動。フロントエンドはポート `3000` で稼働。
4. テストは `pytest backend/` および `npx playwright test` を利用。

## 今後の選定候補

- **データベース**: SQLite / PostgreSQL など永続化層の導入。
- **インフラ**: Docker Compose によるローカル統合開発、もしくはクラウドデプロイ向け IaC（Terraform 等）。
- **監視**: バックエンドにログ集約（structlog など）や APM を追加して運用性を向上。
