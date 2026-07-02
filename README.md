# Claude Code ハンズオン: 壊れた売上レポートツールを立て直す

Claude Code の基本操作を、実際の業務に近いシナリオで体験するハンズオン教材です。

## シナリオ

あなたは、社内で使われている「売上CSVから月次レポートを生成するツール」の
面倒を見ることになりました。ところが月初早々、営業事務から
「6月分のレポートが出せない」というバグ報告（`docs/bug_report.md`）が届きます。

Claude Code を使って、このツールを **直し、整え、拡張し、最後は自分の資産にする** ——
それがこのハンズオンのゴールです。

> **注意**: このリポジトリには学習用の意図的なバグが含まれています。

## 必要な環境

- Python 3.9 以上（標準ライブラリのみ使用。pip install は不要）
- [Claude Code](https://code.claude.com/docs/en/quickstart)
- テスト実行用に pytest（工程②で使います）: `pip install pytest`

## セットアップ（5分）

```bash
git clone <このリポジトリのURL>
cd csv-report-handson
```

動作確認（5月分は正常に出力できます）:

```bash
python3 -m report_tool.cli data/sales_2026.csv --month 2026-05
cat report_2026-05.md
```

6月分を実行するとエラーになります。これがハンズオンの出発点です:

```bash
python3 -m report_tool.cli data/sales_2026.csv --month 2026-06
```

## リポジトリ構成

```
├── README.md          # このファイル
├── EXERCISES.md       # 課題シート（ここを読みながら進める）
├── data/
│   ├── sales_2026.csv   # 2026年1〜6月の売上データ
│   └── sales_edge.csv   # 発展課題用（欠損値などを含む）
├── report_tool/       # レポート生成ツール本体
│   ├── loader.py        # CSV読み込み
│   ├── aggregate.py     # 集計
│   └── cli.py           # コマンドライン入口
├── tests/             # テスト（最初は空。あなたが育てます）
└── docs/
    └── bug_report.md    # 顧客からのバグ報告（工程②の入力）
```

## 進め方

`EXERCISES.md` を開いて、工程①から順に進めてください。
講習に参加した方は、ライブで見た工程も自分の手で再現するところから始めるのがおすすめです。

## 進めるうえでの心構え

- **permission mode は既定のまま**にしてください。Claude Code が何をしようと
  しているかを確認して承認する、というリズム自体が学習内容の一部です。
- エージェントの提案は**必ず読んでから承認**する癖をつけましょう。
  業務で使うときの安全の型になります。
- 失敗しても大丈夫です。`/rewind` でいつでも巻き戻せます（工程③で体験します）。
